#regular expressions
import re
pattern=r"[\w.-]+@[\w.-]+"
string="Please send your fedback at info@oxford.com"
match=re.search(pattern,string)
if match:
    print("Email to:",match.group())
else:
    print("no match")
pattern=r"^[0-9]+ .*"
string="12 abc"
match=re.search(pattern,string)
if match:
    print("match")
result=re.findall(r'.',"good going")
print(result)
result1=re.findall(r'\w+',"good going")
print(result1)
result2=re.findall(r'\w+$',"good going")
print(result2)
result3=re.findall(r'\w\w\w',"good going")
print(result3)
result=re.findall(r'\d{2}-\d{2}-\d{4}','Hello, my name is mourya and my date of joining is 12-06-2020 and have experince of more than 8 years')
print("date of appointment is:",result)
list=['134567890','5625625625','8688459051','9515354051']
for i in list:
    result=re.findall(r'[7-9]{1}[0-9]{9}',i)
    if result:
        print(result,end=" ")
#vowels
pattern=r'[aeiou]'
if re.search(pattern,"cube"):
    print("\nmatch found")
else:
    print("not found")

    
 
