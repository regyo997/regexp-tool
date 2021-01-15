class LeoRegexp:

    @property
    def match(self):
        return self._match

    @property
    def replace(self):
        return self._replace

    @property
    def notContain(self):
        return self._notContain

    def __init__(self, match: str, replace: str, notContain: str):
        self._match = match
        self._replace = replace
        self._notContain = notContain
