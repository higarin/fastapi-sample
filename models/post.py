from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)

    user = relationship("User", back_populates="posts")
