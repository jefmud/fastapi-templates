# fastapi test 1 with static routes
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# can import uvicorn and debug.
import uvicorn

app = FastAPI()

# handle the template and static files.
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}")
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get('/')
async def index(request:Request):
    # At a minimum, you must pass the request in the context
    context = {"request":request}
    return templates.TemplateResponse('index.html', context)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")