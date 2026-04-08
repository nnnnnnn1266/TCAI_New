class InferenceService:
    """Mock inference service for turtle-care QA."""

    def answer_question(self, question: str) -> str:
        q = question.lower().strip()

        if "bask" in q:
            return "Turtles bask to regulate body temperature and absorb UVB light for shell and bone health."
        if "eat" in q or "diet" in q or "food" in q:
            return "Most pet turtles need a varied diet of pellets, leafy greens, and species-appropriate protein."
        if "water" in q or "tank" in q:
            return "Keep clean, filtered water and maintain species-appropriate temperature and basking areas."

        return (
            "I am a mock Turtle Care AI assistant. In a future version, this response will come from "
            "a fine-tuned LLM specialized in turtle care."
        )
