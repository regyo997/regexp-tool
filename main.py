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
    .replaceWith("$1ABC$3")\
    .generate()

applyTool = LeoRegexpApplyTool()

# files = ["c:\\a.java", "d:\\b.jsp", "e:\\c.xml"]
files = ["c:\\a.java"]
# vvv a.java
# aaa
# <div>
#   bbb
#   ccchello worldddd
#   eee
# </div>
# fff
for file in files:
    output = applyTool.apply(file, regexp0, regexp1, regexp2)
    print("The result after applying regexp for file " + file + " is " + output)
