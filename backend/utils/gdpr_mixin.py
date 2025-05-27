class PersonalDataMixin:
    __personal_data_fields__ = []

    @classmethod
    def get_personal_fields(cls):
        return cls.__personal_data_fields__
