from fastapi import FastAPI, staticfiles
from fastapi.staticfiles import StaticFiles

from app.config import config


def create_app():
    app = FastAPI(
        debug=config.app.debug,
        title=config.app.title,
    )

    app.mount("/static", StaticFiles(directory="./app/static"), name="static")

    @app.get("/health_check", tags=["monitoring"], include_in_schema=False)
    async def health_check():
        return {
            "status": True,
            "message": f"The service {app.title} is running!",
        }

    return app
