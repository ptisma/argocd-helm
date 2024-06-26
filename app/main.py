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

@app.get("/secret")
def secret():
    secretStr = os.getenv('SECRET_STR')
    return {"Secret": secretStr}

@app.get("/notsecret")
def notSecret():
    notSecretStr = os.getenv('NOT_SECRET_STR')
    return {"NotSecret": notSecretStr}
