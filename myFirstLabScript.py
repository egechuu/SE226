#1
name = input("What is your name?")
print("Hello " + name)
id = input("What is your Student ID?")
print("Your ID is " +id)
#2
var1 = input("Enter first variable.")
var2 = input("Enter first variable.")
sum = int(var1) + int(var2)
diff = abs(int(var1)-int(var2))
prod = int(var1) * int(var2)
print("Sum: " + str(sum))
print("Difference: " + str(diff))
print("Product: " + str(prod))
#3
name1 = input("What is your full name?")
lab = input("What is your lab grade?")
midterm = input("What is your midterm grade?")
final = input("What is your final grade?")
lastScore = int(lab)*0.25 + int(midterm)*0.35 + int(final)*0.4
print("Name: " + name1 + "\n"
      "Lab: " + str(lab) + "\n" 
      "Midterm: " + str(midterm) + "\n"
      "Final: " + str(final) + "\n"
      "Last Score: " + str(lastScore) + "\n"
      )
#4
print("*\n**\n***\n**\n*")


        