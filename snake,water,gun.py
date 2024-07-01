computer = 0 
user = 0
user_dict ={1:"Snake" , 2:"Water" , 3:"Gun"}
comp_dict ={1:"Snake" , 2:"Water" , 3:"Gun"}
def Game():
  global user , computer
  import random
  comp_choice=random.choice([1,2,3])
  user_choice=int(input("Enter your choice \n 1 for snake \n 2 for water \n 3 for gun \n 4 for exit \n"))
  if(user_choice==4):
      print("Thank you for playing the game")
      exit()
  else:
      print(f"you chose {user_dict[user_choice]} and computer chose {comp_dict[comp_choice]} ")
  if(user_choice==comp_choice):
      print("Game tie , play it again")
  elif(user_choice==1 and comp_choice==2):
      print("You win...!")
      user+=1
  elif(user_choice==1 and comp_choice==3):
      print("You lose , better luck next time ")
      computer+=1
  elif(user_choice==2 and comp_choice==1):
      print("You lose , better luck next time")
      computer+=1
  elif(user_choice==2 and comp_choice==3):
      print("You win...!")
      user+=1
  elif(user_choice==3 and comp_choice==1):
      print("You win...!")
      user+=1
  elif(user_choice==3 and comp_choice==2):
      print("you lose , play it again")
      computer+=1
  else:
      print("Invalid choice , play again")
print("Welcome to the game \n Select your choice ")
Game()
print(f"\n Your score board of game \n user scored = {user} \n computer scored = {computer}")