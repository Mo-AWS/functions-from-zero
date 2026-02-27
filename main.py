import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from mylib.bot import scrape
from pydantic import BaseModel

app = FastAPI()

class Wiki(BaseModel):
    name: str
    length: int

@app.post("/scrape")
async def scrape_wiki(wiki: Wiki):
    result = scrape(wiki.name, wiki.length)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Welcome to the Wikipedia API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

