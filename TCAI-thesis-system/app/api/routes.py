from fastapi import APIRouter

from app.models.schemas import AskRequest, AskResponse
from app.services.inference import InferenceService

router = APIRouter()
inference_service = InferenceService()


@router.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/ask", response_model=AskResponse, tags=["qa"])
def ask_question(payload: AskRequest) -> AskResponse:
    answer = inference_service.answer_question(payload.question)
    return AskResponse(answer=answer)
