def i_tri(s):
    return "Starting Line... Good Luck!" if s == 0 else "You're done! Stop running!" if s >= 140.8 else ({"Swim":"{:0.2f}".format(140.6-s)+" to go!"} if s <= 2.4 else {"Bike":"{:0.2f}".format(140.6-s)+ " to go!"} if s <= 114.4 else {"Run": "{:0.2f}".format(140.6-s)+" to go!"} if s<= 130.6 else {"Run":"Nearly there!"})

print(i_tri(36))


# print("{:0.2f}".format(1.5))