from buy import Buy

class EbayClient:
    def __init__(self, api_key: str, sandbox: bool = False, version: int = 1):
        self._key = api_key
        self.sandbox = sandbox
        self.api_ver = f"v{version}"
        self.buy = Buy(self)

    def api_query(self, uri, method, result_model):
        pass
