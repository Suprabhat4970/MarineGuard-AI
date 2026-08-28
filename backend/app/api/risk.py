from fastapi import APIRouter

router = APIRouter(
    prefix="/risk",
    tags=["Risk"]
)


@router.get("/")
def get_risk():
    return {
        "message": "Risk service is working"
    }