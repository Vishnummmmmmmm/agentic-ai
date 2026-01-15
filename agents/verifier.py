class VerifierAgent:
    def run(self, execution: dict) -> dict:
        issues = []

        if not execution.get("output"):
            issues.append("Empty output")

        if execution.get("confidence", 0) < 0.7:
            issues.append("Low confidence")

        return {
            "status": "PASS" if not issues else "FAIL",
            "issues": issues
        }
