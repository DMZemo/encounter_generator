import random
import tkinter as tk
from tkinter import ttk, StringVar, OptionMenu, Label, Button, Text, Entry

biomes = {
    'Atmosphere': {                 "humanoid": 0,  "fauna": 0, "flora": 0},
    'Marine': {                     "humanoid": 1,  "fauna": 5, "flora": 2},
    'Glacier': {                    "humanoid": 2,  "fauna": 1, "flora": 1},
    'Tundra': {                     "humanoid": 3,  "fauna": 4, "flora": 5},
    'Taiga': {                      "humanoid": 4,  "fauna": 6, "flora": 6},
    'Cold Desert': {                "humanoid": 5,  "fauna": 3, "flora": 3},
    'Hot Desert': {                 "humanoid": 6,  "fauna": 2, "flora": 4},
    'Tropical Rainforest': {        "humanoid": 7,  "fauna": 13,"flora": 13},
    'Wetland': {                    "humanoid": 8,  "fauna": 7, "flora": 8},
    'Tropical Seasonal Forest': {   "humanoid": 9,  "fauna": 12,"flora": 7},
    'Savanna': {                    "humanoid": 10, "fauna": 9, "flora": 10},
    'Grassland': {                  "humanoid": 11, "fauna": 8, "flora": 9},
    'Temperate Deciduous Forest': { "humanoid": 12, "fauna": 10,"flora": 12},
    'Temperate Rainforest': {       "humanoid": 13, "fauna": 11,"flora": 11}
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

humanoid_er = ()
fauna_er = ()
flora_er = ()
encounter_type = ()
sub_type = ()
survival = ()
survival_mod = ()

window = tk.Tk()
window.title("Encounter Calculator")

# Define a function to get the input as an int
def survival_mod_calc():
    try:
        survival_check = int(survival.get())
        if survival_check <= 11:
            survival_mod = 1
        elif 12 <= survival_check <= 14:
            survival_mod = 1.33
        elif 15 <= survival_check <= 17:
            survival_mod = 1.66
        elif 18 <= survival_check <= 20:
            survival_mod = 2
        elif 21 <= survival_check <= 24:
            survival_mod = 2.33
        elif 25 <= survival_check < 40:
            survival_mod = 2.66
        return survival_mod
    except ValueError:
        print("Invalid input, must be an integer")
        return None
    
def get_survival_mod():
    global survival_mod
    survival_mod = survival_mod_calc()

survival_var = StringVar()
# Create a label and entry box
survival_label = tk.Label(text="Survival Check:")
survival_label.grid(row=0, column=3, padx=5, pady=5)

survival = tk.Entry(window, width=5) 
survival.grid(row=0, column=4, padx=5, pady=5)
survival_mod = survival_mod_calc()


biome_var = StringVar()
biome_humanoid_var = StringVar()
biome_fauna_var = StringVar()
biome_flora_var = StringVar()

season_var = StringVar()
season_humanoid_var = StringVar()
season_fauna_var = StringVar()
season_flora_var = StringVar()

time_of_day_var = StringVar()
time_of_day_humanoid_var = StringVar()
time_of_day_fauna_var = StringVar
time_of_day_flora_var = StringVar()

traffic_var = StringVar()
temp_var = StringVar()
wind_var = StringVar()
precipitation_var = StringVar()
speed_var = StringVar()
attitude_var = StringVar()

biome_label = Label(window, text="Biome:")
biome_label.grid(row=0, column=0, padx=5, pady=5)
biome_var = StringVar(window)
biome_var.set("Atmosphere")  
biome_dropdown = OptionMenu(window, biome_var, *biomes.keys())
biome_dropdown.grid(row=0, column=1, padx=5, pady=5)

time_of_day_label = Label(window, text="Time of Day:")
time_of_day_label.grid(row=3, column=0, padx=5, pady=5)
time_of_day_var = StringVar(window)
time_of_day_var.set("Morning") 
time_of_day_dropdown = OptionMenu(window, time_of_day_var, *times_of_day.keys())
time_of_day_dropdown.grid(row=3, column=1, padx=5, pady=5)

season_label = Label(window, text="Season:")
season_label.grid(row=2, column=0, padx=5, pady=5)
season_var = StringVar(window)
season_var.set("Winter")
season_dropdown = OptionMenu(window, season_var, *seasons.keys())
season_dropdown.grid(row=2, column=1, padx=5, pady=5)

traffic_label = Label(window, text="Traffic:")
traffic_label.grid(row=1, column=0, padx=5, pady=5)
traffic_var = StringVar(window)
traffic_var.set("Barren")
traffic_dropdown = OptionMenu(window, traffic_var, *traffic.keys())
traffic_dropdown.grid(row=1, column=1, padx=5, pady=5)

temp_label = Label(window, text="Temperature:")
temp_label.grid(row=4, column=0, padx=5, pady=5)
temp_var = StringVar(window)
temp_var.set("Cold")
temp_dropdown = OptionMenu(window, temp_var, *temp.keys())
temp_dropdown.grid(row=4, column=1, padx=5, pady=5)

wind_label = Label(window, text="Wind:")
wind_label.grid(row=5, column=0, padx=5, pady=5)
wind_var = StringVar(window)
wind_var.set("Strong")
wind_dropdown = OptionMenu(window, wind_var, *wind.keys())
wind_dropdown.grid(row=5, column=1, padx=5, pady=5)

precipitation_label = Label(window, text="Precipitation:")
precipitation_label.grid(row=6, column=0, padx=5, pady=5)
precipitation_var = StringVar(window)
precipitation_var.set("Wet")
precipitation_dropdown = OptionMenu(window, precipitation_var, *precipitation.keys())
precipitation_dropdown.grid(row=6, column=1, padx=5, pady=5)

speed_label = Label(window, text="Speed:")
speed_label.grid(row=7, column=0, padx=5, pady=5)
speed_var = StringVar(window)
speed_var.set("Normal")
speed_dropdown = OptionMenu(window, speed_var, *speed.keys())
speed_dropdown.grid(row=7, column=1, padx=5, pady=5)

attitude_label = Label(window, text="Attitude:")
attitude_label.grid(row=8, column=0, padx=5, pady=5)
attitude_var = StringVar(window)
attitude_var.set("Neutral")
attitude_dropdown = OptionMenu(window, attitude_var, *attitude.keys())
attitude_dropdown.grid(row=8, column=1, padx=5, pady=5)

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
    
    update_encounter_text(f"Humanoid ER: {humanoid_er}\nFauna ER: {fauna_er}\nFlora ER: {flora_er}\n")
    return humanoid_er, fauna_er, flora_er
    
def update_encounter_text(text):
    encounter_text.insert(tk.END, text)

def clear_encounter_text():
    encounter_text.delete('1.0', tk.END)

def check_encounter_type():
    type_roll = random.randint(1,100)
    update_encounter_text(f"Type Roll:{type_roll}\n")

    if type_roll <= 60:
        encounter_type = "Humanoid"
        update_encounter_text("Checking for Humanoid: \n")
    elif 60 < type_roll <= 80:
        encounter_type = "Fauna"
        update_encounter_text("Checking for Fauna: \n")
    elif type_roll >= 81:
        encounter_type = "Flora"
        update_encounter_text("Checking for Flora: \n")

    sub_type_roll = random.randint(1,100)

    if encounter_type == "Humanoid":
        update_encounter_text(f"Humanoid Encounter Sub-Type: {sub_type_roll}\n")
        if sub_type_roll <= 75:
            sub_type = "Humanoid"
            update_encounter_text("Humanoid! \n")
            return sub_type
        elif 75 < sub_type_roll <= 89:
            sub_type = "Humanoid Event"
            update_encounter_text("Humanoid Event! \n")
            return sub_type
        elif sub_type_roll >= 90:
            sub_type = "Humanoid Corpse"
            update_encounter_text("Humanoid Corpse! \n")
            return sub_type

    if encounter_type == "Fauna":
        update_encounter_text(f"Fauna Encounter Sub-Type: {sub_type_roll}\n")
        if sub_type_roll <= 75:
            sub_type = "Fauna"
            update_encounter_text(f"Fauna! \n")
            return sub_type
        elif 75 < sub_type_roll <= 89:
            sub_type = "Mega Fauna"
            update_encounter_text(f"Mega Fauna! \n")
            return sub_type
        elif sub_type_roll >= 90:
            sub_type = "Apex Predator"
            update_encounter_text(f"Apex Predator! \n")
            return sub_type

    if encounter_type == "Flora":
        update_encounter_text(f"Flora Encounter Sub-Type: {sub_type_roll}\n")
        if sub_type_roll <= 75:
            sub_type = "Flora"
            update_encounter_text(f"Flora! \n")
            return sub_type
        elif 75 < sub_type_roll <= 89:
            sub_type = "Mega Flora"
            update_encounter_text(f"Mega Flora! \n")
            return sub_type
        elif sub_type_roll >= 90:
            sub_type = "Magic Font"
            update_encounter_text(f"Magic Font! \n")
            return sub_type
    else: pass



    def humanoid_rating(humanoid_total):
        update_encounter_text(f"Humanoid Rating: {humanoid_total}\n")
        roll_result1 = random.randint(1, 20)
        update_encounter_text(f"Humanoid Check: {roll_result1}\n")
    
        if roll_result1 > humanoid_rating: 
            update_encounter_text("Uneventful...\n")
        elif roll_result1 == humanoid_rating:
            update_encounter_text("Special!\n")
        else:
            update_encounter_text("Encounter!\n")
        update_encounter_text("\n")

    def fauna_rating(fauna_total):
        update_encounter_text(f"Fauna Rating: {fauna_total}\n")
        roll_result2 = random.randint(1, 20)
        update_encounter_text(f"Fauna Check: {roll_result2}\n")

        if roll_result2 > fauna_rating: 
            update_encounter_text("Uneventful... \n")
        elif roll_result2 == fauna_rating:
            update_encounter_text("Special! \n")
        else:
            update_encounter_text("Encounter! \n")
        update_encounter_text("\n")

    def flora_rating(flora_total):
        update_encounter_text(f"Flora Rating: {flora_total}\n")
        roll_result3 = random.randint(1, 20)
        update_encounter_text(f"Flora Check: {roll_result3}\n")

        if roll_result3 > flora_rating:
            update_encounter_text("Uneventful... \n")
        elif roll_result3 == flora_rating:
            update_encounter_text("Special! \n")
        else:
            update_encounter_text("Encounter! \n")
        update_encounter_text("\n")

def roll20():
    roll = random.randint(1,20)
    return roll

#### sub_type: Humanoid, Humanoid Event, Humanoid Corpse, Fauna, Mega Fauna, Apex Predator, Flora, Mega Flora, Magic Font

def does_encounter():
    check_for_encounter = check_for_encounter()
    if check_for_encounter() == True:
        update_encounter_text(f"!!!SOMETHING IS ENCOUNTERED!!!")
    elif check_for_encounter() == False:
        update_encounter_text(f"...nothing interesting happens...")

def check_for_encounter():
    humanoid_er, fauna_er, flora_er = set_encounter_ratings()
    sub_type = check_encounter_type()
    check = roll20()
    survival_mod = survival_mod_calc()

    update_encounter_text(f"\n")
    update_encounter_text(f"Survival Mod: {survival_mod}\n")
    update_encounter_text(f"Humanoid ER:{humanoid_er}, Fauna ER:{fauna_er}, Flora ER:{flora_er}\n")
    update_encounter_text(f"Encounter Checked For:{sub_type}\n")
    update_encounter_text(f"Roll:{check}\n")
    does_encounter
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
    


calculate_button = ttk.Button(window, text="Set Encounter Ratings", command=set_encounter_ratings)
calculate_button.grid(row=10, column=0, columnspan=1, padx=0, pady=0)

check_encounter_type_button = Button(window, text="Check Encounter Type", command= check_encounter_type)
check_encounter_type_button.grid(row=11, column=0, columnspan=1, padx=0, pady=0)

check_for_encounter_button = Button(window, text="Check For Encounter", command= check_for_encounter)
check_for_encounter_button.grid(row=12, column=0, columnspan=1, padx=0, pady=0)

encounter_text_label = Label(window, text="Results:")
encounter_text_label.grid(row=13, column=0, padx=10, pady=10)
encounter_text = Text(window, height=15, width=50)
encounter_text.grid(row=14, column=0, padx=10, pady=10)

clear_button = Button(window, text="Clear", command=clear_encounter_text)
clear_button.grid(row=12, column=1, columnspan=1, padx=10, pady=5)

update_encounter_text(f"\n")

window.mainloop()