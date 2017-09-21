Name= input("May I know Your Name Sire \n")
print("Welcome Mr",Name)
Age= int(input("What is your age???"))

if Age>=21:
    print(Name,"You are allowed in the Club")
    print("What drink do u want???")
elif Age>=18:
    print("You are allowed in Club but u cant have drinks",end='\n''\n')

else:
    print(Name,"Unfortuntely You are not allowed  in the Club")