# R. Landon Goins
# Title: Honor Roll or Deans list
# This app will record a students first name, last name, and GPA and output to the user whether that student made the Deans List or Honor Roll

lastname = input("Enter Student Last Name: ")

while lastname != "ZZZ":  #Checking if the last name entered ZZZ

    firstname = input("Enter Student First Name: ")  #Asking to enter student First name

    gpa = float(input("Enter Student GPA: "))  #Asking to enter Student GPA

    #Checking if gpa is 3.5 or more
    if gpa >= 3.5:
        print("{} {} has made the Dean's List.".format(firstname, lastname))

    #Checking if gpa is 3.25 or more
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstname, lastname)) 
    lastname = input("\nEnter Student Last Name: ")
    #Repeating until 'ZZZ' entered