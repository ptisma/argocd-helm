from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"Status":"OK"}

@app.get("/hostname")
def hostname():
    hostname = os.getenv('HOSTNAME', 'hostname')
    return {"Hostname": hostname}

@app.get("/")
def root():
    return {"Msg": "Hello world!"}
