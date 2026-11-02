import unittest
from gateway.policy import evaluate_request, validate_response

class PolicyTests(unittest.TestCase):
    def test_synthetic_reflection_allowed(self):
        self.assertEqual(evaluate_request({"synthetic": True, "task": "reflection", "text": "Why did the model change?"})["status"], "allow")

    def test_real_data_rejected(self):
        self.assertEqual(evaluate_request({"synthetic": False, "task": "reflection", "text": "hello"})["status"], "deny")

    def test_forbidden_tasks(self):
        for task in ("human_validation", "recognition", "grading", "profiling", "device_flash", "tool_execution"):
            with self.subTest(task=task):
                self.assertEqual(evaluate_request({"synthetic": True, "task": task, "text": "hello"})["status"], "deny")

    def test_unknown_task_denied(self):
        self.assertEqual(evaluate_request({"synthetic": True, "task": "other", "text": "hello"})["status"], "deny")

    def test_schema_and_authority(self):
        self.assertFalse(validate_response({"message": "ok", "human_validation": True}))
        self.assertFalse(validate_response({"message": "ok", "recognition": "badge"}))
        self.assertFalse(validate_response({"message": "", "requires_human_review": False}))
        self.assertTrue(validate_response({"message": "What would you test next?", "requires_human_review": False}))

if __name__ == "__main__":
    unittest.main()
