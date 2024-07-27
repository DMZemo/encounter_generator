import random
import pandas as pd
import calendar
import tkinter as tk
from tkinter import ttk, Canvas, StringVar, OptionMenu, Label, Button, Text, Entry, PhotoImage, font
from PIL import ImageTk, Image
from tkinter import filedialog

# CORE DICTIONARIES (THE FUEL OF THE ENGINE)
biomes = {
    'ATMOSPHERE': {"humanoid": 0, "fauna": 0, "flora": 0},
    'MARINE': {"humanoid": 1, "fauna": 5, "flora": 2},
    'GLACIER': {"humanoid": 2, "fauna": 1, "flora": 1},
    'TUNDRA': {"humanoid": 3, "fauna": 4, "flora": 5},
    'TAIGA': {"humanoid": 4, "fauna": 6, "flora": 6},
    'COLD_DESERT': {"humanoid": 5, "fauna": 3, "flora": 3},
    'HOT_DESERT': {"humanoid": 6, "fauna": 2, "flora": 4},
    'TROPICAL_RAINFOREST': {"humanoid": 7, "fauna": 13, "flora": 13},
    'WETLAND': {"humanoid": 8, "fauna": 7, "flora": 8},
    'TROPICAL_SEASONAL_FOREST': {"humanoid": 9, "fauna": 12, "flora": 7},
    'SAVANNA': {"humanoid": 10, "fauna": 9, "flora": 10},
    'GRASSLAND': {"humanoid": 11, "fauna": 8, "flora": 9},
    'TEMPERATE_DECIDUOUS_FOREST': {"humanoid": 12, "fauna": 10, "flora": 12},
    'TEMPERATE_RAINFOREST': {"humanoid": 13, "fauna": 11, "flora": 11}
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
    'Busy': 2
}

temp = {
    'Cold': -2,
    'Hot': -1,
    'Cool': 0,
    'Warm': 2,
    'Mild': 3
}

wind = {
    'Strong': 0,
    'None': 1,
    'Light': 3
}

precipitation = {
    'Wet': 0,
    'Normal': 1,
    'Dry': 2
}

speed = {
    'Quick': 3,
    'Normal': 0,
    'Cautious': -3
}

attitude = {
    'Hostile': 3,
    'Neutral': 0,
    'Friendly': -3
}

encounters = [
    "TYPICAL", 
    "HUMANOID", 
    "FAUNA", 
    "FLORA"
]

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
    "3.6.6.0": "Mortal_Humanoid.Planar.Water_Genasi"
}

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
    "4.1.6.6": "Non_Humanoid.Beast.Primate.Flying Monkey"
}

Plants = {
    "4.2.1.0": "Non_Humanoid.Plant.Ordinary",
    "4.2.2.0": "Non_Humanoid.Plant.Carnivorous",
    "4.2.3.0": "Non_Humanoid.Plant.Magical",
    "4.2.4.0": "Non_Humanoid.Plant.Alchemical",
    "4.2.5.0": "Non_Humanoid.Plant.Medicinal",
    "4.2.6.0": "Non_Humanoid.Plant.Very_Rare"
}

survival_mods = {
    "0-11": 0,
    "12-14": 1,
    "15-17": 2,
    "18-20": 3,
    "21-24": 4,
    "25+": 5
}

encounter_log = []
boxes = []

humanoid_er = ()
fauna_er = ()
flora_er = ()
encounter_type = ()
sub_type = ()
survival = ()
survival_mod = ()

window = tk.Tk()
window.title("Random Encounter Calculator")

# Function to update the encounter text in the calendar window
def update_encounter_text(text):
    encounter_text.insert(tk.END, text)

# Function to clear the encounter text in the calendar window
def clear_encounter_text():
    encounter_text.delete('1.0', tk.END)

# Function to clear the calendar
def clear_calendar():
    global boxes
    for box in boxes:
        box.config(text="")

# Function to update the displayed image
def update_image(biome):
    image_path = f"C:/Users/phili/OneDrive/Desktop/code/helper/src_game/Entities/pop/Random_Encounters/All_Biome_Images/{biome.upper()}.png"
    image = Image.open(image_path)
    
    # Resize the image to fit within the window dimensions
    window_width = 800
    window_height = 800
    image = image.resize((window_width, window_height), Image.BICUBIC)
    
    tk_image = ImageTk.PhotoImage(image)
    image_label.configure(image=tk_image)
    image_label.image = tk_image

# Create a label to display the image
image_label = tk.Label(window)
image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the image label over the entire window

# Function to handle the selection change
def on_select_change(event):
    selected_biome = biome_var.get()
    update_image(selected_biome)

def generate_random_choices(dictionary, num_choices):
    random_keys = random.choices(list(dictionary.keys()), k=num_choices)
    random_values = [dictionary[key] for key in random_keys]
    for key, value in zip(random_keys, random_values):
        update_encounter_text(f"\nTOKEN:{key}:{value}\n\n")

def generate_random_encounter(biome, encounter_type):
    # Read the Excel file into a DataFrame
    df = pd.read_excel('C:\\Users\\phili\\OneDrive\\Desktop\\code\\helper\\src_game\\Entities\\pop\\Random_Encounters\\Master_Biome_Encounter_Lists.xlsx')

    # Filter the DataFrame based on the chosen biome and encounter type
    filtered_df = df[(df['Biome'] == biome) & (df['Encounter'] == encounter_type)]

    # Check if any encounters match the chosen criteria
    if filtered_df.empty:
        return "No encounters found for the chosen biome and encounter type."
    
    # Randomly select an encounter from the filtered DataFrame
    random_encounter = filtered_df.sample(n=1)

    # Format the encounter details neatly
    formatted_encounter = format_encounter(random_encounter)
    
    update_encounter_text(formatted_encounter)
    update_encounter_text('\n')
    
    return formatted_encounter

def format_encounter(encounter):
    # Get the columns and values of the encounter
    columns = encounter.columns.tolist()
    values = encounter.values.tolist()[0]

    # Format the columns and values neatly with right justification
    formatted_encounter = '\n'.join([f"{column.rjust(10)}: {str(value).rjust(5)}" for column, value in zip(columns, values)])
    
    return formatted_encounter

def biome_encounter_combiner():
    biome = biome_var.get()
    encounter = encounter_var.get()
    random_encounter = generate_random_encounter(biome, encounter)

##### RESULTS TEXT BOX & CLEAR BUTTON #####
encounter_text_label = Label(window, text="Results:")
encounter_text_label.grid(row=16, column=1, padx=1, pady=1)
encounter_text = Text(window, height=20, width=60)
encounter_text.grid(row=15, column=2, padx=5, pady=5)

# Clear button to clear both the results text box and the calendar
clear_button = Button(window, text="Clear", command=lambda: [clear_encounter_text(), clear_calendar()])
clear_button.grid(row=15, column=3, columnspan=1, padx=1, pady=1)

# SURVIVAL INPUT
survival_label = tk.Label(text="Survival Check:")
survival_label.grid(row=10, column=0, padx=5, pady=5)
survival_var = StringVar(window)
survival_var.set("0-11") 
survival_dropdown = OptionMenu(window, survival_var, *survival_mods.keys())
survival_dropdown.grid(row=10, column=1, padx=5, pady=5)

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
time_of_day_fauna_var = StringVar()
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
biome_label.grid(row=1, column=0, padx=1, pady=5)
biome_var = StringVar(window)
biome_var.set("ATMOSPHERE")  
biome_dropdown = OptionMenu(window, biome_var, *biomes.keys(), command=on_select_change)  # Add command to handle selection change
biome_dropdown.grid(row=1, column=1, padx=1, pady=5)

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
speed_label = Label(window, text="PC Speed:")
speed_label.grid(row=8, column=0, padx=5, pady=5)
speed_var = StringVar(window)
speed_var.set("Normal")
speed_dropdown = OptionMenu(window, speed_var, *speed.keys())
speed_dropdown.grid(row=8, column=1, padx=5, pady=5)

# ATTITUDE LABEL & BUTTON
attitude_label = Label(window, text="PC Attitude:")
attitude_label.grid(row=9, column=0, padx=5, pady=5)
attitude_var = StringVar(window)
attitude_var.set("Neutral")
attitude_dropdown = OptionMenu(window, attitude_var, *attitude.keys())
attitude_dropdown.grid(row=9, column=1, padx=5, pady=5)

# ENCOUNTER LABEL & BUTTON
encounter_label = Label(window, text="Encounter:")
encounter_label.grid(row=11, column=0, padx=5, pady=5)
encounter_var = StringVar(window)
encounter_var.set("TYPICAL")
encounter_dropdown = OptionMenu(window, encounter_var, *encounters)
encounter_dropdown.grid(row=11, column=1, padx=5, pady=5)

##### ENCOUNTER RATING LOGICS #####
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
    selected_survival = survival_var.get()

    survival_mod = survival_mods[selected_survival]
   
    humanoid_er = (
        int(biomes[selected_biome]['humanoid'])
        + int(times_of_day[selected_time_of_day]['humanoid'])
        + int(traffic[selected_traffic])
        + int(survival_mod)
        + int(speed[selected_speed])
        + int(attitude[selected_attitude])
    )
    
    fauna_er = (
        int(biomes[selected_biome]['fauna'])
        + int(times_of_day[selected_time_of_day]['fauna'])
        + int(seasons[selected_season]['fauna'])
        + int(wind[selected_wind])
        + int(survival_mod)
        + int(speed[selected_speed])
        + int(attitude[selected_attitude])
    )
    
    flora_er = (
        int(biomes[selected_biome]['flora'])
        + int(times_of_day[selected_time_of_day]['flora'])
        + int(seasons[selected_season]['flora'])
        + int(temp[selected_temp])
        + int(precipitation[selected_precipitation])
        + int(survival_mod)
        + int(speed[selected_speed])
        + int(attitude[selected_attitude])
    )
    
    update_encounter_text(f"Humanoid ER: {humanoid_er}\n Fauna ER: {fauna_er}\n Flora ER: {flora_er}\n\n")
    
    return humanoid_er, fauna_er, flora_er

def check_encounter_type():
    type_roll = random.randint(1, 100)
    if type_roll <= 60:
        encounter_type = "Humanoid"
    elif type_roll <= 80:
        encounter_type = "Fauna"
    else:
        encounter_type = "Flora"
    update_encounter_text(f"{type_roll}:{encounter_type}:")
    sub_type = get_subtype(encounter_type)
    return sub_type


def get_subtype(encounter_type):
    sub_type_roll = random.randint(1, 100)
    update_encounter_text(f"Sub-Type: {sub_type_roll} ")

    if sub_type_roll <= 75:
        sub_type = encounter_type
    elif sub_type_roll <= 89:
        sub_type = f"Special {encounter_type}"
    else:
        sub_type = f"Dead {encounter_type}"

    update_encounter_text(f"A {sub_type}!\n")
    return sub_type

def roll20():
    return random.randint(1, 20)

def check_for_encounter():
    humanoid_er, fauna_er, flora_er = set_encounter_ratings()
    sub_type = check_encounter_type()
    roll = roll20()
    selected_survival = survival_var.get()
    survival_mod = survival_mods[selected_survival]
    check = survival_mod + roll

    update_encounter_text(f"Survival Mod: {survival_mod} + Roll: {roll} = Survival Total: {check}\n")
    update_encounter_text(f"Checked For: {sub_type}\n")

    encounter_types = {
        "Humanoid": humanoid_er,
        "Special Humanoid": humanoid_er,
        "Dead Humanoid": humanoid_er,
        "Fauna": fauna_er,
        "Special Fauna": fauna_er,
        "Dead Fauna": fauna_er,
        "Flora": flora_er,
        "Special Flora": flora_er,
        "Dead Flora": flora_er
    }

    if sub_type in encounter_types:
        if check < encounter_types[sub_type]:
            update_encounter_text("Encounter!\n")
            return True
        elif check == encounter_types[sub_type]:
            update_encounter_text("Special!\n")
            return True
        else:
            update_encounter_text(f"No {sub_type} Encounter.\n")
            return False

    update_encounter_text("\n")

def combo_check():
    check_for_encounter()
    biome_encounter_combiner()

# Function to generate encounter results
def generate_encounter_results():
    encounter_results = []
    for _ in range(7):  # Simulate 7 days
        day_encounter_results = []
        for time_of_day in times_of_day.keys():
            time_of_day_var.set(time_of_day)  # Set the time_of_day_var for the current check
            encounter_prob = check_for_encounter()
            day_encounter_results.append(encounter_prob)
            if encounter_prob:  # If encounter occurred, log it
                encounter_log.append(f"{_+1}:{time_of_day}")
        encounter_results.append(day_encounter_results)
    return encounter_results


calendar_window = None  # Initialize the calendar window as None initially
boxes = []  # List to store the text boxes for each day
encounter_log = []  # Placeholder for encounter log
encounter_results = []
roll_results = [[0 for _ in range(4)] for _ in range(7)]  # Initialize roll results

# Set the first day of the 30-day span (0 - Monday, 1 - Tuesday, ..., 6 - Sunday)
first_day = 0  # Default value is Monday

def set_first_day(value):
    global first_day
    day_names = calendar.day_name
    mapping = {
        day_names[0]: 0,
        day_names[1]: 1,
        day_names[2]: 2,
        day_names[3]: 3,
        day_names[4]: 4,
        day_names[5]: 5,
        day_names[6]: 6,
    }
    first_day = mapping[value]
    update_calendar()


def open_calendar_window():
    global calendar_window
    if calendar_window is None or not calendar_window.winfo_exists():  # Check if the window is not open
        calendar_window = tk.Tk()
        calendar_window.title("1 Week")
        week_calendar()
    else:
        update_calendar()

def week_calendar():
    global boxes, encounter_results, roll_results
    for i in range(7):
        box_frame = tk.Frame(calendar_window, width=221, height=400)  # Create a frame for each box
        box_frame.grid(row=0, column=i)  # Place all the boxes in the same row

        box = tk.Text(box_frame, width=20, height=40, wrap=tk.WORD)
        box.grid(row=0, column=0, sticky="nsew")  # Use grid instead of pack

        boxes.append(box)

    encounter_results = generate_encounter_results()
    roll_results = [[0 for _ in range(4)] for _ in range(7)]  # Initialize roll results
    update_calendar()


def update_calendar():
    global first_day, boxes, encounter_results, roll_results

    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for i, box in enumerate(boxes):
        text = generate_day_text(i, day_names)
        if i < len(encounter_results):
            text += generate_encounter_info(i)

        update_box_text(box, text)

def generate_day_text(i, day_names):
    day_number = i + 1
    col = (i + first_day) % 7
    day_of_week = day_names[col]
    return f"{day_number} {day_of_week}\n\n"

def generate_encounter_info(i):
  text = ""
  for j, time_of_day in enumerate(["Morning", "Midday", "Evening", "Midnight"]):
    humanoid_er, fauna_er, flora_er = set_encounter_ratings()
    roll = roll20()  # Generate a new roll for each iteration
    encounter_true = check_for_encounter()
    roll_results[i][j] = roll  # Update roll results for each time of day

    encounter_happened = ""
    if encounter_true:
      encounter_happened = generate_random_encounter(biome_var.get(), "TYPICAL")  # Replace with appropriate biome and encounter type

    text += f"{time_of_day}:\n"
    text += f"ER Humanoid: {humanoid_er}\n"
    text += f"ER Fauna: {fauna_er}\n"
    text += f"ER Flora: {flora_er}\n"
    text += f"Roll: {roll}\n"
    text += f"Encounter: {encounter_true}\n"
    text += f"Encounter happened: {encounter_happened}\n\n"

  return text

def update_box_text(box, text):
    box.config(state=tk.NORMAL)
    box.delete(1.0, tk.END)
    box.insert(tk.END, text)
    box.config(state=tk.DISABLED)
    if not box.yview():
        y_scrollbar = tk.Scrollbar(box, orient=tk.VERTICAL, command=box.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        box.config(yscrollcommand=y_scrollbar.set)
        box.config(font=("Arial", 6))  # Set font size

def save_encounter_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            for i, day in enumerate(encounter_results):
                f.write(f"Day {i+1}:\n")
                for j, time_of_day in enumerate(["Morning", "Midday", "Evening", "Midnight"]):
                    if day[j]:
                        f.write(f"{time_of_day}: Encounter\n")
                    else:
                        f.write(f"{time_of_day}: No Encounter\n")
                f.write("\n")

##### RESULTS BUTTONS #####
set_encounter_ratings_button = Button(window, text="See Encounter Ratings", command=set_encounter_ratings)
set_encounter_ratings_button.grid(row=12, column=0, columnspan=1, padx=1, pady=1)

combo_check_button = Button(window, text="Combo", command=combo_check)
combo_check_button.grid(row=12, column=1, columnspan=1, padx=1, pady=1)

check_encounter_type_button = Button(window, text="Check Encounter Type", command=check_encounter_type)
check_encounter_type_button.grid(row=13, column=0, columnspan=1, padx=1, pady=1)

check_for_encounter_button = Button(window, text="Check For Encounter", command=check_for_encounter)
check_for_encounter_button.grid(row=13, column=1, columnspan=1, padx=1, pady=1)

encounter_and_biome = Button(window, text="Encounter&Biome", command=biome_encounter_combiner)
encounter_and_biome.grid(row=15, column=0, columnspan=1, padx=1, pady=1)

calendar_button = Button(window, text="Calendar", command=open_calendar_window)
calendar_button.grid(row=15, column=1, columnspan=1, padx=1, pady=1)

# Add a button to save encounter results
save_button = Button(window, text="Save Results", command=save_encounter_results)
save_button.grid(row=14, column=0, columnspan=1, padx=1, pady=1)

# Clear button to clear both the results text box and the calendar
clear_button = Button(window, text="Clear", command=lambda: [clear_encounter_text(), clear_calendar()])
clear_button.grid(row=15, column=3, columnspan=1, padx=1, pady=1)

update_image(biome_var.get())


window.mainloop()
