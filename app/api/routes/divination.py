from fastapi import APIRouter

router = APIRouter()

@router.get("/",summary="起卦接口")
def get_divination():
    return "起卦接口"