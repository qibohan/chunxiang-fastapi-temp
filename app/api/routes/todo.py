# from fastapi import APIRouter, Body

# router = APIRouter()

# @router.get("/all",summary="查询数据库中所有Todo")
# def get_all_todo():
#     return ""


# @router.post("/add",summary="添加Todo")
# def add_todo(text: str = Body(embed=True)):
#     return ""

from fastapi import APIRouter, Body, HTTPException
from sqlmodel import select
from app.models.public_models.Out import RespMod, ErrorMod
from app.api.depends import SessionDep
from app.models.table import Todo

router = APIRouter()

@router.get("/all", summary="查询数据库中所有Todo")
def get_all_todo(session: SessionDep):
    """获取所有待办事项"""
    try:
        statement = select(Todo)
        todos = session.exec(statement).all()
        return RespMod(
            message="获取待办事项成功",
            data=[todo.model_dump() for todo in todos]
        )
    except Exception as e:
        raise ErrorMod(f"获取待办事项失败: {str(e)}")

@router.post("/add", summary="添加Todo")
def add_todo(text: str = Body(embed=True), session: SessionDep = None):
    """添加新的待办事项"""
    try:
        # 检查是否已存在相同的待办事项
        statement = select(Todo).where(Todo.text == text)
        existing_todo = session.exec(statement).first()
        if existing_todo:
            raise ErrorMod("该待办事项已存在")
        
        # 创建新的待办事项
        new_todo = Todo(text=text, completed=False)
        session.add(new_todo)
        session.commit()
        session.refresh(new_todo)
        
        return RespMod(
            message="添加待办事项成功",
            data=new_todo.model_dump()
        )
    except ErrorMod:
        raise
    except Exception as e:
        raise ErrorMod(f"添加待办事项失败: {str(e)}")