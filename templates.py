from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Request
app = FastAPI()
# @app.get("/hello/")
# async def hello():
#     ret='''
# <html>
# <body>
# <h2>Hello World!</h2>
# </body>
# </html>
# '''
#     return HTMLResponse(content=ret)

templates = Jinja2Templates(directory="templates")
@app.get("/hellohii/{name}", response_class=HTMLResponse)
async def hellohii(request: Request,name:str):
    return templates.TemplateResponse("hello.html", {"request": request,"name":name})