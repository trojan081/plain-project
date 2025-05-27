from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime



class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))

    creator = relationship("User", foreign_keys=[created_by])
    updater = relationship("User", foreign_keys=[updated_by])
    info = relationship("ProjectInfo", back_populates="project", uselist=False)
    versions = relationship("ProjectVersion", back_populates="project")



class ProjectStatus(Base):
    __tablename__ = "project_status"

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))

class ProjectInfo(Base):
    __tablename__ = "project_info"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    org_id = Column(Integer, ForeignKey("organizations.id"))
    cad_drafter_id = Column(String, ForeignKey("users.id"))
    project_manager = Column(String, ForeignKey("users.id"))
    project_status = Column(Integer, ForeignKey("project_status.id"))
    area = Column(String)
    location = Column(String)
    regulation_document = Column(String)
    custom_status = Column(String)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    project = relationship("Project", back_populates="info")
    status = relationship("ProjectStatus", backref="project_infos")
    organization = relationship("Organization", backref="projects")
    cad_drafter = relationship("User", foreign_keys=[cad_drafter_id])
    manager = relationship("User", foreign_keys=[project_manager])

class ProjectVersion(Base):
    __tablename__ = "project_versions"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    version = Column(Integer)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    project = relationship("Project", back_populates="versions")

class UserProject(Base):
    __tablename__ = "user_projects"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    project = relationship("Project", backref="user_links")
    user = relationship("User", foreign_keys=[user_id])


class AllRoadConstruction(Base):
    __tablename__ = "all_road_constructions"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    company_id = Column(Integer, ForeignKey("organizations.id"))
    construction = Column(JSON)
    name = Column(String, nullable=False)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", foreign_keys=[user_id])
    company = relationship("Organization", backref="road_constructions")

class ProjectRoadConstruction(Base):
    __tablename__ = "project_road_constructions"

    id = Column(Integer, primary_key=True)
    construction_id = Column(Integer, ForeignKey("all_road_constructions.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    type_number = Column(String)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    project = relationship("Project", backref="road_constructions")
    construction = relationship("AllRoadConstruction", backref="used_in_projects")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))
    reply_to_id = Column(Integer, ForeignKey("comments.id"), nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship("User", foreign_keys=[created_by])
    project = relationship("Project", backref="comments")
    reply_to = relationship("Comment", remote_side=[id])
