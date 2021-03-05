# One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. 
# Each day thereafter, you go out double the number of bills. 
# How long does it take for the stack of bills to exceed the height of the tower?



def sears_height(doller_thickness, sears_height):
    number_of_bills = 1
    days = 1

    while doller_thickness * number_of_bills < sears_height:
        number_of_bills *= 2
        days += 1
        # print("days :", days)
        # print("dollar_thickness :", doller_thickness)
        final_dollar_height = number_of_bills * doller_thickness
        final_number_of_bills = number_of_bills
    return final_dollar_height, final_number_of_bills


sears_tall = 442
dollar_thick = 0.11 * 0.001

doller_height = sears_height(dollar_thick, sears_tall)
print(doller_height)