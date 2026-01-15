import requests

class APITool:
    def __init__(self, base_url: str, api_key: str = None):
        self.base_url = base_url
        self.api_key = api_key

    def get(self, endpoint: str, params: dict = None) -> dict:
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=headers,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
