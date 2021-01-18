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

    def startWith(self, start: str):
        self._prefix += "("+start+")"
        self._appendDontContainPrifix("("+start+")")
        return self

    def endsWith(self, end: str):
        self._suffix = "("+end+")"+self._suffix
        self._appendDontContainSuffix("("+end+")")
        return self

    def notStartWith(self, notStart: str):
        self._prefix += "(?!"+notStart+")"
        self._appendDontContainPrifix("(?!"+notStart+")")
        return self

    def notEndsWith(self, notEnd: str):
        self._suffix = "(?!"+notEnd+")"+self._suffix
        self._appendDontContainSuffix("(?!"+notEnd+")")
        return self

    def _appendDontContainPrifix(self,start: str):
        for i in range(len(self._dontContainPrefixs)):
            self._dontContainPrefixs[i] += start
        return self

    def _appendDontContainSuffix(self,end: str):
        for i in range(len(self._dontContainSuffixs)):
            self._dontContainSuffixs[i] += end
        return self
        
    def appendToDontContainStrs(self, start: str, end: str):
        for i in range(len(self._dontContainPrefixs)):
            self._dontContainPrefixs[i] += "(" + start + ".*?)"
        for i in range(len(self._dontContainSuffixs)):
            self._dontContainSuffixs[i] = "(.*?" + \
                end + ")" + self._dontContainSuffixs[i]

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
        match = self._prefix + self._match + self._suffix
        dontMatch = self.generateDontMatch()
        return LeoRegexp(match, self._replace, dontMatch)

    def generateDontMatch(self):
        dontMatch = ""
        for dontContainPrefix in self._dontContainPrefixs:
            dontContainPrefix = dontContainPrefix + self._match + self._suffix
            dontMatch += dontContainPrefix + "|"
        for dontContainSuffix in self._dontContainSuffixs:
            dontContainSuffix = self._prefix + self._match + dontContainSuffix
            dontMatch += dontContainSuffix + "|"
        dontMatch = dontMatch.strip("|")
        return dontMatch

    def __str__(self):
        return self._toString()

    def toString(self):
        match = self._prefix + self._match + self._suffix
        return match
