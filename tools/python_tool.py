class PythonTool:
    """
    Controlled Python execution tool.
    Only allow deterministic calculations.
    """

    def run(self, code: str) -> dict:
        allowed_builtins = {"sum": sum, "len": len, "min": min, "max": max}

        try:
            result = eval(code, {"__builtins__": allowed_builtins})
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}
