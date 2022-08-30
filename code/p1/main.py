reavers=float(input("how many reavers:"))
number=reavers
if number < 3:
    print("Not enough crew")
y=reavers*3
units=float(input("how many units:"))
numbers=units
if numbers < 0:
    print("Enter only positive integers for reavers and units.")
if number >= y:
    print("Not enough units.")
reaver=reavers-2
dock=3*reaver
unit=units-dock
yondu=int(unit*(13/100)) 
peter=int((unit-yondu)*11/100)
remaining=(unit)-(yondu)-(peter)
x=remaining/reavers
crew=int(x)
RBF=int(remaining-(crew*reavers))
print("Yondu's share:",yondu+crew)
print("Peter's share:",peter+crew)
print("crew:",crew)
print("RBF:",RBF)
