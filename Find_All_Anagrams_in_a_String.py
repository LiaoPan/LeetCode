import re

s= "cbaebabacd"
p= "abc"
reg = r'(?=.*a)(?=.*b)(?=.*c)'
ret = re.match(reg,s)

print ret.group()

# for i in ret:
#     print i.start()