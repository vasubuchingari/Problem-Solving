s="hello aeiou iam the "
vowels="aeiou"
v_count=0
c_count=0

for x in s:
    if x in vowels:
        v_count=v_count+1
    elif x==" ":
        pass
    else:
        c_count=c_count+1
        
print(v_count,c_count)
