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

    @property
    def dontContainPrefixs(self):
        return self._dontContainPrefixs

    @property
    def dontContainSuffixs(self):
        return self._dontContainSuffixs

    def __init__(self):
        self._match = ""
        self._prefix = ""
        self._suffix = ""
        self._replace = None
        self._prefixForNotContaintCheck = ""
        self._suffixForNotContaintCheck = ""
        self._dontContainPrefixs = []
        self._dontContainSuffixs = []

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
        self.appendToDontContainStrs(start, end)
        return self

    def appendToDontContainStrs(self, start: str, end: str):
        for i in range(len(self._dontContainPrefixs)):
            self._dontContainPrefixs[i] += "(" + start + ".*?)"
        for i in range(len(self._dontContainSuffixs)):
            self._dontContainSuffixs[i] = "(.*?" + end + ")" + self._dontContainSuffixs[i]

    def thenDontContainThisBeforeMatch(self, notContainBefore: str):
        self._dontContainPrefixs.append(
            self._prefix + "(" + notContainBefore + ".*?)")
        return self

    def thenDontContainThisAfterMatch(self, notContainAfter: str):
        self._dontContainSuffixs.append(
            "(.*?" + notContainAfter + ")" + self._suffix)
        return self

    def replaceWith(self, value: str):
        self._replace = value
        return self

    def generate(self):
        wholeRegexp = self._prefix + self._match + self._suffix
        dontContain = self.generateDontContain()
        return LeoRegexp(wholeRegexp, self._replace, dontContain)
    
    def generateDontContain(self):
        dontContain = ""
        for dontContainPrefix in self._dontContainPrefixs:
            dontContainPrefix = dontContainPrefix + self._match + self._suffix
            dontContain += dontContainPrefix + "|"
        for dontContainSuffix in self._dontContainSuffixs:
            dontContainSuffix = self._prefix + self._match + dontContainSuffix
            dontContain += dontContainSuffix + "|"
        dontContain=dontContain.strip("|")
        return dontContain
