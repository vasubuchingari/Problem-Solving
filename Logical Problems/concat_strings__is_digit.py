def rep(s1,s2):
    print(s1.replace(" ",s2))

rep("i am ok","&")

num="123333"
if num.isdigit():
    print("yes")
else:
    print("no")


def concat(s1,s2):
    res=""
    for x in s1:
        if x==" ":
            x=s2
        res+=x
        
    print(res)
            
s1="hello hiii hello"
s2="-"
concat(s1,s2)
