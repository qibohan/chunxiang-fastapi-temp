
from sqlmodel import SQLModel
from app.models.base_models.SMSCodeRecordBase import SMSCodeRecordBase
from app.models.base_models.UserBase import UserBase
from app.models.base_models.TodoBase import TodoBase

# 用户表
class User(UserBase, table=True):
    pass


# 短信发送记录
class SMSCodeRecord(SMSCodeRecordBase, table=True):
    pass

# Todo表
class Todo(TodoBase, table=True):
    pass