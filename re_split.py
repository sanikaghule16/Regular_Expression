import re
str_check=re.compile(r"[^A-Za-z\s.]")
str_name=input("\nplease enter your name:")
while str_check.search(str_name):
    print("\nplease enter your name correctly")
    str_name=input("\nplease enter your name:")
    
from re import split
print(re.split("\\W+",'words words worlds'))
print(re.split("\\W+","word's word worlds"))
print(re.split("\\W+",'on 12th jan 2028'))
print(re.split("\\d+","add the number 12"))
