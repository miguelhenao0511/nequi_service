from fastapi import FastAPI
from app.controllers import nequi_controller

app = FastAPI()

app.include_router(nequi_controller.router)