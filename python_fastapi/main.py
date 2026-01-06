from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field
# uvicorn main:app --reload

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     # 注意这里加了 f，大括号里的变量才会生效
#     return {"message": f"hello {name}"}

#访问/hello   响应结果 msg: 你好 FastAPI
@app.get("/hello")
async def get_hello():
    return{"msg":"你好FASTAPI"}

@app.get("/book/{id}")
async def get_book(id:int = Path(...,gt = 0,lt = 101,description="书籍的id")):
    return {"id":id,"title":f"这是第{id}本书"} 

#查找数据作者，路径参数 name ，长度范围 2-10
@app.get("/author/{name}")
async def get_name(name:str = Path(...,min_length=2,max_length=15)):
    return {"msg":f"这是{name}的信息"}


#需求 查询新闻 分页  skip：跳过的记录数，limit：返回的记录数 
@app.get("/news/news_list")
async def get_news_list(
    skip:int = Query(0,description="跳过的记录数",lt = 100),
    limit:int = 10
):
    return {"skip":skip,"limit":limit}

@app.get("/books")
async def get_books(
    # 1. 图书分类：
    # - 默认值："Python开发" (写在第一个参数)
    # - 长度限制：min_length=5, max_length=255
    category: str = Query("Python开发", min_length=5, max_length=255, description="图书分类"),
    
    # 2. 价格：
    # - 题目没说默认值，我们假设它是“必填”的，所以用 ... (Ellipsis)
    # - 范围限制：50 ~ 100。
    # - ge=50 (大于等于50), le=100 (小于等于100)
    price: int = Query(..., ge=50, le=100, description="价格")
):
    return {"category": category, "price": price, "msg": "查询成功"}

##请求体：POST PUT 
#注册：用户名与密码
class User(BaseModel):
    username:str = Field(default="ZAHNGSAN",min_length= 2 ,max_length= 10)
    password:str = Field(min_length=3,max_length=20)


@app.post("/register")
async def register(user :User):
    return user



 






class Book(BaseModel):
    title: str      # 书名
    author: str     # 作者
    publisher: str  # 出版社
    price: float    # 售价 (金额通常用 float 浮点数，或者 decimal)

# --- 第二步：编写接口 ---
@app.post("/add_book")
async def add_book(book: Book):
    # 这里通常会写保存到数据库的代码
    # 现在我们只是演示，直接把收到的数据打印出来或者返回回去
    print(f"收到了新书：{book.title}, 价格：{book.price}")
    
    return {"msg": "添加成功", "book_info": book}


