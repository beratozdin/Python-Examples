# This is a basic tip calculator program.

price=float(input("Please, enter the price($):"))
percentage=float(input("Please, enter the percentage of tip(%):"))
number_of_people=int(input("Please, enter the number of people:"))

tip=price*(percentage/100.0)
total_price=price+tip

if number_of_people==1:
    print(f"Tip($): {tip}\nTotal amount($): {total_price}")
else:
    print(f"Tip(Ş): {tip}\nTotal amount($) : {total_price}")
    print(f"Tip per person($): {tip/number_of_people}\nAmount per person($): {total_price/number_of_people}")




