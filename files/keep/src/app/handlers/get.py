from keep.src.app.config import app


@app.get('/')
async def root():
    return {"message": 'hello'}