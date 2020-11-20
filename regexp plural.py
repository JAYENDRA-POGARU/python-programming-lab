import re
def pluralize(noun):
    if re.search('[sxzh]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiousgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[aeiou]y$',noun):
        return re.sub('y$','ys',noun)
    else:
        return noun+'s'
list=["bush","fox","toy","boy"]
for i in list:
    print(i,'-',pluralize(i))
