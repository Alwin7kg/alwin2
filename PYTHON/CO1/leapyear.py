#To find the leap year
#datetime
import datetime
current_year= datetime.date.today().year
#Get the final year from the user
final_year= int(input("Enter final year: "))
if final_year<current_year:
    print("final year must be greater than or equal to the current year.")
else:
    print(f"Leap years from {current_year}to{final_year}")
    for year in range (current_year,final_year+1):
        if (year % 4==0 and year % 100!=0) or (year % 400==0):
            print(year)
