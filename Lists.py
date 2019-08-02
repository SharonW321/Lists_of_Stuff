Women_in_tech = ["Dr. Aprille Joy Ericsson", "Cindy Alvarez", "Dorothy Vaughan", "Jess Lee", "Amanda Randles"]
Girls_Who_Code = ["Naomi", "Syd", "Erin", "Kim"]
#print(Girls_Who_Code)
#print(len(Girls_Who_Code))
#print(Girls_Who_Code)
#print(Women_in_tech)
#print("These people have  lot more in common than they think!")
if "Beyonce" in Girls_Who_Code:
    print("beyonce is in Girls_Who_Code")
else:
    print("Beyonce is not in Girls_Who_Code")
Girls_Who_Code.append("Sharon")
for each in Girls_Who_Code:
    print(each)
Women_in_tech.insert(3,"Sharon")
print(Girls_Who_Code)
print("These people have lot more in common than they think!")
print(Women_in_tech)
print(*Girls_Who_Code)
for index in range(len(Girls_Who_Code)):
    print(Girls_Who_Code[index])
