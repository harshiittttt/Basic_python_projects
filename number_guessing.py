import random
print("Welcome to our nuber guessing game")



randomnumber = random.randint(10,99)
userinput = 0
def takeuserinput():
    userinput = int(input("PLEASE ENTER YOUR GUESSED NUMBER"))  
    return userinput
    
    

while userinput != randomnumber:
      userinput = takeuserinput()
      if userinput>randomnumber :
          print("please go left")
          
      elif userinput<randomnumber:
          print("please go right")
          
      else:
          print("whoaa !! you have entered the correct number")
          
          



    
          
          
   