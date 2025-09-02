
ENDPOINT = "https://api.sms.ir"


class BaseRequester:
    def __init__(self, logger) -> None:
        self.endpoint = ENDPOINT
        self.logger = logger
