import spaces
import piggy
import time 

inventory = ["fish"]
######///-stage1 complete. -///#####
def start1():
	print("Welcome young adventurer!\n Enter 'help' at anytime to see keywords")

def help(stage):
	print("This is the help menu. Enter 'exit' or 'ʇıxǝ' to leave.\n")
	#stage1
	keywords1 = ["start","help","see inventory"]
	meanings1 = ["Takes you to the start of the checkpoint.", "Gives you the key words and what they mean.","see stored items"]
	#stage2
	keywords2 = ["start","help","jump","walk","see inventory"]
	meanings2 = ["Takes you to the start of the checkpoint.", "Gives you the key words and what they mean.","lets you jump","you walk","see stored items"]
	#stage2.1
	keywords21 = ["start","help","pick it up","keep going","see inventory"]
	meanings21 = ["Takes you to the start of the checkpoint.", "Gives you the key words and what they mean.","pick up the stick","walk on without it","see stored items"]
	#stage 3
	keywords3 = allowed_answers = ["jump","walk","help","start","see inventory"]
	meanings3 = ["lets you jump","you walk further","Takes you to the start of the checkpoint.", "See stored items"]
	if stage ==1:
		spaces.display(keywords1,meanings1)
	elif stage ==2:
		spaces.display(keywords2,meanings2)
	elif stage ==2.1:
		spaces.display(keywords21,meanings21)
	exit = ""
	exit = input()
	while exit != "exit" and exit!= "ʇıxǝ":
		exit = input()

def see_inventory():
	print("you have:")
	if len(inventory)==0:
		print("nothing")
	else:
		spaces.single(inventory)
	
	#exit = ""
	#exit = input()
	#while exit != "exit" and exit!= "ʇıxǝ":
	#	exit = input()

def new_name():
	start1()
	name = ""
	name = name_input()
	return name
		

def name_input():
	name = ""
	name = input("Choose a name, young adventurer:\n")
	#check if they restart
	accepted_input = ["help","start","see inventory","piggy"]
	while name in accepted_input:
		if name =="help":#calls the function. need to make it check if help was just run
			help(stage)
			name = name_input()
		elif name == "start":
			name = new_name()
		elif name == "see inventory":
			see_inventory()
			name = name_input()
		elif name == "piggy":
			piggy.main()
	return name

def check(choice):
	if choice  == "help":
		print(stage)
		help(stage)
		choice = input()
	elif choice == "see inventory":
		see_inventory()
		choice = name_input()	
def stage1 ():
	#in this stage, the user chooses a name and will get called this name for the whole game. They also have a chance to ask for help
	global stage
	global name
	stage =1
	start1()
	global name
	name = ""
	name = name_input()
	print("hi there "+name)

#####////~Stage 2~////#####
def start2():
	print("You are in an open field, with the sun high above your head, and the wind blowing the grass around you.")
	time.sleep(1)

def question():
	ans = ""
	ans = input("what do you do next?: ").lower()
	return ans

def new():
	start2()
	choice = ""
	choice = explore()
	return choice
def explore():
	stage = 2
	choice = question()
	while choice != "walk":
		if choice  == "help":
			print(stage)
			help(stage)
			explore()
		elif choice == "start":
			choice = new()
		elif choice == "see inventory":
			see_inventory()
			choice = question()
		elif choice == "jump":
			time.sleep(1)
			print("You jump and land exactly where you started")
			choice = question()
		else: 
			print("sorry, i didn;t quite get that, try again:")
			choice = question()
	stage = 2.1
	print("\nYou walk gently along the field, and you start to notice but quickly ignore the suns intense heat,")
	time.sleep(1)
	def stick():
		print("you discover a strange green glowing stick. Do you pick it up or keep going?")
		stick_choice = ""
		stick_choice = input("")
		allowed_answers = ["keep going","pick it up","help","start","see inventory"]
		while stick_choice not in allowed_answers: 
			print("sorry, didnt quite get that, try again")
			stick_choice = input()
		return stick_choice

	stick_choice = ""
	stick_choice = stick()

	#if stick_choice == "keep going":
	#	print("you walk and then an ogre asks for the stick and you dont have it so you d#ie. game over.\n")
	#	time.sleep(1)
	#	stage =1
	#	main()

	if stick_choice == "pick it up":
		inventory.append("stick")
		
	elif stick_choice == "see inventory":
		see_inventory()
		stick_choice=stick()

	elif stick_choice == "help":
		print(stage)
		help(stage)
		stick_choice = stick()

	elif stick_choice == "start":
		explore()
	print("In the Cave you see a strang shadow. Ogre Fred. He asks you if you have a green stick. You scramble in your pockets.")

	if "stick" in inventory:
		time.sleep(5)
		print("you do.")
		time.sleep(2)
		stage3()
	else:
		time.sleep(2.5)
		print("as you scramble around in your pockets the ogre gets impatient, calls for a chicken which bursts through the ceiling with bow in hand, drawn. You are taken captive for eternity. Game over.")
		time.sleep(4)
		main()
	#need to add those extra choices like inventory and start and help, and need to add inventory to help

def stage2 ():
	global stage
	stage =2
	start2()
	explore()


#####////--- STAGE THREE ---/////#####
def intro3():
	stage = 3
	next = ""
	print("Ogre Fred lets you by and you enter a gloomy cave. You bravely walk in through its dark tunnels, walking past lowly lit torches and spiderwebs.")
	next = input("you hear a faint sound in the distance and start to approach it,")
	next = input("An elf.")
	next = input(name+"!")
	print('"how do you know my name?", you ask')
	next = input()
	print("everyone knows you here. I'm Maia, a messenger elf or some random mystical thing idk we've heard tales of a young adventurer like you, with the jade stick of kwiatra. You must save us from.. blah blah blah")
	next = input()

def action3():
	print("'what do you do now?''")
	allowed_answers = ["jump","walk","help","start","see inventory"]
	choice= input("").lower()
	while choice not in allowed_answers:
		print("try again:")
		action = input("")
	while choice != "walk":
		if choice  == "help":
			print(stage)
			help(stage)
			action3()
		elif choice == "start":
			choice = intro3()
		elif choice == "see inventory":
			see_inventory()
			action3()
		elif choice == "jump":
			time.sleep(1)
			print("You jump and hit your head on the rocks above you.")
			#reduce health by one
			choice = question()
		else: 
			print("sorry, i didn;t quite get that, try again:")
			choice = question()

#/////AIM/////: Gonna ADD A THING TO GET RID OF AN ITEM IN THE INVENTORY AT THE COST OF HUNGER, BUT SAVES FROM HUNGER DEATH	

def stage3():
	stage = 3
	intro3()
	action3()
def main():
	stage1()
	stage2()
main()
