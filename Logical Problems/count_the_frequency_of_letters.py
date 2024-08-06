s="hello aeiou iam the "
dic={}
for x in s:
    if x==" ":
        pass
    elif x in dic:
        dic[x]=dic[x]+1
    else:
        dic[x]=1
        
for key in dic.keys():
    print(key,":",dic[key])
    
print(dic)
