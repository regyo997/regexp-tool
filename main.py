from modules.LeoRegexpApplyTool import LeoRegexpApplyTool
from modules.LeoRegexpBuilder import LeoRegexpBuilder

regexp0 = LeoRegexpBuilder()\
    .match("hello world")\
    .ifBetween("<div>", "</div>")\
    .replaceWith("AAA")\
    .generate()

regexp1 = LeoRegexpBuilder()\
    .match("hello world")\
    .ifBetween("<div>", "</div>")\
    .thenBetween("<span>", "</span>")\
    .replaceWith("BBB")\
    .generate()

regexp2 = LeoRegexpBuilder()\
    .match("hello\w+world")\
    .ifBetween("<div>", "</div>")\
    .startsWith("bbb")\
    .thenContainThisBeforeMatch("ccc")\
    .thenBetween("<span>","</span>")\
    .endsWith('ggg')\
    .thenDontContainThisAfterMatch("fff")\
    .replaceWith("ABC")\
    .generate()

applyTool = LeoRegexpApplyTool()

# files = ["c:\\a.java", "d:\\b.jsp", "e:\\c.xml"]
files = ["c:\\a.java"]
# aaa
# <div>
#   bbb
#   ccc<span>ddd
#   eeehelloXXXworldfff
#   ggg</span>iii
#   jjj
# </div>
# kkk
print(regexp0.toString())
print(str(regexp1))
for file in files:
    # output = applyTool.apply(file, regexp0, regexp1, regexp2)
    output = applyTool.apply(file, regexp2)
    print("The result after applying regexp for file " + file + " is " + output)
