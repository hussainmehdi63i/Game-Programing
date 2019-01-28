import random
import time


input("Whats your name?")
print("You wake in an unusual area")
print("Where are You")
time.sleep(5)
print("You see two roads giong oposite to each other")
time.sleep(3)

chosenPath = input("Which will you choose Right or Left:")

print("You head down the Way")
time.sleep(2)
print("You dont Know where you are the area deosnt seem to be fimiliar at all...")
time.sleep(2)
print("Its Dark your scared and then you see")
print()
time.sleep(3)

if chosenPath == "left":
        print("You see a big house....")
        time.sleep(3)
        print("Wait that house seem really fimiliar it just like your house")
else:
    print("A huge wolf running towards you...")
    time.sleep(3)
    print("You are scared you start as fast as you can...")
    time.sleep(3)
    print("While running you spot a huge house")

print("You run towards the house and open the door")
time.sleep(4)
print("The door is jammed")
time.sleep(3)

kickdoor = input ("What do you want to do:")
time.sleep(3)

if kickdoor == "kick":
    print("You see a huge a room filled with furniture.You have a nostalgic feeling as the furniture is set the same way like your house. ")
    time.sleep(3)
else:
     kickdoor1 = input("kick the door:")
     print("You see a huge a room filled with furniture.You have a nostalgic feeling as the furniture is set the same way like your house. ")
     time.sleep(3)


print("You look through the room but find nothing. Except a drawer infront of you ")
input("You open the Drawer:")
time.sleep(4)
print("You find a Device, You look through it and there is a Voice memo init")

letter = input("What do you want to do with the Voice memo.Do you want to listen to it:")

if letter == "yes":
    print("To whom who is listning to this message.They came of out of no where we are being chased by them. Within the darkness they came and took everyone away.Whoever you are run and be carefull. Dont go towards the voices in the forest avoid them.They are coming warn everyone ")
    time.sleep(3)
    print("OH it coming, NOOOOOOOOOO!!!")
    time.sleep(4)
    print("...........")
    time.sleep(3)
    print("You are scared by that message.Confused and scared you look through your pocket for something to defemd yourself")
    pocket = input("Search Pocket:")
    time.sleep(3)
    print("You find")
    pocketlist = ["Gum","Lighter","Picture,"]
    print(pocketlist)
    time.sleep(3)
    print("There is nothing worth using in your pocket")
else:
    print("You accidently press the wrong button and the message got deleted")
    print("You wont be able to lsiten to the message again")
    time.sleep(2)
    print("Your are worried about the meassage as might have contained improtant meassge")
    time.sleep(3)

print("You find nothing interesting in the house and go out to search for more clues.")
time.sleep(3)
print("You keep giong straight towards the path. Not knowing where to go or what to do exactly")
time.sleep(2)
print("You start to hear some voices coming from away......")
time.sleep(2)

sound = input("Do you had towards the voice, Yes or no:")
time.sleep(3)

if sound == "yes":
    print("You walk towards the sound and approach the UNKOWNS...")
    print("It chases after you, You cant run it catching up to you and......")
    time.sleep(3)
    print("It catches up to you and destroyes you to pieces")
    time.sleep(3)
    print("GAME OVER")
    time.sleep(3)
    exit()
else:
    print("You avoid the noise and go towards the path you were walking.You keep walking straight hoping to find somehting to find out,How you got here and what to do to get out.")
    print("Walking through that for hours, you feel like somehthin is following you and you stop.......")
    time.sleep(3)

print("Youn see a wolf runing towards you, youn have no where to run but you spot two weaopns you can use a rock and a pointy tree trunk")
weapons = input("Which do you want to use rock or tree:")
time.sleep(3)

if weapons == "tree":
    print("The wolf comes running toward you pick the tree and stick out it jumps towards.......")
    time.sleep(4)
    print(".......")
    time.sleep(3)
    print("You open you eyes and the wolf is above you not moving and the tree trunk is inside its belly blood coming from its stomach all over you.")

else:
    print("The wolf comes running towards you, you pick the rock and throw it as hard as you can. It hits the wolf...... ")
    time.sleep(4)
    print("The rock hit the wolf but it has no effect, the wolf came running down and snatches your neck away and you DIE")
    time.sleep(3)
    print("GAME OVER")
    time.sleep(3)
    exit()

print("You remove the wolf from you and started to run scared from what jst happened you keep running your breath giong away, not knowing what to to do")
print("You see a bright light while running, You run towards in hope that you found someone living there")
time.sleep(3)
input("enter to run faster:")
input("enter to run faster:")
input("enter to run faster:")
input("enter to run faster:")
input("enter to run faster:")
input("enter to run faster:")
print("you run as fast as you can towards the bright light, As soon as you reach the light you see that")
time.sleep(3)
print("The light is like bulb and you touch it suddenly........")
time.sleep(3)
print("YOU GET TAKEN AWAY in the light")
print("......")
time.sleep(2)
print("You hear a voice inside the light.saying your name")

name = input("Do you go towards the Voice:")
time.sleep(3)

if name == "yes":
    print("You go towards the voice")
    print("You get closer")
    time.sleep(2)
    print("closer")
    time.sleep(2)
    print("closer and then")
    time.sleep(4)
    print("You suddenly wake up in your house and your mom shouting your name to wake you")
    time.sleep(3)
    print("You realise it was all a dream, You are reliefed after seeing you house...")
    print("TEARS start coming out of you eyes")
    time.sleep(3)
    print("You shout I AM HOME")
    time.sleep(4)

else:
    print("You avoid the voice and keep heading straight....")
    time.sleep(3)
    print("Sudedenly you start hearing voices saying you can never leave this place and you feel the floor moving under you and make huge hole and you drop init.......")
    time.sleep(2)
    print("........")
    time.sleep(2)
    print("YOU WAKE UP in the same place you started from you start running towards the light but you just keep coming back to same place")
    time.sleep(4)
    print("AFTER about 10 tryes you relise you stuck in this mysterious place forever")
    time.sleep(4)
    print ("GAME OVER")
    time.sleep(4)
