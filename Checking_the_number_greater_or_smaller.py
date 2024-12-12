num = int(input("Enter a integer number "))

if(num>15):
    print(num, " is greter than 15 ")
    print("I am in if block")
elif(num<15):
    print(num, " is not greter than 15 ")
    print("I am in elif block")
else:
    print("I am in neither in if or elif block \nI am in else block")