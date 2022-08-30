adults=1
babies=0 #define the babies
months=1 #define the adults
cages=500 #define amount of cages
total=adults+babies
print("Month, Adults, Babies, Total") #title in cvs format
while total <= 500: #while statement for the loop that portrays the total bunnies won't go over cage amount
    print(int(months), int(adults), int(babies), int(total))#month,adults, babies, total is shown
    temp_adults=adults
    months=months+1 #raise in months for each loop
    adults=adults+babies #after one month old the babies are placed as adults
    babies=temp_adults
    total=adults+babies #adding up total bunnies and assigning to variable
print(int(months), int(adults), int(babies), int(total))
