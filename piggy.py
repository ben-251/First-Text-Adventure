def main():
	class character:
		def __init__ (self,name,health):
			self.name = name
			self.health = health
		
		#getters(i know we dont use them in school so not sure why they're there)
		def get_name (self):
			return self.name
		def get_health(self):
			return self.health

		#setters
		def set_name (self,new):
			self.name = new	
		def set_health (self,new):
			self.health = new
		
	class piggy(character):
		def __init__ (self,name,health,inventory,job,active):
			super().__init__(name,health)
			self.inventory = inventory
			self.job = job
			self.active = False


	class bigbad(character):
		def __init__ (self,name,health,power):
			super().__init__(name,health)
			self.power = power


	###########/////CHARACTER CREATION AND OTHER GLOBAL STUFF//////#############


	import spaces as sp
	active_character = ""
	helgie = piggy("Helgie",5,["Hay","Rope","e"],"farmer",False)
	marcie = piggy("Marcie",6,["Sticks","Rope"],"stick builder",False)
	ettie =  piggy ("Ettie",4,["Bricks","Cement","Paint"],"builder",False)

	Wolf = bigbad("Grant",15,14)

	##gonna add code so that only one pig can be true and the others must be false, so 
	def character_choice():
		choice = ""
		choice = input("Welcome to the easter egg piggy program\nChoose a player: Ettie, Marcie, or Helgie: ").lower()
		#iv
		while choice != "helgie" and choice != "marcie" and choice != "ettie":
			print("sorry, invalid input. choose out of the three little piggies please:")
			choice = input("Who are you going for? ").lower()

		if choice == "helgie":
			active_character = helgie
			helgie.active = True
		elif choice == "marcie":
			active_character = marcie
			helgie.active = True
		elif choice == "ettie":
			active_character = ettie
			ettie.active = True
		return active_character
		#set character	
		
	active_character = character_choice()


	print(f"Hello {active_character.name}!")
	print("you currently have: ")
	sp.single(active_character.inventory)
	print(f"and you are a {active_character.job}")
