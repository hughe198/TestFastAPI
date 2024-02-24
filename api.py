from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def read_root():
    return{"message":"This is a new message!"}
