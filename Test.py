"""
Human Character Sheet
Program: This is a character creation program where we apply numerical values to different attributes 
(Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) then apply them to contextual modifiers. This program is heavily
inspired Dungeons and Dragons and while it can be used in Tabletop Roleplaying Games (TTRPG), but the program extends beyond gaming. 
The program can be used to model agents in simulations, tracking development, or evalute configurable systems where attributes follow
rules and modifiers. This program is not used to represent real individuals, only entities.  
"""


class abilityScore:
    def __init__(self, score):
        self.score = score
    
    def standard_array():
        print("Standard Array: 8, 10, 12, 13, 14, 15")
        s_array = [8, 10 , 12, 13, 14, 15]
        ability_score = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

        for array in ability_score:
            while True:
                try:
                    score = int(input(f"Enter a score for {array}: "))
                    if score in s_array: #checks if the check is inside s_array
                        ability_score[array] = score #ability_score is the dictionary. [array] is the loop that goes through each element. score is the the number that is sabedsaved in the element every loop
                        s_array.remove(score)
                        if s_array:
                            print(f"Remaining scores: {s_array}")
                        break
                    else:
                        print("Invalid scores. Please choose from the remaining scores.")
                except ValueError:
                    print("Invalid input. Please enter a number")
        return ability_score


class Character:
    def __init__(self, name, score):
        self.name = name
        self.speed = 0 #Int
        self.score = score

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Speed: {self.speed}")
        self.score_to_modifer()

    def race_human(human):
        human.score["STR"] += 1
        human.score["DEX"] += 1
        human.score["CON"] += 1
        human.score["INT"] += 1
        human.score["WIS"] += 1
        human.score["CHA"] += 1
        human.speed = 30
        
    
    def race_tiefling(tiefling):
        #PHB version
        tiefling.score["CHA"] += 2
        tiefling.score["INT"] += 1
        tiefling.speed = 30

    def race_gnome(gnome):
        #PHB
        gnome.score["INT"] += 2
        gnome.speed = 25

        gnome_choice = input("Choose which Gnome subrace to play as: Forest (+1 to DEX) or Rock (+1 to CON)): ").lower()
        if gnome_choice == "forest":
            gnome.score["DEX"] += 1
        elif gnome_choice == "rock":
            gnome.score["CON"] += 1
        else:
            print("Error. Please choose between Forest or Rock")
            gnome.race_gnome
            
    def score_to_modifer(modifier):
        print("Ability Modifier:\n")
        for ability, value in modifier.score.items():
            modifier = (value - 10) // 2
            print(f"{ability}: {modifier}")


class Skills:
    def __init__(self):
        pass

#Role instead of class becasue class is a programming language term
class Level:
    Role_DATA = {
        "Fighter": {
            "Saving Throws": ["STR", "CON"],
            "Skills": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
            "Skill_Choice": 2            
            }, 
        "Barbarian": {
            "Saving Throws": ["STR", "CON"],
            "Skills": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
            "Skill_Choice": 2
            },
        "Cleric": {
            "Saving Throws": ["WIS", "CHA"],
            "Skills": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
            "Skill_Choice": 2
            },
        "Monk": {
            "Saving Throws": ["STR", "DEX"],
            "Skills": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
            "Skill_Choice": 2            
        },
        "Rogue": {
            "Saving Throw": ["DEX", "INT"],
            "Skills": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
            "Skill_Choice": 3
        },
        "Bard": {
            "Saving Throw": ["WIS", "CHA"]

        }
        #...
        }

    def __init__(self, level):
        self.level = level
        self.proficiency = self.get_proficiency_bonus(level)
    
    def get_proficiency_bonus(level):
        if not (1 <= level <= 20):
            raise ValueError("Level must be between 1 and 20")
        return ((level - 1) // 4) + 2
    
class Role: 
    def __init__(self):
        pass

    def get_class(role):
        roles = ["Fighter", "Barbarian", "Cleric", "Monk", "Ranger", "Druid", "Paladin", "Rogue", "Sorcerer", "Warlock", "Wizard"]
        if role in roles:
            pass
        else:
            raise ValueError(f"Invalid Error: {role}. Must be one of the {role}")


scores = abilityScore.standard_array()

my_character = Character("Adrannis", scores)
my_character.race_human()
my_character.display_stats()

gnome_char = Character("Pike", scores)
gnome_char.race_gnome()
gnome_char.display_stats()


"""
#Assuming Standard array
score = {"STR": 15, "DEX": 12, "CON": 14, "INT": 8, "WIS": 13, "CHA": 10}
human = Character("Bob", score)

#updated version
human.race_human()

human.display_stats()

#Tiefling Version
score = {"STR": 8, "DEX": 12, "CON": 14, "INT": 10, "WIS": 13, "CHA": 15}
tiefling = Character("Jester", score)
tiefling.race_tiefling()
tiefling.display_stats()
"""
"""
score = {"STR": 15, "DEX": 12, "CON": 14, "INT": 8, "WIS": 13, "CHA": 10}
gnome = Character("Pike", score)
gnome.race_gnome()
gnome.display_stats()
"""