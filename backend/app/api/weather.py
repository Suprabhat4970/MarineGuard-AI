from fastapi import APIRouter

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/")
def get_weather():
    return {
        "message": "Weather service is working"
    }