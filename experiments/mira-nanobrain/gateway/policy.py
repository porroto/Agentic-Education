"""Fail-closed research gateway. No model, network, storage or device access."""
ALLOWED_TASKS = frozenset({"reflection", "socratic_hint", "stem_question"})
FORBIDDEN_FIELDS = frozenset({"human_validation", "learning_proof", "recognition", "grade", "score", "profile", "tool_call", "device_command"})
MAX_TEXT = 2000

def evaluate_request(request):
    if not isinstance(request, dict):
        return {"status": "deny", "reason": "invalid_request"}
    if request.get("synthetic") is not True:
        return {"status": "deny", "reason": "synthetic_only"}
    if request.get("task") not in ALLOWED_TASKS:
        return {"status": "deny", "reason": "task_not_permitted"}
    text = request.get("text")
    if not isinstance(text, str) or not text.strip() or len(text) > MAX_TEXT:
        return {"status": "deny", "reason": "invalid_text"}
    if set(request) - {"synthetic", "task", "text", "language", "id"}:
        return {"status": "deny", "reason": "unknown_fields"}
    if request.get("language", "en") not in ("en", "es"):
        return {"status": "deny", "reason": "unsupported_language"}
    return {"status": "allow", "reason": "synthetic_research_only"}

def validate_response(response):
    if not isinstance(response, dict) or set(response) != {"message", "requires_human_review"}:
        return False
    message = response["message"]
    return (isinstance(message, str) and bool(message.strip()) and len(message) <= MAX_TEXT
            and type(response["requires_human_review"]) is bool)

def safe_fallback():
    return {"message": "This research response is unavailable. Ask an authorized human for help.", "requires_human_review": True}
