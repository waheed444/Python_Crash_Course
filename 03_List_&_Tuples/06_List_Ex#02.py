
# WAP to ask the user to enter names of their 3 favorite games & store them in a list.

games=[]     # make emty list to add the items by user's choice
game1=input("Enter 1st game you like here  :")
game2=input("Enter 2nd game you like here  :")
game3=input("Enter 3rd game you like here  :")

games.append(game1)
games.append(game2)
games.append(game3)

print(games) 
print(type(games))

