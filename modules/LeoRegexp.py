class LeoRegexp:

    @property
    def match(self):
        return self._match

    @property
    def replace(self):
        return self._replace

    @property
    def dontMatch(self):
        return self._dontMatch

    def __init__(self, match: str, replace: str, dontMatch: str):
        self._match = match
        self._replace = replace
        self._dontMatch = dontMatch

    def toString(self):
        return self._match
        
    def __str__(self):
        return self.toString()