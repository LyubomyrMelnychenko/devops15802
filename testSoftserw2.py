j=2
a=0
i = j
while i <=5 :
    print(f"i={i}")
    a+=1
    i+=1
    j=-j+i
print (f"кількість циклів={a}")
print (f"j={j}")
# dict
a = {'age':49}
print(a['age'])
b = a.get('age')
b = list([b])
print(b)
print(len(b))

