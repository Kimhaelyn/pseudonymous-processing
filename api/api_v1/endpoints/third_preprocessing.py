from fastapi import APIRouter
from crud.db_crud import read_data
from api.api_v1.endpoints.second_preprocessing import second_preprocess

router = APIRouter()

update_data = []
age = [0, 0, 0, 0]

@router.get('/third')
async def second_preprocess():
    
    #for�� ���� ���� start ��� 
    # 1. ������ ���̽� �о����
    data = await read_data()
    
    
    #print(data, flush=True)
    
    for privacy in data:
        privacy = privacy.dict()
        
        for cell in privacy['cells']:
            #2. age_distribution ����
            del cell['age_distribution']
            
            #3. age_distribution �߰� 
            cell['age_distribution'] ={
                "youth": 0,
                "middle_aged": 0,
                "senior": 0, 
                "elderly": 0
            }
            
            print(cell, flush=True)

            #4. 2�ܰ� ���� ó�� 
            for person in cell['people']:
                
                #print(person, flush=True)
                
                # 3. IMSI ���� �����, ��ȭ��ȣ �����
                del person['mobile_number']
                del person['IMSI']
                
                # 4. ���� ���� ó�� 
            
                if person['age'] > 20 and person['age'] <30 :
                    person['age'] = 'mid_20s'
                    age[0]+=1
                
                elif person['age'] > 30 and person['age'] < 40 :
                    person['age'] = 'mid_30s'
                    age[0]+=1
                
                elif person['age'] > 40:
                    person['age'] = 'mid_40s'   
                    age[1]+=1
                
            
            
            cell['age_distribution']['youth'] = age[0]
            cell['age_distribution']['middle_aged'] = age[1]
            cell['age_distribution']['senior'] = age[2]
            cell['age_distribution']['elderly'] = age[3]
        
        update_data.append(privacy) 
        
        #end�ð� ����ٰ� ��� update_data�� �ð� �߰� -> ȭ�鿡 ��ȯ�ϱ� 
        
                     
    return update_data
        