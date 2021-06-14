#---------------------- if ----------------------------
i = 10
if (i > 15):
   print ("10 is less than 15")
print ("I am Not in if")

#---------------------- if-else ----------------------------
i = 10
if (i >= 15):
    print("i is greater/equal to  15")
else:
    print("i is less than 5")


#---------------------- if-elif-else ----------------------------
i = 10
if (i >= 15):
    print("i is greater than/equal to 15")
elif(i<=5):
    print("i is less than/equal to 5")
else:
    print("i is less than 15 and grater than 5")

'''-----Nested if -------------
if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here
'''

x=5
print(1 < x < 10) #True
print(x < 10 < x*10 < 100) #True
print(10 < x < 20 ) #False