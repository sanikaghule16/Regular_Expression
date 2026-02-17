import re
pattern='^a...s$'
test_str='abyys'
result=re.match(pattern,test_str)
if result:
    print("search string Match successfully")
else:
    print("not Match")
print(result)

'''#get value from user
import re
pattern='^a...s$'
test_str=input("enter a string:")
result=re.match(pattern,test_str)
if result:
    print("search string Match successfully")
else:
    print("not Match")
print(result)'''
#we consider r for raw
import re
s='welcome.python'
match=re.search(r'.',s)#without \
print(match)
match=re.search(r'\.',s)#using '\' escape sequence
print(match)

import re
string="my name is sanika and my mobile number is 8010342071 and my friend name is Riya and her mobile number is 9766066081 and 9022345465"
pattern="\\d+"
result=re.findall(pattern,string)
print(result)

import re
p=re.compile('[a-e]')
string="sanika is a boss"
result=re.findall(p,string)
print(result)

import re
p=re.compile("\\w")
print(p.findall("he said me hello 12%$# times"))
