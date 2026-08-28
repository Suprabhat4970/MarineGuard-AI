from fastapi import APIRouter

router = APIRouter(
    prefix="/vessels",
    tags=["Vessels"]
)

@router.get("/")
def get_vessels():
    return{
        "message": "vessel service is working"
    }