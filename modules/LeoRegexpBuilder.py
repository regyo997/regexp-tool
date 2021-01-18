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
        self._prefix = "(" + start
        self._suffix = end + ")"
        return self

    def thenBetween(self, start: str, end: str):
        self._prefix += ".*?)(" + start
        self._suffix = end + ")(.*?" + self._suffix
        self._concatDontContainPrifix(".*?)("+start)
        self._concatDontContainSuffix(end + ")(.*?")
        return self

    def startsWith(self, start: str):
        self._prefix += "\s*?)("+start
        self._concatDontContainPrifix("[\s]*?)("+start)
        return self

    def endsWith(self, end: str):
        self._suffix = end+")(\s*?"+self._suffix
        self._concatDontContainSuffix(end+")(\s*?")
        return self

    def notStartsWith(self, notStart: str):
        self._prefix += "\s*?)((?!"+notStart+")"
        self._concatDontContainPrifix("\s*?)((?!"+notStart+")")
        return self

    def notEndsWith(self, notEnd: str):
        self._suffix = "(?!"+notEnd+"))(\s*?"+self._suffix
        self._concatDontContainSuffix("(?!"+notEnd+"))(\s*?")
        return self

    def _concatDontContainPrifix(self, start: str):
        for i in range(len(self._dontContainPrefixs)):
            self._dontContainPrefixs[i] += start
        return self

    def _concatDontContainSuffix(self, end: str):
        for i in range(len(self._dontContainSuffixs)):
            end+self._dontContainSuffixs[i]
        return self

    def thenDontContainThisBeforeMatch(self, notContainBefore: str):
        self._dontContainPrefixs.append(
            self._prefix + ".*?)(" + notContainBefore)
        return self

    def thenDontContainThisAfterMatch(self, notContainAfter: str):
        self._dontContainSuffixs.append(
            notContainAfter + ")(.*?" + self._suffix)
        return self

    def replaceWith(self, value: str):
        self._replace = value
        return self

    def generate(self):
        match = self._prefix + ".*?)" + self._match + "(.*?" + self._suffix
        dontMatch = self._generateDontMatch()
        return LeoRegexp(match, self._replace, dontMatch)

    def _generateDontMatch(self):
        dontMatch = ""
        for dontContainPrefix in self._dontContainPrefixs:
            dontContainPrefix = dontContainPrefix + \
                ".*?)" + self._match + "(.*?" + self._suffix
            dontMatch += dontContainPrefix + "|"
        for dontContainSuffix in self._dontContainSuffixs:
            dontContainSuffix = self._prefix + \
                ".*?)" + self._match + "(.*?" + dontContainSuffix
            dontMatch += dontContainSuffix + "|"
        dontMatch = dontMatch.strip("|")
        return dontMatch

