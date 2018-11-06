from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
food_types=Trie()
for food in types:
  food_types.insert(food)

#Write code to insert restaurant data into a data structure here. The data is in data.py

restaurant_types=HashMap(20)
for listr in restaurant_data:
  key=listr[0]
  list_type=restaurant_types.retrieve(key)
  if not list_type:
    restaurant_same_type=LinkedList(listr)
    restaurant_types.assign(key,restaurant_same_type)
  else:
    list_type.insert_beginning(listr)
    restaurant_types.assign(key,list_type)


#Write code for user interaction here
while True:
  more_than_one_choice= True
  while more_than_one_choice:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    #Search for user_input in food types data structure here
    list_rest=[]
    list_children=food_types.get_children()
    word=""
    found=True
    for ind_char,char in enumerate(user_input):
        key=food_types.convert_key(char)
        if not list_children[key]:
          found = False
          break
        else:
          word+=str(char)
          if ind_char!=len(user_input)-1:
                      list_children=list_children[key].get_children()
    if found:
      if not list_children:
        if word:
          list_rest.append(word)
        else:
          found=False
      else:
        trie_to_follow=list_children[key]
        trie_to_follow.traverse(word,list_rest)



    if not found:
      print("\n Sorry, there is no type of restaurant starting with {0} . Try again.\n".format(user_input))
    else:
      if len(list_rest)==1:
        more_than_one_choice= False
      else:
        print("The choices that you have with these beginning letters are: ")
        for rest in list_rest:
          rest=rest[0].upper()+rest[1:]
          print("\t {0}".format(rest))

    #After finding food type write code for retrieving restaurant data here
  rest=list_rest[0]
  rest=rest[0].upper()+rest[1:]
  user_input=str(input("\n The only option with those beginning letters is "+rest+". Do you want to look at "+rest+" restaurants?  Enter 'y' for yes 'n' for no.  \n"))
  if user_input=='y':
      key=list_rest[0]
      rest_addresses=restaurant_types.retrieve(key)
      current_node=rest_addresses.get_head_node()
      print("\n The {0} Restaurants in Soho are: ".format(rest[0].upper()+rest[1:]))
      print(" __________________________________\n")
      while current_node:
          address=current_node.get_value()
          print("\tName: {0}".format(address[1]))
          price=""
          for i in range(0,int(address[2])):
            price+='$'
          print("\tPrice: {0} ".format(price))
          print("\tRating:{0}/5".format(address[3]))
          print("\tAddress:{0}".format(address[4]))
          print("\n\t ------------------\n")
          current_node=current_node.get_next_node()
  user_input=str(input(" \n Do you want to find another restaurant? Enter 'y' for yes 'n' for no. \n \n"))
  if user_input=='n':
          break
  
