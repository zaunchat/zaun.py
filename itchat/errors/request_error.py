class NotVaildRequest(Exception):
    def __init__(self, message, request) -> None:
        self.message = message
        self.request = request