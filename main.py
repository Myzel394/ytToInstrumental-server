import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import router
from utils.startup import startup_initialize

load_dotenv()

debug = bool(os.getenv("DEBUG", 1))


def get_application() -> FastAPI:
    application = FastAPI(
        debug=debug,
        title="YT2Instrumental",
    )
    
    application.include_router(router)
    
    application.mount("/static", StaticFiles(directory="static"), name="static")
    
    @application.on_event("startup")
    async def handle_startup():
        startup_initialize()
    
    return application


app = get_application()

if __name__ == "__main__":
    if debug:
        import uvicorn
        
        uvicorn.run(app)
