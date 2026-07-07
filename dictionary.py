d={}
for i in range(2):
    key=input("Enter key:")
    value=input("Enter value:")
    d[key]=value
keys=list(d.keys())
for i in d[keys[0]]:
    for j in d[keys[1]]:
        print(i+j)
