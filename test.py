from os import name
from fastapi import FastAPI,HTTPException, applications,requests
import uvicorn
from typing import List
from pydantic import BaseModel

import mysql.connector

class Data_entity(BaseModel):
    id: int
    name: str
    salary:int

app=FastAPI()





my_db=mysql.connector.connect(host="localhost",user="root",password="Kapil@7740",database="kumar")
my_cursor=my_db.cursor()

@app.post('/insert')
async def Entry(data:Data_entity):
    id=data.id
    name=data.name
    salary=data.salary
    try:
        my_cursor.execute(''' Insert INTO kkkk VALUES(%s,%s,%s)''',(id,name,salary))
        my_db.commit()
    except Exception as e:
        print(e)
        my_db.rollback()
        my_db.close()
        return f"Done !!"

@app.put('/update')
async def Edit(data:Data_entity):
    id=data.id
    name=data.name
    salary=data.salary
    try:
        my_cursor.execute(''' Update kkkk set name=%s,salary=%s where id=%s''',(id,name,salary))
        my_db.commit()
    except Exception as e:
        print(e)
        my_db.rollback()
        my_db.close()
        return f"Done !!"

@app.delete('/delete')
async def Remove(data:Data_entity):
    id=data.id

    my_cursor.execute(''' Delete from kkkk where id=%s''',(id,))
    my_db.commit()
    my_db.close()
    return f"Done !!"

@app.get('/show')
async def Entry():
    my_cursor.execute(''' Select * FROM kkkk ''')
    x=my_cursor.fetchall()
    print(x)
    return {
        "id":Data_entity.id,
        "name":Data_entity.name,
        "salary":Data_entity.salary

    }

if __name__=="__main__":
    uvicorn.run(app)

