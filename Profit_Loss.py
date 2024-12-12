print("Here, you can calculate profit or loss of your activity \n First,")
pur_cost = int(input("Enter the actual cost "))
sale_cost = int(input("Also \n Enter the sale cost "))

if(pur_cost < sale_cost):
    print("Your profit is about ", sale_cost-pur_cost, " doller")
else:
    print("No profit")
    if(pur_cost > sale_cost):
        print("Your loss is about ", pur_cost-sale_cost, " doller")
    else:
        print("Your actual cost and sale cost is equal")
