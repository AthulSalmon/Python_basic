u=int(input("Enter the unit"))
if u<=100:
    amount=u*0.5
elif u>100 and u<=150:
    amount=(100*0.5)+((u-100)*0.75)
elif u>150 and u<=200:
    amount=(100*0.5)+(50*0.75)+((u-150)*1)
else:
    amount=(100*0.5)+(50*0.75)+(50*1)+((u-200)*2)
print("Amout",amount)
