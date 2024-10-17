name =  input("Enter your name: ")
section = input("Enter your section: ")

prelim = float(input("Enter your Prelim Grade: "))
if prelim <40 or prelim >100:
   print("Error")
   
else:
    midterm = float(input("Enter your Midterm Grade: "))
    if midterm <40 or midterm >100:
        print("Error")
        
    else:
        finalterm = float(input("Enter your final Grade: "))
        if finalterm <40 or finalterm >100:
            print("Error")
        else:   
            finalgrade = round((prelim * 0.33 + midterm * 0.33 + finalterm * 0.33))
            print(f"This is your total grade {finalgrade}")

        if finalgrade >100:
            print("Your Final Grade is 1.00")
    
        elif finalgrade >= 93 <=100:
            print("Your Final Grade is 1.00")
            
        elif finalgrade >= 81 <=92:
            print("Your Final Grade is 2.00")

        elif finalgrade >=75 <=80:
            print("Your Final Grade is 3.00")

        elif finalgrade <75 >=0:
            print("Your Final Grade is 5.00")
