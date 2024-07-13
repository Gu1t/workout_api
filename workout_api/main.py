import logging
from fastapi import FastAPI
from workout_api.routers import api_router
from fastapi_pagination import add_pagination

# Configuração básica do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

add_pagination(app)

@app.on_event("startup")
async def startup_event():
    logger.info("Aplicativo iniciado")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Aplicativo encerrado")