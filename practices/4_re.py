import re
p = re.compile("ca.e")

m = p.match('case')
print(m.group())
#. 하나의 문자    /  ^문자의 시작 / $문자의 끝  / 