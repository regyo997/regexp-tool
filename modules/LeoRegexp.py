class LeoRegexp:

    @property
    def match(self):
        return self._match

    @property
    def replace(self):
        return self._replace

    @property
    def dontContain(self):
        return self._dontContain

    def __init__(self, match: str, replace: str, dontContain: str):
        self._match = match
        self._replace = replace
        self._dontContain = dontContain
