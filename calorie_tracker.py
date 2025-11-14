# Name-Rohan Kumar Singh
# Date-7/10/2025
# Title-Daily calorie tracker 

print("welcome everyone this is the calorie tracker console app which is used to keep a track of your daily intakes")

meals= []
calories=[]
n=int(input("how many meals do you want to enter?"))
for i in range (n):
    meal_name=str(input("enter meals"))
    calorie_amount=float(input("enter calorie for the same"))
    meals.append(meal_name)
    calories.append(calorie_amount)
    print("enter meals="+str(meals))
    print("calories per meal="+str(calories))
    
def Tcalories():
    total_calories=0
    for cal in calories:
        total_calories +=cal
        average= total_calories / len(calories)
    print("average calorie per meal=" , average) 
    print("total calories=", total_calories)
    return total_calories,average
    
total,average=Tcalories()

limit_calories=float(input("enter limit calories"))
if(total>limit_calories):
    print("congo you are under your daily maintainence calories")
else:
    print("carefull! you are exceeding your daily maintainence calories")
    
    
print("\nMeal Name              Calories")
print("---------------------------------")
for meal,cal in zip(meals,calories):
 print(f"{meal:<20}{cal}")
 
print("---------------------------")
print(f"{'total:':<20}{total}")
print(f"{'average:':<20}{average:.2f}")