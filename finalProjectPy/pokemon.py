import random
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
window = tk.Tk()
window.geometry("750x500")
window.title("pokedax")
image_references = {}
cutscene = tk.Frame(window)
cutscene.pack()
arena = tk.Frame(window)
characterSelectionScreen = tk.Frame(window)        


def displayStats(CharacterSelectionChoice):
        global playerChoice
        playerChoice = CharacterSelectionChoice
        processPlayerChoice()
        

def processPlayerChoice():
    global characterChoice
    if playerChoice == 1:
            Heavy = character(name="Heavy", hp=170, agility=70, dmgOtTurnsLeft=0, healthBeingIncreasedRn=0,
                              healthCheck=False, healthTurnleft=0,
                              attakList=[["burst", 30, 5], ["rapid fire", 40, 0]], 
                              defenList=[["sandwich", 0, 15], ["close medic support!", 50, 0]], 
                              pokemonAttackChnc=0, dmgOtbeingInflictedRn=0, pokemonDefenseChnc=0, dmgOtCheck=False)
            characterChoiceName = "Heavy"
            characterChoice = Heavy
            Heavy.intro(characterChoiceName = characterChoiceName)
    elif playerChoice == 2:
            Scout = character(name="Scout", hp=120, agility=100, dmgOtTurnsLeft=0, healthBeingIncreasedRn=0,
                              healthCheck=False, healthTurnleft=0,
                              attakList=[["double Barrel", 40, 0], ["Pincer Menuever", 0, 20], ["Uppercut", 15, 15]], 
                              defenList=[["sandwich", 0, 15]], pokemonAttackChnc=0, dmgOtbeingInflictedRn=0, pokemonDefenseChnc=0, dmgOtCheck=False)
            characterChoiceName = "Scout"
            characterChoice = Scout
            Scout.intro(characterChoiceName = characterChoiceName)
    
global playerChoice
playerChoice = 1


def show_third_cutscene():
        backgroundCutScene2.grid_forget()

        backgroundCutScene3.grid(row=1, column=1)

def show_second_cutscene():
        backgroundCutScene1.grid_forget()
        
        backgroundCutScene2.grid(row=1, column=1)
def show_fourth_cutscene():
        backgroundCutScene3.grid_forget()

        backgroundCutScene4.grid(row=1, column= 1)

def show_character_selection():
        backgroundCutScene4.grid_forget()
        cutscene.pack_forget()
        characterSelectionScreen.pack()
        window.geometry("750x850")
        DisplayCharacter1.grid(row=1, column=0)
        DisplayCharacter2.grid(row=1, column=1)
        DisplayCharacter3.grid(row=1, column= 2)
        DisplayCharacter4.grid(row=1, column = 3)
        DisplayCharacter5.grid(row=3, column=0)
        DisplayCharacter6.grid(row=3, column=1)
        DisplayCharacter7.grid(row=3, column= 2)
        DisplayCharacter8.grid(row=3, column = 3)

        button1 = tk.Button(characterSelectionScreen, text='Heavy', width=10, command=lambda: displayStats(1))
        button1.grid(row=2, column=0, padx= 5)
        button2 = tk.Button(characterSelectionScreen, text='Scout', width=10, command=lambda: displayStats(2))
        button2.grid(row=2, column=1, padx= 5)
        button3 = tk.Button(characterSelectionScreen, text='Doc',width=10, command=lambda: displayStats(3))
        button3.grid(row=2, column=2, padx= 5)
        button4 = tk.Button(characterSelectionScreen, text='Spy', width=10, command=lambda: displayStats(4))
        button4.grid(row=2, column=3, padx= 5)
    

        button5 = tk.Button(characterSelectionScreen, text='Pyro', width=10, command=lambda: displayStats(5))
        button5.grid(row=4, column=0, padx= 5)
        button6 = tk.Button(characterSelectionScreen, text='Demo', width=10, command=lambda: displayStats(6))
        button6.grid(row=4, column=1, padx= 5)
        button7 = tk.Button(characterSelectionScreen, text='Engy', width=10, command=lambda: displayStats(7))
        button7.grid(row=4, column=2, padx= 5)
        button8 = tk.Button(characterSelectionScreen, text='Sniper', width=10, command=lambda: displayStats(8))
        button8.grid(row=4, column=3, padx= 5)
        

image_references['cutscene1'] = ImageTk.PhotoImage(Image.open('cutscenes/9.png').resize((750, 500)).convert("RGBA"))
backgroundCutScene1 = tk.Label(cutscene, image=image_references['cutscene1'], background="black")
backgroundCutScene1.grid(row=1, column=1)

image_references['cutscene2'] = ImageTk.PhotoImage(Image.open('cutscenes/10.png').resize((750, 500)).convert('RGBA'))
backgroundCutScene2 = tk.Label(cutscene, image=image_references['cutscene2'], background="black")

image_references['cutscene3'] = ImageTk.PhotoImage(Image.open('cutscenes/11.png').resize((750, 500)).convert('RGBA'))
backgroundCutScene3 = tk.Label(cutscene, image=image_references['cutscene3'], background="black")

image_references['cutscene4'] = ImageTk.PhotoImage(Image.open('cutscenes/12.png').resize((750, 500)).convert('RGBA'))
backgroundCutScene4 = tk.Label(cutscene, image=image_references['cutscene4'], background="black")

    # Load and display images for character selection
image_references['Heavy'] = ImageTk.PhotoImage(Image.open('charactershowcase/Heavy.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter1 = tk.Label(characterSelectionScreen,image=image_references['Heavy'])

image_references['Scout'] = ImageTk.PhotoImage(Image.open('charactershowcase/scout.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter2 = tk.Label(characterSelectionScreen,image=image_references['Scout'])

image_references['Doc'] = ImageTk.PhotoImage(Image.open('charactershowcase/doc.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter3 = tk.Label(characterSelectionScreen, image=image_references['Doc'])

image_references['Spy'] = ImageTk.PhotoImage(Image.open('charactershowcase/spy.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter4 = tk.Label(characterSelectionScreen, image=image_references['Spy'])

image_references['Pyro'] = ImageTk.PhotoImage(Image.open('charactershowcase/pyro.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter5 = tk.Label(characterSelectionScreen, image=image_references['Pyro'])

image_references['Demo'] = ImageTk.PhotoImage(Image.open('charactershowcase/demo.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter6 = tk.Label(characterSelectionScreen,image=image_references['Demo'])

image_references['Engy'] = ImageTk.PhotoImage(Image.open('charactershowcase/engy.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter7 = tk.Label(characterSelectionScreen, image=image_references['Engy'])

image_references['Sniper'] = ImageTk.PhotoImage(Image.open('charactershowcase/Sniper.png').resize((175, 250)).convert('RGBA'))
DisplayCharacter8 = tk.Label(characterSelectionScreen, image=image_references['Sniper'])


window.after(000, show_second_cutscene)
window.after(000, show_third_cutscene)
window.after(000, show_fourth_cutscene)
window.after(000, show_character_selection)
    
def showCharacterOnPanel(character_name):
    panel2_reference =  ImageTk.PhotoImage(Image.open(f'arena/panel2{character_name}.png').resize((175, 250)).convert('RGBA'))
    panel2_Show = tk.Label(arena, image = panel2_reference)
    panel2_Show.image = panel2_reference
    panel2_Show.grid(column =1, row= 1, padx= 0, pady= 0 )
def showPokemonOnPanel(poke_name):
    panel4_reference = ImageTk.PhotoImage(Image.open(f'arena/panel4{poke_name}.png').resize(175, 250).convert("RGBA"))
    panel4_show = tk.Label(arena, image= panel4_reference)
    panel4_show.image = panel4_reference
    panel4_show.grid(column =4, row= 1, padx= 0, pady= 0 )     

def BattleArena(self, characterChoiceName):

    characterSelectionScreen.pack_forget()  
    arena.pack() 
    window.geometry("875x500")

    # Panels Setup
    panel_array = ['arena/panel1.png', 'arena/panel2Empty.png', 'arena/panel3NoEffect.png', 'arena/panel4Empty.png', 'arena/panel5.png']
    for i in range(len(panel_array)):
        panel_Reference = ImageTk.PhotoImage(Image.open(f'{panel_array[i]}').resize((175, 250)).convert('RGBA'))
        panel_Show = tk.Label(arena, image=panel_Reference)
        panel_Show.image = panel_Reference
        panel_Show.grid(column=i, row=1, padx=0, pady=0)

    if characterChoiceName == "Heavy":
        charmander1 = character(
            name="Charmander", hp=120, agility=70, healthBeingIncreasedRn=0, healthCheck=False, healthTurnleft=0,
            attakList=[["scratch", 30, 0], ["ember", 15, 5], ["flamethrower", 0, 15]], 
            defenList=[["invigur!", 25, 0]], pokemonAttackChnc=60, dmgOtbeingInflictedRn=0, pokemonDefenseChnc=40, dmgOtCheck=False, dmgOtTurnsLeft=0
        )

        squirtle2 = character(
            name="Squirtle", hp=140, agility=35, healthBeingIncreasedRn=0, healthCheck=False, healthTurnleft=0,
            attakList=[["water Gun", 60, 0], ["Hydro pump", 35, 15]], 
            defenList=[["invigur!", 25, 0]], pokemonAttackChnc=75, dmgOtbeingInflictedRn=0, pokemonDefenseChnc=25, dmgOtCheck=False, dmgOtTurnsLeft=0
        )

        bulbasaur3 = character(
            name="Bulbasaur", hp=260, agility=10, healthBeingIncreasedRn=0, healthCheck=False, healthTurnleft=0,
            attakList=[["Earthquake", 90, 0]], 
            defenList=[["invigur!", 0, 10]], pokemonAttackChnc=80, dmgOtbeingInflictedRn=0, pokemonDefenseChnc=20, dmgOtCheck=False, dmgOtTurnsLeft=0
        )
        global pokemonRoster
        roster_options = [
            [charmander1, squirtle2, bulbasaur3],
            [charmander1, bulbasaur3, squirtle2],
            [squirtle2, charmander1, bulbasaur3],
            [squirtle2, bulbasaur3, charmander1],
            [bulbasaur3, charmander1, squirtle2],
            [bulbasaur3, squirtle2, charmander1]
        ]
        pokemonRoster = random.choice(roster_options)
        pokemonCount = 0
        window.after(0, showCharacterOnPanel(character_name="Heavy"))
        if pokemonRoster[pokemonCount].name == "Squirtle": 
            window.after(0, showPokemonOnPanel(character_name="Squirtle"))
        if pokemonRoster[pokemonCount].name == "Charmander": 
            window.after(0, showPokemonOnPanel(character_name="Charmander"))
        if pokemonRoster[pokemonCount].name == "Bulbasaur": 
            window.after(0, showPokemonOnPanel(character_name="Bulbasaur"))
        
        # Create action menu window as a Toplevel
        arenaChoiceOptions = tk.Toplevel(window)
        arenaChoiceOptions.title("Action Menu")
        arenaChoiceOptions.geometry("700x200")
        arenaActionMenu = tk.Frame(arenaChoiceOptions)
        arenaActionMenu.pack()

        # Pokémon Initialization (should be defined once)
    

        # Pokémon roster randomizer
        
        global turn
        turn = 1
        # Round Label
        
        def player_turn():
            RoundLabel = tk.Label(arena, text=f"Round: {turn}", font="Arial")
            RoundLabel.grid(row=2, column=2)
            # DMG/Health Over Time Checks
            if characterChoice.dmgOtCheck:
                characterChoice.dmgOtAction()
            if characterChoice.healthCheck:
                characterChoice.defenseOtAction()
            
            if characterChoice.hp < 1:
                messagebox.showwarning("Player has died", "Thank you for playing")
                return
            
            # Display attacks and defenses
            healthDisplayText = tk.Label(arenaActionMenu, text=f"Health: {characterChoice.hp}", font="Arial")
            healthDisplayText.grid(row=6, column=0)
            
            # Display attack options
            for i, attack in enumerate(characterChoice.attakList):
                tk.Label(arenaActionMenu, text=f"{i+1}. Attack: {attack[0]} | Instant damage: {attack[1]} | DoT: {attack[2]}").grid(row=7+i, column=1)
                attackChoiceButton = tk.Button(arenaActionMenu, text='Attack', width=10, command=lambda a=attack: playerAfterClick("attack", a))
                attackChoiceButton.grid(row=7+i, column=4)

            # Display defense options
            for l, defense in enumerate(characterChoice.defenList):
                tk.Label(arenaActionMenu, text=f"{l+1}. Defense: {defense[0]} | Value: {defense[1]} | Heal: {defense[2]}").grid(row=len(characterChoice.attakList)+9+l, column=1)
                defendChoiceButton = tk.Button(arenaActionMenu, text='Defend', width=10, command=lambda d=defense: playerAfterClick("defense", d)) #????
                defendChoiceButton.grid(row=len(characterChoice.attakList)+9+l, column=4)
        player_turn()
        def playerAfterClick(action_type, action_choice):
            for widget in arenaActionMenu.winfo_children():
                widget.grid_forget()
            if action_type == "defense":
                characterChoice.defense(action_choice[0], action_choice[1], action_choice[2], defenseCount=2)
            elif action_type == "attack":
                characterChoice.attack(pokemonRoster[pokemonCount], action_choice[0], action_choice[1], action_choice[2], dmgOtCount=3) 
            poke_turn()


        def poke_turn():
            global turn
            nonlocal pokemonCount
            if characterChoiceName.hp > 100:
                PlayerVitals_reference = tk.PhotoImage(image = f"player/green{characterChoiceName}")
            #CHECKPOINT
                playerVitalShow = tk.Label(arena, image= PlayerVitals_reference)
                playerVitalShow.grid(row=3, column=1)
            try:
                # Pokémon turn checks
                global current_pokemon
                current_pokemon = pokemonRoster[pokemonCount]
                if current_pokemon.dmgOtCheck:
                    current_pokemon.dmgOtAction()
                if current_pokemon.healthCheck:
                    current_pokemon.defenseOtAction()

                if current_pokemon.hp < 1:
                    messagebox.showinfo(title= "Poke Died", message = f"""{current_pokemon.name} has perished, next Pokémon is being chosen!
                                        {current_pokemon.name} has perished, next Pokémon is being chosen!
                                        Care package: +100 health for {characterChoice.name}!
                                        """)
                    characterChoice.hp += 100
                    pokemonCount += 1
                    if pokemonCount >= len(pokemonRoster):
                        messagebox.showwarning(title= "end Game", message= "game has ended, you have won, good job")
                        exit()

                # Pokémon action decision
                if current_pokemon.action() == "attacking":
                    actionchoice = random.choice(current_pokemon.attakList)
                    current_pokemon.attack(characterChoice, actionchoice[0], actionchoice[1], actionchoice[2], dmgOtCount=3)
                else:
                    actionchoice = random.choice(current_pokemon.defenList)
                    current_pokemon.defense(actionchoice[0], actionchoice[1], actionchoice[2], defenseCount=2)
                turn += 1
                player_turn()
                    

            
            except IndexError:
                messagebox.showinfo(title= "end game", text = "Game ended! Congratulations!")
                exit()

                
            



        
        
class character():
    def __init__(self, name, hp, agility, attakList, defenList, pokemonAttackChnc, pokemonDefenseChnc, dmgOtbeingInflictedRn, dmgOtCheck, dmgOtTurnsLeft, 
                 healthBeingIncreasedRn, healthCheck, healthTurnleft):
        self.name = name
        self.hp = hp
        self.agility = agility
        self.attakList = attakList
        self.defenList = defenList
        self.pokemonAttackchnc = pokemonAttackChnc
        self.pokemonDefenseChnc = pokemonDefenseChnc
        self.dmgOtCheck = False
        self.dmgOtbeingInflictedRn = 0
        self.dmgOtTurnsLeft = 0  
        self.healthBeingIncreasedRn = 0
        self.healthCheck = False
        self.healthTurnleft = 0
        # if turn%2 != 0:
        #     self.turnUser = "player"
        # else:
        #     self.turnUser = "CPU"

    def intro(self, characterChoiceName):
        for widget in characterSelectionScreen.winfo_children():
            widget.grid_forget()
            # Load and display images for character selection
        image_references['Heavy'] = ImageTk.PhotoImage(Image.open('charactershowcase/Heavy.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter1 = tk.Label(characterSelectionScreen,image=image_references['Heavy'])

        image_references['Scout'] = ImageTk.PhotoImage(Image.open('charactershowcase/scout.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter2 = tk.Label(characterSelectionScreen,image=image_references['Scout'])

        image_references['Doc'] = ImageTk.PhotoImage(Image.open('charactershowcase/doc.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter3 = tk.Label(characterSelectionScreen, image=image_references['Doc'])

        image_references['Spy'] = ImageTk.PhotoImage(Image.open('charactershowcase/spy.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter4 = tk.Label(characterSelectionScreen, image=image_references['Spy'])

        image_references['Pyro'] = ImageTk.PhotoImage(Image.open('charactershowcase/pyro.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter5 = tk.Label(characterSelectionScreen, image=image_references['Pyro'])

        image_references['Demo'] = ImageTk.PhotoImage(Image.open('charactershowcase/demo.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter6 = tk.Label(characterSelectionScreen,image=image_references['Demo'])

        image_references['Engy'] = ImageTk.PhotoImage(Image.open('charactershowcase/engy.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter7 = tk.Label(characterSelectionScreen, image=image_references['Engy'])

        image_references['Sniper'] = ImageTk.PhotoImage(Image.open('charactershowcase/Sniper.png').resize((175, 250)).convert('RGBA'))
        DisplayCharacter8 = tk.Label(characterSelectionScreen, image=image_references['Sniper'])
        DisplayCharacter1.grid(row=1, column=0)
        DisplayCharacter2.grid(row=1, column=1)
        DisplayCharacter3.grid(row=1, column= 2)
        DisplayCharacter4.grid(row=1, column = 3)
        DisplayCharacter5.grid(row=3, column=0)
        DisplayCharacter6.grid(row=3, column=1)
        DisplayCharacter7.grid(row=3, column= 2)
        DisplayCharacter8.grid(row=3, column = 3)

        button1 = tk.Button(characterSelectionScreen, text='Heavy', width=10, command=lambda: displayStats(1))
        button1.grid(row=2, column=0, padx= 5)
        button2 = tk.Button(characterSelectionScreen, text='Scout', width=10, command=lambda: displayStats(2))
        button2.grid(row=2, column=1, padx= 5)
        button3 = tk.Button(characterSelectionScreen, text='Doc',width=10, command=lambda: displayStats(3))
        button3.grid(row=2, column=2, padx= 5)
        button4 = tk.Button(characterSelectionScreen, text='Spy', width=10, command=lambda: displayStats(4))
        button4.grid(row=2, column=3, padx= 5)
    

        button5 = tk.Button(characterSelectionScreen, text='Pyro', width=10, command=lambda: displayStats(5))
        button5.grid(row=4, column=0, padx= 5)
        button6 = tk.Button(characterSelectionScreen, text='Demo', width=10, command=lambda: displayStats(6))
        button6.grid(row=4, column=1, padx= 5)
        button7 = tk.Button(characterSelectionScreen, text='Engy', width=10, command=lambda: displayStats(7))
        button7.grid(row=4, column=2, padx= 5)
        button8 = tk.Button(characterSelectionScreen, text='Sniper', width=10, command=lambda: displayStats(8))
        button8.grid(row=4, column=3, padx= 5)
        nameDisplayText = tk.Label(characterSelectionScreen, text=f"Name:{self.name}", font="Arial")
        nameDisplayText.grid(row= 5, column= 0)
        healthDisplayText = tk.Label(characterSelectionScreen, text=f"Health:{self.hp}", font="Arial")
        healthDisplayText.grid(row= 6, column= 0)
        AttackDisplayText = tk.Label(characterSelectionScreen, text="ATTACKS: ", font="Arial")
        AttackDisplayText.grid(row= 6, column= 1)
        agilityDisplayText = tk.Label(characterSelectionScreen, text=f"Agility:{self.agility}", font="Arial")
        agilityDisplayText.grid(row= 7, column= 0)
        DefenseDisplayText = tk.Label(characterSelectionScreen, text="DEFENSES: ", font="Arial")
        DefenseDisplayText.grid(row= len(self.attakList)+8, column= 1)
    
        button1 = tk.Button(characterSelectionScreen, text='Confirm Choice Button', width=20, command=lambda: BattleArena(self, characterChoiceName))
        button1.grid(row=len(self.attakList)+len(self.defenList)+9, column=0, padx= 5)

        
        for i in range(len(self.attakList)):
            CharacterAttackDisplay1 = tk.Label(characterSelectionScreen, text = f"{i+1}. Attack name = {self.attakList[i][0]}|")
            CharacterAttackDisplay1.grid(row= 7+i, column= 1)
            CharacterAttackDisplay2 = tk.Label(characterSelectionScreen, text = f"instant damage = {self.attakList[i][1]}|") 
            CharacterAttackDisplay2.grid(row= 7+i, column= 2)
            CharacterAttackDisplay3 = tk.Label(characterSelectionScreen, text = f" damage over 3 turns = {self.attakList[i][2]}") 
            CharacterAttackDisplay3.grid(row= 7+i, column= 3)  
        for l in range(len(self.defenList)):
            CharacterDefenseDisplay1 = tk.Label(characterSelectionScreen, text = f"{l+1}. Defense name = {self.defenList[l][0]}|")
            CharacterDefenseDisplay1.grid(row= len(self.attakList)+l+9, column= 1)
            CharacterDefenseDisplay2 = tk.Label(characterSelectionScreen, text = f"verbose for round = {self.defenList[l][1]}|") 
            CharacterDefenseDisplay2.grid(row= len(self.attakList)+l+9, column= 2)
            CharacterDefenseDisplay3 = tk.Label(characterSelectionScreen, text = f" health increase = {self.defenList[l][2]}") 
            CharacterDefenseDisplay3.grid(row= len(self.attakList)+l+9, column= 3)
        

    def attack(self, target, attackName, attackValue, dmgOt, dmgOtCount):
        messagebox.showinfo(arena, message = f"{self.name} attacks {target.name} using {attackName} with power {attackValue}.")
        
        if dmgOt > 0:
            messagebox.showinfo(arena, message = f"{attackName} will also deal {dmgOt} damage over {dmgOtCount} turns.")

        attackSuccess = random.randint(1, 100)
        if attackSuccess > self.agility:
            messagebox.showwarning(arena, message = f"{attackName} has failed! {target.name}'s health is currently {target.hp}")

        else:
            target.hp -= attackValue
            messagebox.showwarning(arena, message = f"{self.name} has succeeded in attacking {target.name}, their health is now {target.hp}")

            
            if dmgOt > 0:
                messagebox.showinfo(arena, message = f"Over the next {dmgOtCount} turns, {target.name} will be inflicted by {dmgOt} damage each turn.")

                target.dmgOtCheck = True
                target.dmgOtbeingInflictedRn = dmgOt
                target.dmgOtTurnsLeft = dmgOtCount
                
    def dmgOtAction(self):
        if self.dmgOtTurnsLeft > 0:
            self.hp -= self.dmgOtbeingInflictedRn
            messagebox.showwarning(title="Damage Over Time Alert", message=f"""{self.name} experiences {self.dmgOtbeingInflictedRn} DoT damage, {self.dmgOtTurnsLeft} turns remaining.
            {self.name}'s hp is now {self.hp}""")
            self.dmgOtTurnsLeft -= 1
            if self.dmgOtTurnsLeft == 0:
                self.dmgOtCheck = False
        else:
            messagebox.showwarning(title="Damage Over Time Alert", message=f"{self.name} no longer suffers from damage over time effect.")
            
    def defense(self, defenseName,defenseValue, hpValue, defenseCount):
        if defenseValue > 0:
            self.healthTurnleft = defenseCount
            self.healthCheck = True
            self.healthBeingIncreasedRn = defenseValue
            #arena
            messagebox.showinfo(arena, message = f"{self.name} uses {defenseName} with verbose {defenseValue} for {self.healthTurnleft} round.")
            self.hp += self.healthBeingIncreasedRn
            self.defenseOtAction()
        
        if hpValue > 0:
            self.hp += hpValue  
            messagebox.showinfo(title = "health point effect", message = f"""{self.name} ability increases its health points by {hpValue}, this effect is permenant!
            {self.name}'s health is now {self.hp}""")

    def defenseOtAction(self):
        if self.healthTurnleft > 0:
            messagebox.showwarning(title="Health Buff", message= f"""{self.name} experiences {self.healthBeingIncreasedRn} Health being temporarily enhanced for {self.healthTurnleft} turns remaining."
                     {self.name}'s health is now {self.hp}""")
            self.healthTurnleft -= 1
            if self.healthTurnleft == 0:
                self.healthCheck = False
                self.hp -= self.healthBeingIncreasedRn
        else:
            messagebox.showinfo(title = "Health over time", message = f"{self.name} no longer has enhanced health over time.")

    def action(self):
        actionRoll = random.randint(1, 100)
        
        if actionRoll <= self.pokemonAttackchnc:
            move = "attacking"
        else:
            move = "defending"
            
        return move

#PICK CHARACTER #PICK CHARACTER #PICK CHARACTER #PICK CHARACTER #PICK CHARACTER #PICK CHARACTER #PICK CHARACTER #PICK CHARACTER #PICK CHARACTER#PICK CHARACTER


window.mainloop()

