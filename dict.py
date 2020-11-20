dict={'Roll_No':'19h61a0538','Name':'Jay','course':'B.tech'}
print(dict)
dict1={x:2*x for x in range(1,10)}
print(dict1)
print(dict['Roll_No'])
dict['marks']=85
print(dict)
dict['course']='M.tech'
print(dict)
del dict['marks']
print(dict)
dict.clear()
print(dict)
