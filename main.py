from fastapi import FastAPI, UploadFile, Form, Response
# FastAPI 라이브러리에서 주요 기능을 가져온다.
# FastAPI : 애플리케이션 인스턴스를 생성
# UploadFile : 파일 업로드, Form : html 폼 데이터를 처리, Response : 사용자 정의 응답 반환
from fastapi.responses import JSONResponse
# JSON 형식의 응답을 쉽게 반환할 수 있게 해준다.
from fastapi.encoders import jsonable_encoder
# python 객체를 json 형식으로 변환
from fastapi.staticfiles import StaticFiles
# 이미지나 CSS 등 정적인 파일을 제공
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from typing import Annotated
# 타입을 명확하게 할 수 았도록 해준다.
import sqlite3
# SQLite 데이터베이스와 상호작용하기 위한 모듈

con = sqlite3.connect("hello.db", check_same_thread=False)
cur = con.cursor()
# 데이터베이스 작업을 수행할 수 있는 커서를 생성
# cursor : 명령을 실행하고 결과를 가져오는 작업을 수행하는데 사용

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
# NOT EXISTS : 이미 같은 이름의 테이블이 존재할 경우 생성하지 않도록 한다.

app = FastAPI() # FastAPI를 호출

SECRET = "super-coding"
manager = LoginManager(SECRET,'/login')

@manager.user_loader()
def query_user(id):
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    user = cur.execute(f"""
                       SELECT * from users WHERE id = '{id}'
                       """).fetchone()
    return user

@app.post('/login')
def login(id:Annotated[str,Form()],
          password:Annotated[str,Form()]):
    user = query_user(id)
    print(user['password'])
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    
@app.post('/signup')
def signup(id:Annotated[str,Form()],
           password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    cur.execute(f"""
                INSERT INTO users(id, name, email, password)
                VALUES('{id}','{name}','{email}','{password}')
                """) #DB에 저장
    con.commit() #connection을 확정 짓는다.
    return '200'

@app.post("/items") #/items 경로로 들어오는 POST 요청을 처리하는 함수
async def create_item(image:UploadFile, 
                title:Annotated[str,Form()],  # html 폼에서 title 값을 가져온다. 타입은 str
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()], 
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]):
    
    image_bytes = await image.read() #비동기적으로 업로드된 이미지를 image_bytes에 저장, 이진 형식
    cur.execute(f"""
                INSERT INTO 
                items(title, image, price, description, place, insertAt)
                VALUES ('{title}','{image_bytes.hex()}',{price},'{description}','{place}','{insertAt}')
                """)
    # (title, image, price, description, place)의 값을 갖는 테이블에
    # VALUES ('{title}','{image_bytes.hex()}','{price}','{description}','{place}') 값을 넣어주겠다.
    # mage_bytes.hex() : 이미지 데이터를 16진수 문자열로 변환하여 저장, BLOB 데이터 형식으로 저장하기 위한 처리
    con.commit()
    return JSONResponse(content={"status": "success", "code": 200})

#모든 아이템 가져오기
@app.get('/items') 
async def get_itmes(): 
    con.row_factory = sqlite3.Row #데이터의 컬럼명도 같이 가져오는 문법, 이를 통해 각 행을 키-값 쌍으로 쉽게 접근할 수 있다.
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * from items;
                       """).fetchall()
    return JSONResponse(jsonable_encoder(
        dict(row) for row in rows))
    # 가져온 데이터를 sonable_encoder로 JSON 형식으로 변환 > JSONResponse 를 사용해서 반환
    
    
@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id = {item_id}
                              """).fetchone()[0] 
    # .fetchone()[0] : 단일 결과를 가져올 때 사용
    # 특정 아이템의 이미지를 가져온다. 여기서 가져오는 이미지는 16진법, 헥스 형태
    return Response(content=bytes.fromhex(image_bytes)) 
    # image_bytes(16진법)를 가져와서 해석 > 바이트 형식으로 변환해서 Response를 하겠다.

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")