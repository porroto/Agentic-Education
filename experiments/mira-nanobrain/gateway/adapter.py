"""Simulation adapter only. No nanochat execution in M0-M2."""
from .policy import evaluate_request, validate_response, safe_fallback

def simulate(request):
    decision = evaluate_request(request)
    if decision["status"] != "allow":
        return {"status": "denied", "reason": decision["reason"], "response": safe_fallback()}
    candidate = {"message": "What evidence or observation could help you investigate that?", "requires_human_review": False}
    if not validate_response(candidate):
        return {"status": "denied", "reason": "invalid_model_output", "response": safe_fallback()}
    return {"status": "simulated", "response": candidate}
