def miles_to_kilometers():
    miles = float(input("Enter number of miles: "))
    conversion_factor = 1.609
    kilometers = miles * conversion_factor
    print(f"""{miles} miles is equal to {kilometers} kilometers""")

miles_to_kilometers()