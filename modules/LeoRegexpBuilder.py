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

    @property
    def prefixForNotContaintCheck(self):
        return self._prefixForNotContaintCheck

    @property
    def suffixForNotContaintCheck(self):
        return self._suffixForNotContaintCheck

    def __init__(self):
        self._match = ""
        self._prefix = ""
        self._suffix = ""
        self._replace = None
        self._prefixForNotContaintCheck = ""
        self._suffixForNotContaintCheck = ""
    def match(self, pattern: str):
        self._match = "(" + pattern + ")"
        return self

    def ifBetween(self, start: str, end: str):
        self._prefix = "(" + start + ".*?)"
        self._suffix = "(.*?" + end + ")"
        self._prefixForNotContaintCheck = "(" + start + ".*?)"
        self._suffixForNotContaintCheck = "(.*?" + end + ")"
        return self

    def thenBetween(self, start: str, end: str):
        self._prefix += "(" + start + ".*?)"
        self._suffix = "(.*?" + end + ")" + self._suffix
        self._prefixForNotContaintCheck += "(" + start + ".*?)"
        self._suffixForNotContaintCheck = "(.*?" + \
            end + ")" + self._suffixForNotContaintCheck
        return self

    def thenDontContainThisBeforeMatch(self, notContainBefore: str):
        self._prefixForNotContaintCheck += "(" + notContainBefore + ".*?)"
        return self

    def thenDontContainThisAfterMatch(self, notContainAfter: str):
        self._suffixForNotContaintCheck = "(.*?" + notContainAfter + ")" + self._suffixForNotContaintCheck
        return self

    def replaceWith(self, value: str):
        self._replace = value
        return self

    def generate(self):
        wholeRegexp = self._prefix+self._match+self._suffix
        notContainRegexp = self._prefixForNotContaintCheck + \
            self._match+self._suffixForNotContaintCheck
        if notContainRegexp == wholeRegexp:
            notContainRegexp = None
        return LeoRegexp(wholeRegexp, self._replace, notContainRegexp)
