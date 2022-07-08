from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from app.database import Base

class Post(Base):
  __tablename__ = "posts"
  
  id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
  title = Column(String(50), nullable=False)
  content = Column(String(50), nullable=False)
  published = Column(TINYINT(1, unsigned=True), server_default=text('1'), nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
  owner_id = Column(INTEGER(unsigned=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  
  owner = relationship("User")
  
class User(Base):
  __tablename__ = "users"
  
  id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
  
class Vote(Base):
  __tablename__ = "votes"
  
  user_id = Column(INTEGER(unsigned=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
  post_id = Column(INTEGER(unsigned=True), ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
  
  