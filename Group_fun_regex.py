#group
import re
s="welcome to smbst college"
result=re.search(r"\D{4}g",s)
print(result.group())

# set password

import re

def main():
    passwd = input("Enter the password:")
    
    reg = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!#])[A-Za-z\d@$!#]{6,20}$'
    
    # compiling regex
    pat = re.compile(reg)
    
    # searching regex
    mat = re.search(pat, passwd)
    
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")

# Driver Code
if __name__ == '__main__':
    main()

