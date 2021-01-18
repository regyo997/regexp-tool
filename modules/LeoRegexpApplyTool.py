from modules.LeoRegexp import LeoRegexp
import os
import re
import copy
from typing import List


class LeoRegexpApplyTool:

    def __init__(self):
        pass

    def apply(self, filePath: str, *regexps: List[LeoRegexp]):
        fileText = self._readFile(filePath)
        output = fileText
        for regexp in regexps:
            matchedTexts = self._matchAndExcludeDontMatch(fileText, regexp)
            output = self._replace(fileText, matchedTexts, regexp.replace)
        return output

    def _readFile(self, filePath: str):
        file = open(filePath, 'r')
        fileText = file.read()
        file.close()
        return fileText

    def _matchAndExcludeDontMatch(self, fileText: str, regexp: LeoRegexp):
        matchedTexts = []
        for reMatch in re.finditer(regexp.match, fileText, re.DOTALL):
            if(reMatch != None and self._hasNotDontMatch(reMatch.group(), regexp.dontMatch)):
                matchedTexts.append(reMatch.group())
        return matchedTexts

    def _hasNotDontMatch(self, matchedText: str, dontMatch: str):
        hasNotDontMatch = True
        if(dontMatch != '' and re.search(dontMatch, matchedText, re.DOTALL) != None):
            hasNotDontMatch = False
        return hasNotDontMatch

    def _replace(self, fileText: str, matchedTexts: List[str], replace: str):
        output = copy.deepcopy(fileText)
        if(replace != None):
            for matchedText in matchedTexts:
                output = output.replace(matchedText, replace, 1)
        return output
