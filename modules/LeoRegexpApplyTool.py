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
            output = self._doRegProcess(regexp, output)
        return output

    def _readFile(self, filePath: str):
        file = open(filePath, 'r')
        fileText = file.read()
        file.close()
        return fileText

    def _doRegProcess(self, regexp: LeoRegexp, inputText: str):
        outputText = inputText
        for regexpMatch in re.finditer(regexp.match, outputText, re.DOTALL):
            if(regexpMatch != None):
                outputText = self._replaceOrNot(
                    regexp, regexpMatch, outputText)
        return outputText

    def _replaceOrNot(self, regexp: LeoRegexp, regexpMatch: List[re.Match], inputText: str):
        outputText=inputText
        if(regexp.replace != None):
            outputText = self._generateReplaceText(
                regexp, regexpMatch, outputText)
        return outputText

    def _generateReplaceText(self, regexp: LeoRegexp, regexpMatch: List[re.Match], inputText: str):
        replaceWithThisStr = self._parseDollerSignToTextStr(
            regexp, regexpMatch)
        howManyGroup = len(regexpMatch.groups())
        middleMatchGroupNum = (howManyGroup//2+1)
        matchGroupStr = regexpMatch.group(middleMatchGroupNum)
        output = inputText.replace(matchGroupStr, replaceWithThisStr)
        return output

    def _parseDollerSignToTextStr(self, regexp: LeoRegexp, regexpMatch: List[re.Match]):
        finishParsedReplaceStr = regexp.replace
        howManyGroup = len(regexpMatch.groups())
        for groupNum in range(howManyGroup, 0, -1):
            groupText = regexpMatch.group(groupNum)
            finishParsedReplaceStr = finishParsedReplaceStr.replace(
                '$'+str(groupNum), groupText)
        return finishParsedReplaceStr
