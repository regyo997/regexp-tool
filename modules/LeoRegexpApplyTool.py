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
        for reMatch in re.finditer(regexp.match, outputText, re.DOTALL):
            outputText = self._geneateOutputText(regexp, reMatch, outputText)
        return outputText

    def _geneateOutputText(self, regexp: LeoRegexp, reMatch: List[re.Match], inputText: str):
        outputText = inputText
        if(reMatch != None and self._isNotUndesiredWordsContain(regexp,reMatch)):
            outputText = self._replaceTextOrNot(
                regexp, reMatch, outputText)
        return outputText

    def _isNotUndesiredWordsContain(self, regexp: LeoRegexp, reMatch: List[re.Match]):
        isNotContain = True
        notContainRegexp = regexp.notContain
        matchText = reMatch.group()
        print(re.search(notContainRegexp,matchText,re.DOTALL))
        if(notContainRegexp != None and re.search(notContainRegexp,matchText,re.DOTALL)!=None):
            isNotContain=False
        return isNotContain

    def _replaceTextOrNot(self, regexp: LeoRegexp, reMatch: List[re.Match], inputText: str):
        outputText = inputText
        if(regexp.replace != None):
            outputText = self._generateReplaceText(
                regexp, reMatch, outputText)
        return outputText

    def _generateReplaceText(self, regexp: LeoRegexp, reMatch: List[re.Match], inputText: str):
        replaceWithThisStr = self._parseDollerSignToTextStr(
            regexp, reMatch)
        howManyGroup = len(reMatch.groups())
        middleMatchGroupNum = (howManyGroup//2+1)
        matchGroupStr = reMatch.group(middleMatchGroupNum)
        output = inputText.replace(matchGroupStr, replaceWithThisStr)
        return output

    def _parseDollerSignToTextStr(self, regexp: LeoRegexp, reMatch: List[re.Match]):
        finishParsedReplaceStr = regexp.replace
        howManyGroup = len(reMatch.groups())
        for groupNum in range(howManyGroup, 0, -1):
            groupText = reMatch.group(groupNum)
            finishParsedReplaceStr = finishParsedReplaceStr.replace(
                '$'+str(groupNum), groupText)
        return finishParsedReplaceStr
