import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return


@app.route("/take_on_me")
async def root():
    return 'take me on'

uvicorn.run(app, host="localhost", port=8080, log_level="info", )
