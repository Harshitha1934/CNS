str="Hello World"
res=""
for i in str:
    x=ord(i) ^ 0
    c=chr(x)
    res+=c
print("Result of xor with 0: ", res)
res1=""
res2=""
for i in str:
    x1=ord(i) & 127
    c1=chr(x1)
    res1+=c1
    x2=ord(i) | 127
    c2=chr(x2)
    res2+=c2
print("AND: ", res1)
print("Or: ",res2)
