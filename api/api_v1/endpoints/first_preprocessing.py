from fastapi import APIRouter
from crud.db_crud import read_data

router = APIRouter()

@router.get('/first')
async def frist_preprocess():
    # 1. ������ ���̽� �о����
    data = await read_data()
    return  data

 
    
    
    
    