from fastapi import APIRouter

router = APIRouter(
    prefix="/routes",
    tags=["Routes"]
)


@router.get("/")
def get_routes():
    return {
        "message": "Route service is working"
    }