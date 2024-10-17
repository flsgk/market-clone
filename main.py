from fastapi import FastAPI, UploadFile, Form, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import sqlite3

con = sqlite3.connect("hello.db", check_same_thread=False)
cur = con.cursor()

cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
	            id INTEGER PRIMARY KEY,
	            title TEXT NOT NULL,
	            image BLOB,
	            price INTEGER NOT NULL,
	            description TEXT,
	            place TEXT NOT NULL,
	            inserAt INTEGER NOT NULL
            );
            """)

app = FastAPI()

@app.post("/items")
async def create_item(image:UploadFile, 
                title:Annotated[str,Form()],  
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()], 
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]):
    
    image_bytes = await image.read() #이미지를 읽을 시간을 주는 구문
    cur.execute(f"""
                INSERT INTO 
                items(title, image, price, description, place, insertAt)
                VALUES ('{title}','{image_bytes.hex()}',{price},'{description}','{place}','{insertAt}')
                """)
    # (title, image, price, description, place)의 값을 갖는 테이블에
    # VALUES ('{title}','{image_bytes.hex()}','{price}','{description}','{place}') 값을 넣어주겠다.
    con.commit()
    return '200'


@app.get('/items')
async def get_itmes():
    con.row_factory = sqlite3.Row #데이터의 컬럼명도 같이 가져오는 문법
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * from items;
                       """).fetchall()
    return JSONResponse(jsonable_encoder(
        dict(row) for row in rows))
    
    
@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    # 여기서 가져오는 이미지는 16진법, 헥스 형태
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id = {item_id}
                              """).fetchone()[0] # 하나를 가져올 때의 문법 (추가 학습 필요)
    return Response(content=bytes.fromhex(image_bytes)) # image_bytes 를 가져와서 해석 > bytes 로 변환해서 Response를 하겠다.


@app.post('/signup')
def signup(id:Annotated[str,Form()],
           password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    # cur.execute(f"""
    #             INSERT INTO users(id, name, email, password)
    #             VALUES('{id}','{name}','{email}','{password}')
    #             """) #DB에 저장
    # con.commit() #connection을 확정 짓는다.
    return '200'

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")