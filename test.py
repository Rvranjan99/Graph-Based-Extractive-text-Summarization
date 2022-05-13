
paragraph=open("paragraph.txt",'r')
x=paragraph.read()
s=x.split('\n')
print(s)
st=""
for i in s:
    if i!="":
        st+=i

print(x)
print(st)
