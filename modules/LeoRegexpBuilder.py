from modules.LeoRegexp import LeoRegexp


class LeoRegexpBuilder:

    @property
    def prefix(self):
        return self._prefix

    @property
    def suffix(self):
        return self._suffix

    @property
    def match(self):
        return self._match

    @property
    def replace(self):
        return self._replace

    def __init__(self):
        self._match = ""
        self._prefix = ""
        self._suffix = ""
        self._replace = None

    def match(self, pattern: str):
        self._match = "(" + pattern + ")"
        return self

    def ifBetween(self, start: str, end: str):
        self._prefix = "(" + start + ".*?)"
        self._suffix = "(.*?" + end + ")"
        return self

    def thenBetween(self, start: str, end: str):
        self._prefix += "(" + start + ".*?)"
        self._suffix = "(.*?" + end + ")" + self._suffix
        return self

    def replaceWith(self, value: str):
        self._replace = value
        return self

    def generate(self):
        wholeRegexp = self._prefix+self._match+self._suffix
        return LeoRegexp(wholeRegexp, self._replace)
