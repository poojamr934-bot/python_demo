name= input("enter your name:")
age= int(input("enter your age:"))
#lower() function will convert the input to lowercase , strip() function will remove any leading or trailing whitespace from the input
citizenship=input("are you a citizen of india..?(yes/no): ").strip().lower()
if(age>=18 and citizenship=="yes"):
    
    print(name,"congratulations! you are eligible to vote")
else:
    print(name, "sorry you are not eligible to vote")