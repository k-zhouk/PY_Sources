test_str= "abcd"
sym= "x"
res= []

for i in range(len(test_str)+1):
    new_str1= test_str[0:i]
    new_str2= sym
    new_str3= test_str[i:len(test_str)]
    new_str= new_str1+ new_str2+ new_str3
    
    res.append(new_str)

print("\n")
print(res)
