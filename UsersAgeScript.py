from AgeCalculator import ageCalc
from AgeCalcMsg import ageMsg
userDicc = {}
nUsers = int(input("Enter the number of users: "))
for i in range(0,nUsers):
    name = input("Enter the name of the user:" )
    age = input("Enter the age of the user:" )
    userDicc[name]=age

print("")

for nameUser, ageUser in userDicc.items():
    print("User %s  Age %s Years" % (nameUser, ageUser))
    ageCalc(int(ageUser))
    ageMsg(int(ageUser))