# backend/utils/logger.py

from models.pdata_action import PDataAction
from datetime import datetime
from utils.ulid_generator import generate_ulid

def log_pdata_changes(db, old_obj, new_obj, user_id: str = None):
    cls = type(old_obj) if old_obj else type(new_obj)
    personal_fields = getattr(cls, "__personal_data_fields__", [])
    if not personal_fields:
        return

    # 🔹 Получаем только реально переданные (изменённые) поля
    updated_keys = set(new_obj.__dict__.keys()) - {"_sa_instance_state"}

    object_id = str(getattr(new_obj, "id", None) or getattr(old_obj, "id", None) or user_id)

    actions = []
    for field in personal_fields:
        if field not in updated_keys:
            continue  # 🔸 поле не передавалось в запросе — пропускаем

        old_val = getattr(old_obj, field, None) if old_obj else None
        new_val = getattr(new_obj, field, None) if new_obj else None

        # Удаление (если старое есть, а новое удалено)
        if old_obj and new_obj is None:
            actions.append(PDataAction(
                id=generate_ulid(),
                event_type="delete",
                object_type=cls.__tablename__,
                object_id=str(getattr(old_obj, "id")),
                field=field,
                old_value=str(old_val),
                new_value=None,
                performed_by=user_id,
                performed_at=datetime.utcnow()
            ))
        elif old_obj is None or old_val != new_val:
            actions.append(PDataAction(
                id=generate_ulid(),
                event_type="create" if old_obj is None else "update",
                object_type=cls.__tablename__,
                object_id=str(getattr(new_obj, "id")),
                field=field,
                old_value=str(old_val) if old_val is not None else None,
                new_value=str(new_val) if new_val is not None else None,
                performed_by=user_id,
                performed_at=datetime.utcnow()
            ))

    if actions:
        db.add_all(actions)
        db.commit()
