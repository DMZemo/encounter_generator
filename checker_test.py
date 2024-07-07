import random
import pandas as pd
import tkinter as tk
from tkinter import ttk, Canvas, StringVar, OptionMenu, Label, Button, Text, Entry, PhotoImage

# TYPICAL, HUMANOID, FAUNA, FLORA
# 50% roll for TYPICAL, 50% check for HUMANOID/FAUNA/FLORA

# CORE DICTIONARIES (THE FUEL OF THE ENGINE)
biomes = {
    'ATMOSPHERE': {                 "humanoid": 0,  "fauna": 0, "flora": 0},
    'MARINE': {                     "humanoid": 1,  "fauna": 5, "flora": 2},
    'GLACIER': {                    "humanoid": 2,  "fauna": 1, "flora": 1},
    'TUNDRA': {                     "humanoid": 3,  "fauna": 4, "flora": 5},
    'TAIGA': {                      "humanoid": 4,  "fauna": 6, "flora": 6},
    'COLD DESERT': {                "humanoid": 5,  "fauna": 3, "flora": 3},
    'HOT DESERT': {                 "humanoid": 6,  "fauna": 2, "flora": 4},
    'TROPICAL RAIFOREST': {         "humanoid": 7,  "fauna": 13,"flora": 13},
    'WETLAND': {                    "humanoid": 8,  "fauna": 7, "flora": 8},
    'TROPICAL SEASONAL FOREST': {   "humanoid": 9,  "fauna": 12,"flora": 7},
    'SAVANNA': {                    "humanoid": 10, "fauna": 9, "flora": 10},
    'GRASSLAND': {                  "humanoid": 11, "fauna": 8, "flora": 9},
    'TEMPERATE DECIDUOUS FOREST': { "humanoid": 12, "fauna": 10,"flora": 12},
    'TEMPERATE RAINFOREST': {       "humanoid": 13, "fauna": 11,"flora": 11}
}

times_of_day = {
    'Morning': {'humanoid': 4, 'fauna': 1, 'flora': 2},
    'Midday': {'humanoid': 3, 'fauna': 2, 'flora': 4},
    'Evening': {'humanoid': 2, 'fauna': 3, 'flora': 3},
    'Midnight': {'humanoid': 1, 'fauna': 4, 'flora': 1}
}

seasons = {
    'Spring': {'humanoid': 3, 'fauna': 3, 'flora': 4},
    'Summer': {'humanoid': 4, 'fauna': 1, 'flora': 3},
    'Fall': {'humanoid': 2, 'fauna': 4, 'flora': 2},
    'Winter': {'humanoid': 1, 'fauna': 2, 'flora': 1}
}

traffic = {
    'Barren': -2,
    'Sparse': -1,
    'Populated': 1,
    'Busy': 2}

temp = {
    'Cold': -2,
    'Hot': -1,
    'Cool': 0,
    'Warm': 2,
    'Mild': 3}

wind = {
    'Strong': 0,
    'None': 1,
    'Light': 3}

precipitation = {
    'Wet': 0,
    'Normal': 1,
    'Dry': 2}

speed = {
    'Quick': 3,
    'Normal': 0,
    'Cautious': -3}

attitude = {
    'Hostile': 3,
    'Neutral': 0,
    'Friendly': -3}

encounters = [
    "TYPICAL", 
    "HUMANOID", 
    "FAUNA", 
    "FLORA"]

Rael_Humanoids = {
    "3.1.1.0": "Mortal_Humanoid.Dwarf.Duergar",
    "3.1.2.0": "Mortal_Humanoid.Dwarf.Hill",
    "3.1.3.0": "Mortal_Humanoid.Dwarf.Mountain",
    "3.1.4.0": "Mortal_Humanoid.Dwarf.Derro",
    "3.1.5.0": "Mortal_Humanoid.Dwarf.Magma",
    "3.1.6.0": "Mortal_Humanoid.Dwarf.Fire",
    "3.2.1.0": "Mortal_Humanoid.Sylvan.Fairy",
    "3.2.2.0": "Mortal_Humanoid.Sylvan.Satyr",
    "3.2.3.0": "Mortal_Humanoid.Sylvan.Changeling",
    "3.2.4.0": "Mortal_Humanoid.Sylvan.Shadar-kai",
    "3.2.5.0": "Mortal_Humanoid.Sylvan.Drow",
    "3.2.6.1": "Mortal_Humanoid.Sylvan.Elf.High",
    "3.2.6.2": "Mortal_Humanoid.Sylvan.Elf.Wood",
    "3.2.6.3": "Mortal_Humanoid.Sylvan.Elf.Sea",
    "3.2.6.4": "Mortal_Humanoid.Sylvan.Elf.High_Half",
    "3.2.6.5": "Mortal_Humanoid.Sylvan.Elf.Wood_Half",
    "3.2.6.6": "Mortal_Humanoid.Sylvan.Elf.Sea_Half",
    "3.3.1.0": "Mortal_Humanoid.Smallkin.Deep_Gnome",
    "3.3.2.0": "Mortal_Humanoid.Smallkin.Forest_Gnome",
    "3.3.3.0": "Mortal_Humanoid.Smallkin.Rock_Gnome",
    "3.3.4.0": "Mortal_Humanoid.Smallkin.Stout_Halfling",
    "3.3.5.0": "Mortal_Humanoid.Smallkin.Lightfoot_Halfling",
    "3.3.6.0": "Mortal_Humanoid.Smallkin.Travelling_Halfling",
    "3.4.1.0": "Mortal_Humanoid.Human.Basic",
    "3.4.2.0": "Mortal_Humanoid.Human.Air",
    "3.4.3.0": "Mortal_Humanoid.Human.Water",
    "3.4.4.0": "Mortal_Humanoid.Human.Fire",
    "3.4.5.0": "Mortal_Humanoid.Human.Earth",
    "3.4.6.0": "Mortal_Humanoid.Human.Variant",
    "3.5.1.1": "Mortal_Humanoid.Monstrous.Reptilian.Lizardfolk",
    "3.5.1.2": "Mortal_Humanoid.Monstrous.Reptilian.Kobold",
    "3.5.1.3": "Mortal_Humanoid.Monstrous.Reptilian.Tortle",
    "3.5.1.4": "Mortal_Humanoid.Monstrous.Reptilian.Triton",
    "3.5.1.5": "Mortal_Humanoid.Monstrous.Reptilian.Yuan_ti",
    "3.5.1.6.Bk": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Black",
    "3.5.1.6.Bl": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Blue",
    "3.5.1.6.Gr": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Green",
    "3.5.1.6.Rd": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Red",
    "3.5.1.6.Wi": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.White",
    "3.5.1.6.Bs": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Brass",
    "3.5.1.6.Br": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Bronze",
    "3.5.1.6.Cp": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Copper",
    "3.5.1.6.Go": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Gold",
    "3.5.1.6.Si": "Mortal_Humanoid.Monstrous.Reptilian.Dragonborn.Silver",
    "3.5.2.1": "Mortal_Humanoid.Monstrous.Beastial.Harengon",
    "3.5.2.2": "Mortal_Humanoid.Monstrous.Beastial.Minotaur",
    "3.5.2.3": "Mortal_Humanoid.Monstrous.Beastial.Centaur",
    "3.5.2.4": "Mortal_Humanoid.Monstrous.Beastial.Tabaxi",
    "3.5.2.5": "Mortal_Humanoid.Monstrous.Beastial.Aarakocra",
    "3.5.2.6": "Mortal_Humanoid.Monstrous.Beastial.Kenku",
    "3.5.3.1": "Mortal_Humanoid.Monstrous.Giantkin.Orc/Half-Orc",
    "3.5.3.2": "Mortal_Humanoid.Monstrous.Giantkin.Firbolg",
    "3.5.3.3": "Mortal_Humanoid.Monstrous.Giantkin.Goliath",
    "3.5.3.4": "Mortal_Humanoid.Monstrous.Giantkin.Bugbear",
    "3.5.3.5": "Mortal_Humanoid.Monstrous.Giantkin.Goblin",
    "3.5.3.6": "Mortal_Humanoid.Monstrous.Giantkin.Hobgoblin",
    "3.6.1.0": "Mortal_Humanoid.Planar.Aasimar",
    "3.6.2.0": "Mortal_Humanoid.Planar.Tiefling",
    "3.6.3.0": "Mortal_Humanoid.Planar.Air_Genasi",
    "3.6.4.0": "Mortal_Humanoid.Planar.Earth_Genasi",
    "3.6.5.0": "Mortal_Humanoid.Planar.Fire_Genasi",
    "3.6.6.0": "Mortal_Humanoid.Planar.Water_Genasi"}

Beasts = {
    "4.1.1.1": "Non_Humanoid.Beast.Quadruped.Equine",
    "4.1.1.2": "Non_Humanoid.Beast.Quadruped.Canine",
    "4.1.1.3": "Non_Humanoid.Beast.Quadruped.Feline",
    "4.1.1.4": "Non_Humanoid.Beast.Quadruped.Bovine",
    "4.1.1.5": "Non_Humanoid.Beast.Quadruped.Ursine",
    "4.1.1.6": "Non_Humanoid.Beast.Quadruped.Cervine",
    "4.1.2.1": "Non_Humanoid.Beast.Winged.Avian",
    "4.1.2.2": "Non_Humanoid.Beast.Winged.Chiroptian",
    "4.1.2.3": "Non_Humanoid.Beast.Winged.Feyian",
    "4.1.2.4": "Non_Humanoid.Beast.Winged.Draconian",
    "4.1.2.5": "Non_Humanoid.Beast.Winged.Insectian",
    "4.1.2.6": "Non_Humanoid.Beast.Winged.Elementian",
    "4.1.3.1": "Non_Humanoid.Beast.Serpentine.Poisonous_Snake_Swarm",
    "4.1.3.2": "Non_Humanoid.Beast.Serpentine.Flying_Snake",
    "4.1.3.3": "Non_Humanoid.Beast.Serpentine.Poisonous_Snake",
    "4.1.3.4": "Non_Humanoid.Beast.Serpentine.Constrictor_Snake",
    "4.1.3.5": "Non_Humanoid.Beast.Serpentine.Giant_Poisonous_Snake",
    "4.1.3.6": "Non_Humanoid.Beast.Serpentine.Giant_Constrictor_Snake",
    "4.1.4.1": "Non_Humanoid.Beast.Aquatic.Fish",
    "4.1.4.2": "Non_Humanoid.Beast.Aquatic.Mammal",
    "4.1.4.3": "Non_Humanoid.Beast.Aquatic.Reptile ",
    "4.1.4.4": "Non_Humanoid.Beast.Aquatic.Crustacean",
    "4.1.4.5": "Non_Humanoid.Beast.Aquatic.Cephalopod",
    "4.1.4.6": "Non_Humanoid.Beast.Aquatic.Invertebrate",
    "4.1.5.1": "Non_Humanoid.Beast.Insectoid.Coleoptera",
    "4.1.5.2": "Non_Humanoid.Beast.Insectoid.Diptera",
    "4.1.5.3": "Non_Humanoid.Beast.Insectoid.Hymenoptera",
    "4.1.5.4": "Non_Humanoid.Beast.Insectoid.Lepidoptera",
    "4.1.5.5": "Non_Humanoid.Beast.Insectoid.Arachnid",
    "4.1.5.6": "Non_Humanoid.Beast.Insectoid.Myrapod",
    "4.1.6.1": "Non_Humanoid.Beast.Primate.Chimpanzee",
    "4.1.6.2": "Non_Humanoid.Beast.Primate.Gorilla",
    "4.1.6.3": "Non_Humanoid.Beast.Primate.Orangutan",
    "4.1.6.4": "Non_Humanoid.Beast.Primate.Lemur",
    "4.1.6.5": "Non_Humanoid.Beast.Primate.Macaque",
    "4.1.6.6": "Non_Humanoid.Beast.Primate.Flying Monkey"}

Plants = {
    "4.2.1.0": "Non_Humanoid.Plant.Ordinary",
    "4.2.2.0": "Non_Humanoid.Plant.Carnivorous",
    "4.2.3.0": "Non_Humanoid.Plant.Magical",
    "4.2.4.0": "Non_Humanoid.Plant.Alchemical",
    "4.2.5.0": "Non_Humanoid.Plant.Medicinal",
    "4.2.6.0": "Non_Humanoid.Plant.Very_Rare"}

humanoid_er = ()
fauna_er = ()
flora_er = ()
encounter_type = ()
sub_type = ()
survival = ()
survival_mod = ()

window = tk.Tk()
window.title("Random Encounter Calculator")

bg = PhotoImage(file = r"src_game\Entities\pop\Random_Encounters\astro.png")
bg_image = tk.Label(window, image = bg) 
bg_image.place(relheight=1,relwidth=1)


def generate_random_choices(dictionary, num_choices):
    random_keys = random.choices(list(dictionary.keys()), k=num_choices)
    random_values = [dictionary[key] for key in random_keys]
    #encounter_text.delete(1.0, tk.END)  # Clear previous output
    for key, value in zip(random_keys, random_values):
        update_encounter_text(f"\nTOKEN:{key}:{value}\n")

#FROM CALLER
##################
def generate_random_encounter(biome, encounter_type):
    biome_var == biome
    encounter_var == encounter_type
    clear_encounter_text()
    # Read the Excel file into a DataFrame
    df = pd.read_excel('C:\\Users\\phili\\OneDrive\\Desktop\\code\\helper\\src_game\\Entities\\pop\\Random_Encounters\\Master_Biome_Encounter_Lists.xlsx')
    # Filter the DataFrame based on the chosen biome and encounter type
    filtered_df = df[(df['Biome'] == biome) & (df['Encounter'] == encounter_type)]
    # Check if any encounters match the chosen criteria
    if filtered_df.empty:
        return "No encounters found for the chosen biome and encounter type."
    # Randomly select an encounter from the filtered DataFrame
    random_encounter = filtered_df.sample(n=1)
    # Get the columns and values of the random encounter
    columns = random_encounter.columns.tolist()
    values = random_encounter.values.tolist()[0]
    # Format the columns and values neatly with right justification
    formatted_encounter = '\n'.join([f"{column.rjust(10)}: {str(value).rjust(5)}" for column, value in zip(columns, values)])
    update_encounter_text(formatted_encounter)
    return formatted_encounter


# FROM CALLER
################
def biome_encounter_combiner():
    biome = biome_var.get()
    encounter = encounter_var.get()
    random_encounter = generate_random_encounter(biome, encounter)


def update_encounter_text(text):
    encounter_text.insert(tk.END, text)

def clear_encounter_text():
    encounter_text.delete('1.0', tk.END)

def survival_mod_calc():
    try:
        survival_check = int(survival.get())
        if survival_check <= 11:
            survival_mod = 0
        elif 12 <= survival_check <= 14:
            survival_mod = 1
        elif 15 <= survival_check <= 17:
            survival_mod = 2
        elif 18 <= survival_check <= 20:
            survival_mod = 3
        elif 21 <= survival_check <= 24:
            survival_mod = 4
        elif 25 <= survival_check < 40:
            survival_mod = 5
        elif survival_check == None:
            survival_mod = 1
        return survival_mod
    except ValueError:
        print("Invalid input, must be an integer")
        return None

encounter_text_label = Label(window, text="Results:")
encounter_text_label.grid(row=0, column=0, padx=5, pady=5)
encounter_text = Text(window, height=12, width=60)
encounter_text.grid(row=0, column=1, padx=5, pady=5)

clear_button = Button(window, text="Clear", command=clear_encounter_text)
clear_button.grid(row=0, column=2, columnspan=1, padx=10, pady=5)

# SURVIVAL INPUT
survival_label = tk.Label(text="Survival Check:")
survival_label.grid(row=10, column=0, padx=5, pady=5)
survival = tk.Entry(window, width=5) 
survival.grid(row=10, column=1, padx=5, pady=5)
survival_mod = survival_mod_calc()

# VARYING VARIABLES
## BIOME VARIABLES
biome_var = StringVar()
biome_humanoid_var = StringVar()
biome_fauna_var = StringVar()
biome_flora_var = StringVar()

## SEASON VARIABLES
season_var = StringVar()
season_humanoid_var = StringVar()
season_fauna_var = StringVar()
season_flora_var = StringVar()

## TIME OF DAY VARIABLES
time_of_day_var = StringVar()
time_of_day_humanoid_var = StringVar()
time_of_day_fauna_var = StringVar
time_of_day_flora_var = StringVar()

# STATIC VARIABLES
traffic_var = StringVar()
temp_var = StringVar()
wind_var = StringVar()
precipitation_var = StringVar()
speed_var = StringVar()
attitude_var = StringVar()
encounter_var = StringVar()

# BIOME LABEL & BUTTON
biome_label = Label(window, text="Biome:")
biome_label.grid(row=1, column=0, padx=5, pady=5)
biome_var = StringVar(window)
biome_var.set("ATMOSPHERE")  
biome_dropdown = OptionMenu(window, biome_var, *biomes.keys())
biome_dropdown.grid(row=1, column=1, padx=5, pady=5)

# SEASON LABEL & BUTTON
season_label = Label(window, text="Season:")
season_label.grid(row=2, column=0, padx=5, pady=5)
season_var = StringVar(window)
season_var.set("Winter")
season_dropdown = OptionMenu(window, season_var, *seasons.keys())
season_dropdown.grid(row=2, column=1, padx=5, pady=5)

# TIME OF DAY LABEL & BUTTON
time_of_day_label = Label(window, text="Time of Day:")
time_of_day_label.grid(row=3, column=0, padx=5, pady=5)
time_of_day_var = StringVar(window)
time_of_day_var.set("Morning") 
time_of_day_dropdown = OptionMenu(window, time_of_day_var, *times_of_day.keys())
time_of_day_dropdown.grid(row=3, column=1, padx=5, pady=5)

# TRAFFIC LABEL & BUTTON
traffic_label = Label(window, text="Traffic:")
traffic_label.grid(row=4, column=0, padx=5, pady=5)
traffic_var = StringVar(window)
traffic_var.set("Barren")
traffic_dropdown = OptionMenu(window, traffic_var, *traffic.keys())
traffic_dropdown.grid(row=4, column=1, padx=5, pady=5)

# TEMPERATURE LABEL & BUTTON
temp_label = Label(window, text="Temperature:")
temp_label.grid(row=5, column=0, padx=5, pady=5)
temp_var = StringVar(window)
temp_var.set("Cold")
temp_dropdown = OptionMenu(window, temp_var, *temp.keys())
temp_dropdown.grid(row=5, column=1, padx=5, pady=5)

# WIND LABEL & BUTTON
wind_label = Label(window, text="Wind:")
wind_label.grid(row=6, column=0, padx=5, pady=5)
wind_var = StringVar(window)
wind_var.set("Strong")
wind_dropdown = OptionMenu(window, wind_var, *wind.keys())
wind_dropdown.grid(row=6, column=1, padx=5, pady=5)

# PRECIPITATION LABEL & BUTTON
precipitation_label = Label(window, text="Precipitation:")
precipitation_label.grid(row=7, column=0, padx=5, pady=5)
precipitation_var = StringVar(window)
precipitation_var.set("Wet")
precipitation_dropdown = OptionMenu(window, precipitation_var, *precipitation.keys())
precipitation_dropdown.grid(row=7, column=1, padx=5, pady=5)

# SPEED LABEL & BUTTON
speed_label = Label(window, text="Speed:")
speed_label.grid(row=8, column=0, padx=5, pady=5)
speed_var = StringVar(window)
speed_var.set("Normal")
speed_dropdown = OptionMenu(window, speed_var, *speed.keys())
speed_dropdown.grid(row=8, column=1, padx=5, pady=5)

# ATTITUDE LABEL & BUTTON
attitude_label = Label(window, text="Attitude:")
attitude_label.grid(row=9, column=0, padx=5, pady=5)
attitude_var = StringVar(window)
attitude_var.set("Neutral")
attitude_dropdown = OptionMenu(window, attitude_var, *attitude.keys())
attitude_dropdown.grid(row=9, column=1, padx=5, pady=5)

# ENCOUNTER LABEL & BUTTON
encounter_label = Label(window, text="Encounter:")
encounter_label.grid(row=10, column=2, padx=5, pady=5)
encounter_var = StringVar(window)
encounter_var.set("TYPICAL")
encounter_dropdown = OptionMenu(window, encounter_var, *encounters)
encounter_dropdown.grid(row=10, column=3, padx=5, pady=5)

def set_encounter_ratings():
    selected_biome = biome_var.get()
    selected_time_of_day = time_of_day_var.get()
    selected_season = season_var.get()
    selected_traffic = traffic_var.get()
    selected_temp = temp_var.get()
    selected_wind = wind_var.get()
    selected_precipitation = precipitation_var.get()
    selected_speed = speed_var.get()
    selected_attitude = attitude_var.get()
    survival_mod = survival_mod_calc()
   
    humanoid_er = int(biomes[selected_biome]['humanoid']) + int(times_of_day[selected_time_of_day]['humanoid']) + int(traffic[selected_traffic]) + int(survival_mod * (int(speed[selected_speed]) + int(attitude[selected_attitude])))
    fauna_er = int(biomes[selected_biome]['fauna']) + int(times_of_day[selected_time_of_day]['fauna']) + int(seasons[selected_season]['fauna']) + int(wind[selected_wind]) + int(survival_mod * (int(speed[selected_speed]) + int(attitude[selected_attitude])))
    flora_er = int(biomes[selected_biome]['flora']) + int(times_of_day[selected_time_of_day]['flora']) + int(seasons[selected_season]['flora']) + int(temp[selected_temp]) + int(precipitation[selected_precipitation]) + int(survival_mod * (int(speed[selected_speed]) + int(attitude[selected_attitude])))
    
    update_encounter_text(f"\nHumanoid ER: {humanoid_er}\n Fauna ER: {fauna_er}\n Flora ER: {flora_er}\n")
    return humanoid_er, fauna_er, flora_er

def check_encounter_type():
    type_roll = random.randint(1,100)
    update_encounter_text(f"Type Roll:{type_roll}:")

    if type_roll <= 60:
        encounter_type = "Humanoid"
        update_encounter_text("Humanoid:")
    elif 60 < type_roll <= 80:
        encounter_type = "Fauna"
        update_encounter_text("Fauna:")
    elif type_roll >= 81:
        encounter_type = "Flora"
        update_encounter_text("Flora:")

    sub_type_roll = random.randint(1,100)

    if encounter_type == "Humanoid":
        update_encounter_text(f"Sub-Type:{sub_type_roll} ")
        if sub_type_roll <= 75:
            sub_type = "Humanoid"
            update_encounter_text("Humanoid! \n")
            generate_random_encounter
            generate_random_choices(Rael_Humanoids, 1)
            return sub_type
        elif 75 < sub_type_roll <= 89:
            sub_type = "Humanoid Event"
            update_encounter_text("Humanoid Event! \n")
            generate_random_encounter
            generate_random_choices(Rael_Humanoids, 1)
            return sub_type
        elif sub_type_roll >= 90:
            sub_type = "Humanoid Corpse"
            update_encounter_text("Humanoid Corpse! \n")
            generate_random_encounter
            generate_random_choices(Rael_Humanoids, 1)
            return sub_type

    if encounter_type == "Fauna":
        update_encounter_text(f"Sub-Type:{sub_type_roll} ")
        if sub_type_roll <= 75:
            sub_type = "Fauna"
            update_encounter_text(f"Fauna! \n")
            generate_random_encounter
            generate_random_choices(Beasts, 1)
            return sub_type
        elif 75 < sub_type_roll <= 89:
            sub_type = "Mega Fauna"
            update_encounter_text(f"Mega Fauna! \n")
            generate_random_encounter
            generate_random_choices(Beasts, 1)
            return sub_type
        elif sub_type_roll >= 90:
            sub_type = "Apex Predator"
            update_encounter_text(f"Apex Predator! \n")
            generate_random_encounter
            generate_random_choices(Beasts, 1)
            return sub_type

    if encounter_type == "Flora":
        update_encounter_text(f"Sub-Type:{sub_type_roll} ")
        if sub_type_roll <= 75:
            sub_type = "Flora"
            update_encounter_text(f"Flora! \n")
            generate_random_encounter
            generate_random_choices(Plants, 1)
            return sub_type
        elif 75 < sub_type_roll <= 89:
            sub_type = "Mega Flora"
            update_encounter_text(f"Mega Flora! \n")
            generate_random_encounter
            generate_random_choices(Plants, 1)
            return sub_type
        elif sub_type_roll >= 90:
            sub_type = "Magic Font"
            update_encounter_text(f"Magic Font! \n")
            generate_random_encounter
            generate_random_choices(Plants, 1)
            return sub_type
    else: pass

def roll20():
    roll = random.randint(1,20)
    return roll

def check_for_encounter():
    humanoid_er, fauna_er, flora_er = set_encounter_ratings()
    sub_type = check_encounter_type()
    survival_mod = survival_mod_calc()
    roll = roll20()
    survival_mod = survival_mod_calc()
    check = (survival_mod + roll)

    #update_encounter_text(f"Humanoid ER:{humanoid_er}, Fauna ER:{fauna_er}, Flora ER:{flora_er}\n")
    update_encounter_text(f"Survival Mod: {survival_mod} + {roll} = Survival Total:{check}\n")
    update_encounter_text(f"Checked For: {sub_type}\n")

    if sub_type == "Humanoid":
        if check < humanoid_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == humanoid_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > humanoid_er:
            update_encounter_text(f"No Humanoid Encounter.\n")
            return False
    elif sub_type == "Humanoid Event":
        if check < humanoid_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == humanoid_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > humanoid_er:
            update_encounter_text(f"No Humanoid Event Encounter.\n")
            return False
    elif sub_type == "Humanoid Corpse":
        if check < humanoid_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == humanoid_er:
            update_encounter_text(f"Special\n")
            return True
        elif check > humanoid_er:
            update_encounter_text(f"No Humanoid Corpse Encounter.\n")
            return False
    elif sub_type == "Fauna":
        if check < fauna_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == fauna_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > fauna_er:
            update_encounter_text(f"No Fauna Encounter.\n")
            return False
    elif sub_type == "Mega Fauna":
        if check < fauna_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == fauna_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > fauna_er:
            update_encounter_text(f"No Mega Fauna Encounter.\n")
            return False
    elif sub_type == "Apex Predator":
        if check < fauna_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == fauna_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > fauna_er:
            update_encounter_text(f"No Apex Predator Encounter.\n")
            return False
    elif sub_type == "Flora":
        if check < flora_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == flora_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > flora_er:
            update_encounter_text(f"No Flora Encounter.\n")
            return False
    elif sub_type == "Mega Flora":
        if check < flora_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == flora_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > flora_er:
            update_encounter_text(f"No Mega Flora Encounter.\n")
            return False
    elif sub_type == "Magic Font":
        if check < flora_er:
            update_encounter_text(f"Encounter!\n")
            return True
        elif check == flora_er:
            update_encounter_text(f"Special!\n")
            return True
        elif check > flora_er:
            update_encounter_text(f"No Magic Font Encounter.\n")
            return False
    else:
        pass
    update_encounter_text(f"\n")

set_encounter_ratings_button = Button(window, text="See Encounter Ratings", command=set_encounter_ratings)
set_encounter_ratings_button.grid(row=1, column=2, columnspan=1, padx=2, pady=2)

check_encounter_type_button = Button(window, text="Check Encounter Type", command= check_encounter_type)
check_encounter_type_button.grid(row=2, column=2, columnspan=1, padx=2, pady=2)

check_for_encounter_button = Button(window, text="Check For Encounter", command= check_for_encounter)
check_for_encounter_button.grid(row=3, column=2, columnspan=1, padx=2, pady=2)

check_for_encounter_button = Button(window, text="Encounter&Biome", command= biome_encounter_combiner)
check_for_encounter_button.grid(row=9, column=2, columnspan=1, padx=2, pady=2)

window.mainloop()
