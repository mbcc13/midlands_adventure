import time

## player answers
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]
yes = ["Y", "y", 'yes']
no = ["n", "N", "no"]
wrong_answer = ("Please use A, B, or C")
##Items
sword = 0



def intro():
  print("You awake in the middle of the night in a field "
  "A Werewolf is staring at you growling, it looks hungry ")
  print ("Will you: ")
  time.sleep(1)
  print("""  A. Run into the woods behind you
  B. Throw your empty glass
  C. pray to the Old Gods and the new that your eath doesn't hurt too bad""")
  choice = input("---> ")
  if choice in answer_a:
      woods()

def woods():
    print("You run into the woods, but you hear the Werewolf right behind you")
    time.sleep(2)
    print("You are running as fast as you can when you trip on something")
    time.sleep(1)
    print("A handle is sticking out of the ground! \nDo you pull on it? Y/N")
    choice = input("--->")
    time.sleep(1)
    if choice in yes:
        print("It is a sword!")
        print("You steady yourself as the werewolf comes closer!")
        time.sleep(2)
        print("The werewolf pounces at you!")
        time.sleep(1)
        print("You drive the sword into its chest! \nyou are safe!")
    elif choice in no:
        print("The beast catches you, with no weapon you are easily torn apart")

    else:
        print("It is a simple yes or no question")
        woods()


intro()