from .browse import Browse

class Buy:
    def __init__(self, client):
        self._client = client
        self.browse = Browse(client)
