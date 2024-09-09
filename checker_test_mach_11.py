import random
import os
import tkinter as tk
from tkinter import StringVar, OptionMenu, Text, Label, Button, messagebox, filedialog, Scrollbar
from PIL import ImageTk, Image
import pandas as pd
import calendar

class RandomEncounterCalculator:
    def __init__(self, master):
        self.window = master
        self.window.title("Random Encounter Calculator")

        # CORE DICTIONARIES
        self.biomes = {
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

        self.times_of_day = {
            'Morning': {'humanoid': 4, 'fauna': 1, 'flora': 2},
            'Midday': {'humanoid': 3, 'fauna': 2, 'flora': 4},
            'Evening': {'humanoid': 2, 'fauna': 3, 'flora': 3},
            'Midnight': {'humanoid': 1, 'fauna': 4, 'flora': 1}
        }

        self.seasons = {
            'Spring': {'humanoid': 3, 'fauna': 3, 'flora': 4},
            'Summer': {'humanoid': 4, 'fauna': 1, 'flora': 3},
            'Fall': {'humanoid': 2, 'fauna': 4, 'flora': 2},
            'Winter': {'humanoid': 1, 'fauna': 2, 'flora': 1}
        }

        self.traffic = {
            'Barren': -2,
            'Sparse': -1,
            'Populated': 1,
            'Busy': 2
        }

        self.temp = {
            'Cold': -2,
            'Hot': -1,
            'Cool': 0,
            'Warm': 2,
            'Mild': 3
        }

        self.wind = {
            'Strong': 0,
            'None': 1,
            'Light': 3
        }

        self.precipitation = {
            'Wet': 0,
            'Normal': 1,
            'Dry': 2
        }

        self.speed = {
            'Quick': 3,
            'Normal': 0,
            'Cautious': -3
        }

        self.attitude = {
            'Hostile': 3,
            'Neutral': 0,
            'Friendly': -3
        }

        self.survival_mods = {
            "0-11": 0,
            "12-14": 1,
            "15-17": 2,
            "18-20": 3,
            "21-24": 4,
            "25+": 5
        }

        self.encounters = [
            "TYPICAL",
            "HUMANOID",
            "FAUNA",
            "FLORA"
        ]

        self.base_path = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'code', 'helper', 'src_game', 'Entities', 'pop', 'Random_Encounters')

        # UI VARIABLES
        self.biome_var = StringVar(self.window)
        self.biome_var.set("ATMOSPHERE")

        self.season_var = StringVar(self.window)
        self.season_var.set("Winter")

        self.time_of_day_var = StringVar(self.window)
        self.time_of_day_var.set("Morning")

        self.traffic_var = StringVar(self.window)
        self.traffic_var.set("Barren")

        self.temp_var = StringVar(self.window)
        self.temp_var.set("Cold")

        self.wind_var = StringVar(self.window)
        self.wind_var.set("Strong")

        self.precipitation_var = StringVar(self.window)
        self.precipitation_var.set("Wet")

        self.speed_var = StringVar(self.window)
        self.speed_var.set("Normal")

        self.attitude_var = StringVar(self.window)
        self.attitude_var.set("Neutral")

        self.survival_var = StringVar(self.window)
        self.survival_var.set("0-11")

        self.encounter_var = StringVar(self.window)
        self.encounter_var.set("TYPICAL")

        self.stored_encounter_ratings = None
        self.calendar_window = None
        self.boxes = []
        self.encounter_log = []
        self.encounter_results = []
        self.roll_results = [[0 for _ in range(4)] for _ in range(7)]
        self.first_day = 0  # Default value is Monday

        # Set up the GUI
        self.setup_ui()

    def setup_ui(self):

        self.image_label = Label(self.window)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1) 
        self.update_image(self.biome_var.get())

        # BIOME LABEL & BUTTON
        Label(self.window, text="Biome:").grid(row=1, column=0, padx=1, pady=5)
        OptionMenu(self.window, self.biome_var, *self.biomes.keys(), command=self.on_select_change).grid(row=1, column=1, padx=1, pady=5)

        # SEASON LABEL & BUTTON
        Label(self.window, text="Season:").grid(row=2, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.season_var, *self.seasons.keys()).grid(row=2, column=1, padx=5, pady=5)

        # TIME OF DAY LABEL & BUTTON
        Label(self.window, text="Time of Day:").grid(row=3, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.time_of_day_var, *self.times_of_day.keys()).grid(row=3, column=1, padx=5, pady=5)

        # TRAFFIC LABEL & BUTTON
        Label(self.window, text="Traffic:").grid(row=4, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.traffic_var, *self.traffic.keys()).grid(row=4, column=1, padx=5, pady=5)

        # TEMPERATURE LABEL & BUTTON
        Label(self.window, text="Temperature:").grid(row=5, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.temp_var, *self.temp.keys()).grid(row=5, column=1, padx=5, pady=5)

        # WIND LABEL & BUTTON
        Label(self.window, text="Wind:").grid(row=6, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.wind_var, *self.wind.keys()).grid(row=6, column=1, padx=5, pady=5)

        # PRECIPITATION LABEL & BUTTON
        Label(self.window, text="Precipitation:").grid(row=7, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.precipitation_var, *self.precipitation.keys()).grid(row=7, column=1, padx=5, pady=5)

        # SPEED LABEL & BUTTON
        Label(self.window, text="PC Speed:").grid(row=8, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.speed_var, *self.speed.keys()).grid(row=8, column=1, padx=5, pady=5)

        # ATTITUDE LABEL & BUTTON
        Label(self.window, text="PC Attitude:").grid(row=9, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.attitude_var, *self.attitude.keys()).grid(row=9, column=1, padx=5, pady=5)

        # SURVIVAL LABEL & BUTTON
        Label(self.window, text="Survival Check:").grid(row=10, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.survival_var, *self.survival_mods.keys()).grid(row=10, column=1, padx=5, pady=5)

        # ENCOUNTER LABEL & BUTTON
        Label(self.window, text="Encounter:").grid(row=11, column=0, padx=5, pady=5)
        OptionMenu(self.window, self.encounter_var, *self.encounters).grid(row=11, column=1, padx=5, pady=5)

        # RESULTS BUTTONS
        Button(self.window, text="See Encounter Ratings", command=self.set_encounter_ratings).grid(row=12, column=0, columnspan=1, padx=1, pady=1)
        Button(self.window, text="Combo", command=self.combo_check).grid(row=12, column=1, columnspan=1, padx=1, pady=1)

        Button(
            self.window,
            text="Check Encounter Type",
            command=lambda: self.check_encounter_type(*self.set_encounter_ratings())
        ).grid(row=13, column=0, columnspan=1, padx=1, pady=1)

        Button(
            self.window,
            text="Check For Encounter",
            command=lambda: self.check_for_encounter(*self.set_encounter_ratings())
        ).grid(row=13, column=1, columnspan=1, padx=1, pady=1)

        # RESULTS TEXT BOX & CLEAR BUTTON
        self.encounter_text = Text(self.window, height=16, width=60)
        self.encounter_text.grid(row=15, column=2, padx=5, pady=5)

        # Clear button to clear both the results text box and the calendar
        Button(self.window, text="Clear", command=self.clear_all).grid(row=15, column=4, columnspan=1, padx=1, pady=1)

        Button(self.window, text="Calendar", command=self.open_calendar_window).grid(row=15, column=1, columnspan=1, padx=1, pady=1)

        # Add a button to save encounter results
        Button(self.window, text="Save Results", command=self.save_encounter_results).grid(row=14, column=0, columnspan=1, padx=1, pady=1)

        # Adding a Scroll Bar to the Encounter Text Box
        scrollbar = Scrollbar(self.window)
        scrollbar.grid(row=15, column=3, sticky='ns')
        self.encounter_text = Text(self.window, height=20, width=60, yscrollcommand=scrollbar.set)
        self.encounter_text.grid(row=15, column=2, padx=5, pady=5)
        scrollbar.config(command=self.encounter_text.yview)

        

    def update_image(self, biome):
        image_path = os.path.join(self.base_path, 'All_Biome_Images', f"{biome.upper()}.png")
        try:
            image = Image.open(image_path)
            image = image.resize((800, 800), Image.BICUBIC)
            tk_image = ImageTk.PhotoImage(image)
            self.image_label.configure(image=tk_image)
            self.image_label.image = tk_image
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image file not found: {image_path}")

    def on_select_change(self, event):
        self.update_image(self.biome_var.get())

    def set_encounter_ratings(self):
        self.stored_encounter_ratings = None
        selected_biome = self.biome_var.get()
        selected_time_of_day = self.time_of_day_var.get()
        selected_season = self.season_var.get()
        selected_traffic = self.traffic_var.get()
        selected_temp = self.temp_var.get()
        selected_wind = self.wind_var.get()
        selected_precipitation = self.precipitation_var.get()
        selected_speed = self.speed_var.get()
        selected_attitude = self.attitude_var.get()
        selected_survival = self.survival_var.get()

        survival_mod = self.survival_mods[selected_survival]

        humanoid_er = sum([
            self.biomes[selected_biome]['humanoid'],
            self.times_of_day[selected_time_of_day]['humanoid'],
            self.seasons[selected_season]['humanoid'],
            self.traffic[selected_traffic],
            survival_mod,
            self.speed[selected_speed],
            self.attitude[selected_attitude]
        ])

        fauna_er = sum([
            self.biomes[selected_biome]['fauna'],
            self.times_of_day[selected_time_of_day]['fauna'],
            self.seasons[selected_season]['fauna'],
            self.wind[selected_wind],
            survival_mod,
            self.speed[selected_speed],
            self.attitude[selected_attitude]
        ])

        flora_er = sum([
            self.biomes[selected_biome]['flora'],
            self.times_of_day[selected_time_of_day]['flora'],
            self.seasons[selected_season]['flora'],
            self.temp[selected_temp],
            self.precipitation[selected_precipitation],
            survival_mod,
            self.speed[selected_speed],
            self.attitude[selected_attitude]
        ])

        typical_er = int((humanoid_er + fauna_er + flora_er) / 3)
        total_rating = humanoid_er + fauna_er + flora_er + typical_er

        self.update_encounter_text(
            f"Humanoid ER: {humanoid_er}\n"
            f"Fauna ER: {fauna_er}\n"
            f"Flora ER: {flora_er}\n"
            f"Typical ER: {typical_er}\n"
            f"Total Rating: {total_rating}\n\n"
        )

        self.stored_encounter_ratings = (humanoid_er, fauna_er, flora_er, typical_er, total_rating)
        return humanoid_er, fauna_er, flora_er, typical_er, total_rating

    def check_encounter_type(self, humanoid_er, fauna_er, flora_er, typical_er, total_rating):
        type_roll = random.random()  # Generate a random number between 0 and 1
        type_roll = round(type_roll, 3)  # Round to the nearest thousandth
        encounter_type = ""
        sub_type = ""

        # Weighted probabilities
        probabilities = [
            (humanoid_er / total_rating, "HUMANOID"),
            (fauna_er / total_rating, "FAUNA"),
            (flora_er / total_rating, "FLORA"),
            (typical_er / total_rating, "TYPICAL")
        ]

        cumulative_probability = 0
        for i, (weight, encounter) in enumerate(probabilities):
            cumulative_probability += weight
            if type_roll < cumulative_probability:
                encounter_type = encounter
                break

        sub_type_roll = random.randint(1, 100)
        if sub_type_roll <= 75:
            sub_type = encounter_type
        elif sub_type_roll <= 89:
            sub_type = f"Special {encounter_type}"  # Ensure correct formatting
        else:
            sub_type = f"Dead {encounter_type}"  # Ensure correct formatting

        self.update_encounter_text(f"{type_roll}% {encounter_type}:{sub_type}\n")
        return sub_type, encounter_type

    def roll20(self):
        return random.randint(1, 20)

    def check_for_encounter(self, humanoid_er, fauna_er, flora_er, typical_er, total_rating):
        # Determine encounter type and roll
        sub_type, encounter_type = self.check_encounter_type(humanoid_er, fauna_er, flora_er, typical_er, total_rating)
        roll = self.roll20()
        selected_survival = self.survival_var.get()
        survival_mod = self.survival_mods[selected_survival]
        check = survival_mod + roll

        # Get encounter rating for the determined subtype
        encounter_rating = {
            "HUMANOID": humanoid_er,
            "Special HUMANOID": humanoid_er,
            "Dead HUMANOID": humanoid_er,
            "FAUNA": fauna_er,
            "Special FAUNA": fauna_er,
            "Dead FAUNA": fauna_er,
            "FLORA": flora_er,
            "Special FLORA": flora_er,
            "Dead FLORA": flora_er,
            "TYPICAL": typical_er, 
            "Special TYPICAL": typical_er, 
            "Dead TYPICAL": typical_er   
        }

        # Determine if an encounter happens
        encounter_happened = check <= encounter_rating[sub_type]  # Access the correct ER from the dictionary

        # Log whether an encounter happened and the roll details
        self.update_encounter_text(f"Encounter Happened: {encounter_happened} | Roll: {roll} | Type: {encounter_type}\n")

        # If an encounter happens, generate and log the encounter
        if encounter_happened:
            # Generate the encounter based on the biome and encounter type
            biome = self.biome_var.get()  # Get the currently selected biome
            encounter_details = self.generate_random_encounter(biome, encounter_type)
            
            # Log the encounter details
            self.update_encounter_text(f"Encounter Details: {encounter_details}\n")

        return encounter_happened, roll, encounter_type


    def combo_check(self):
        humanoid_er, fauna_er, flora_er, typical_er, total_rating = self.set_encounter_ratings()
        encounter_happened, roll, encounter_type = self.check_for_encounter(humanoid_er, fauna_er, flora_er, typical_er, total_rating)
        self.update_encounter_text(f"Encounter Type: {encounter_type}\n")
        self.update_encounter_text(f"Roll: {roll}\n")
        self.update_encounter_text(f"Encounter Happened: {'Yes' if encounter_happened else 'No'}\n")
        self.generate_random_encounter(self.biome_var.get(), encounter_type)

    def generate_random_encounter(self, biome, encounter_type):
        excel_file_path = os.path.join(self.base_path, 'Master_Biome_Encounter_Lists.xlsx')
        try:
            df = pd.read_excel(excel_file_path)
            filtered_df = df[(df['Biome'] == biome) & (df['Encounter'] == encounter_type)]

            if filtered_df.empty:
                return "No encounters found for the chosen biome and encounter type."

            random_encounter = filtered_df.sample(n=1)
            formatted_encounter = self.format_encounter(random_encounter)

            self.update_encounter_text(formatted_encounter)
            self.update_encounter_text('\n')

            return formatted_encounter
        except FileNotFoundError:
            messagebox.showerror("Error", f"Excel file not found: {excel_file_path}")
            return "Error: Excel file not found."

    def format_encounter(self, encounter):
        columns = encounter.columns.tolist()
        values = encounter.values.tolist()[0]

        formatted_encounter = '\n'.join([f"{column.rjust(5)}: {str(value).rjust(5)}" for column, value in zip(columns, values)])
        return formatted_encounter

    def clear_all(self):
        self.encounter_text.delete('1.0', tk.END)
        for box in self.boxes:
            box.config(text="")

    def open_calendar_window(self):
        if self.calendar_window is None or not self.calendar_window.winfo_exists():
            self.calendar_window = tk.Tk()
            self.calendar_window.title("1 Week")
            self.calendar_window.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.week_calendar()

    def week_calendar(self):
        for widget in self.boxes:
            widget.destroy()

        self.boxes.clear()
        for _ in range(7):
            box_frame = tk.Frame(self.calendar_window, width=222, height=400)
            box_frame.grid(row=0, column=len(self.boxes))

            box = Text(box_frame, width=22, height=60, wrap=tk.WORD)
            box.grid(row=0, column=0, sticky="nsew")
            self.boxes.append(box)

        self.encounter_results = self.generate_week_results()
        self.roll_results = [[0 for _ in range(4)] for _ in range(7)]
        self.update_calendar(self.encounter_results)

    def update_calendar(self, encounter_results):
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        time_of_day = ["Morning", "Midday", "Evening", "Midnight"]

        for i, box in enumerate(self.boxes):
            day_number = i + 1
            day_of_week = day_names[(i + self.first_day) % 7]
            text = f"{day_number} {day_of_week}\n\n"

            if i < len(encounter_results):
                for j, (encounter_prob, roll, encounter_type, humanoid_er, fauna_er, flora_er, typical_er, total_rating) in enumerate(encounter_results[i]):
                    self.roll_results[i][j] = roll
                    encounter_happened = "True" if encounter_prob else "False"
                    text += f"{time_of_day[j]}:\n"
                    text += f"ER Humanoid: {humanoid_er}\n"
                    text += f"ER Fauna: {fauna_er}\n"
                    text += f"ER Flora: {flora_er}\n"
                    text += f"ER Typical: {typical_er}\n"
                    text += F"Total ER: {total_rating}\n"
                    text += f"Encounter happened: {encounter_happened} (Roll: {roll})\n"
                    text += f"Encounter Type: {encounter_type}\n\n"

            self.update_box_text(box, text)

    def update_box_text(self, box, text):
        box.config(state=tk.NORMAL)
        box.delete(1.0, tk.END)
        box.insert(tk.END, text)
        box.config(state=tk.DISABLED)
        box.config(font=("Arial", 10))
        if not box.yview():
            y_scrollbar = tk.Scrollbar(box, orient=tk.VERTICAL, command=box.yview)
            y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            box.config(yscrollcommand=y_scrollbar.set)

    def generate_week_results(self):
        encounter_results = []
        for day in range(7):
            day_results = []
            for time_of_day in ["Morning", "Midday", "Evening", "Midnight"]:
                self.time_of_day_var.set(time_of_day)
                humanoid_er, fauna_er, flora_er, typical_er, total_rating = self.set_encounter_ratings()
                encounter_prob, roll, encounter_type = self.check_for_encounter(humanoid_er, fauna_er, flora_er, typical_er, total_rating)
                day_results.append((encounter_prob, roll, encounter_type, humanoid_er, fauna_er, flora_er, typical_er, total_rating))
                if encounter_prob:
                    self.encounter_log.append(f"Day {day + 1}: {time_of_day}")
            encounter_results.append(day_results)
        return encounter_results

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to close the calendar?"):
            if self.calendar_window:
                self.calendar_window.destroy()
            self.calendar_window = None
            self.boxes.clear()

    def save_encounter_results(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for i, day in enumerate(self.encounter_results):
                    f.write(f"Day {i + 1}:\n")
                    for j, time_of_day in enumerate(["Morning", "Midday", "Evening", "Midnight"]):
                        encounter_prob = day[j][0]
                        roll = day[j][1]
                        f.write(f"{time_of_day}: {'Encounter' if encounter_prob else 'No Encounter'} (Roll: {roll})\n")
                    f.write("\n")

    def update_encounter_text(self, text):
        self.encounter_text.insert(tk.END, text)

def main():
    root = tk.Tk()
    app = RandomEncounterCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
