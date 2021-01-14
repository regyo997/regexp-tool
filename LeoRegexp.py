class LeoRegexp:

    @property
    def match(self):
        return self._match

    @property
    def replace(self):
        return self._replace

    def __init__(self, match: str, replace: str):
        self._match = match
        self._replace = replace
