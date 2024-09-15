import random
import os
import tkinter as tk
from tkinter import StringVar, OptionMenu, Text, Label, Button, messagebox, filedialog, Scrollbar
from PIL import ImageTk, Image
import pandas as pd


# Modular data definitions for encounters
class EncounterData:
    @staticmethod
    def get_biomes():
        return {
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

    @staticmethod
    def get_times_of_day():
        return {
            'Morning': {'humanoid': 4, 'fauna': 1, 'flora': 2},
            'Midday': {'humanoid': 3, 'fauna': 2, 'flora': 4},
            'Evening': {'humanoid': 2, 'fauna': 3, 'flora': 3},
            'Midnight': {'humanoid': 1, 'fauna': 4, 'flora': 1}
        }

    @staticmethod
    def get_seasons():
        return {
            'Spring': {'humanoid': 3, 'fauna': 3, 'flora': 4},
            'Summer': {'humanoid': 4, 'fauna': 1, 'flora': 3},
            'Fall': {'humanoid': 2, 'fauna': 4, 'flora': 2},
            'Winter': {'humanoid': 1, 'fauna': 2, 'flora': 1}
        }

    @staticmethod
    def get_traffic():
        return {
            'Barren': -2,
            'Sparse': -1,
            'Populated': 1,
            'Busy': 2
        }

    @staticmethod
    def get_temp():
        return {
            'Cold': -2,
            'Hot': -1,
            'Cool': 0,
            'Warm': 2,
            'Mild': 3
        }

    @staticmethod
    def get_wind():
        return {
            'Strong': 0,
            'None': 1,
            'Light': 3
        }

    @staticmethod
    def get_precipitation():
        return {
            'Wet': 0,
            'Normal': 1,
            'Dry': 2
        }

    @staticmethod
    def get_speed():
        return {
            'Quick': 3,
            'Normal': 0,
            'Cautious': -3
        }

    @staticmethod
    def get_attitude():
        return {
            'Hostile': 3,
            'Neutral': 0,
            'Friendly': -3
        }

    @staticmethod
    def get_survival_mods():
        return {
            "0-11": 0,
            "12-14": 1,
            "15-17": 2,
            "18-20": 3,
            "21-24": 4,
            "25+": 5
        }

    @staticmethod
    def get_encounters():
        return [
            "TYPICAL",
            "HUMANOID",
            "FAUNA",
            "FLORA"
        ]


# Generic Entity Class for Encounters
class EncounterEntity:
    def __init__(self, name, humanoid, fauna, flora):
        self.name = name
        self.humanoid = humanoid
        self.fauna = fauna
        self.flora = flora

    @classmethod
    def from_dict(cls, name, data):
        return cls(name, data['humanoid'], data['fauna'], data['flora'])


# Encounter Calculator class
class EncounterCalculator:
    def __init__(self, biome, season, time_of_day, traffic, temp, wind, precipitation, speed, attitude, survival):
        self.biome = biome
        self.season = season
        self.time_of_day = time_of_day
        self.traffic = traffic
        self.temp = temp
        self.wind = wind
        self.precipitation = precipitation
        self.speed = speed
        self.attitude = attitude
        self.survival = survival

    def calculate_ratings(self):
        ratings = {}
        for encounter_type in ["humanoid", "fauna", "flora"]:
            ratings[encounter_type] = sum([
                getattr(self.biome, encounter_type),
                getattr(self.time_of_day, encounter_type),
                getattr(self.season, encounter_type),
                self.traffic,
                self.temp,
                self.wind,
                self.precipitation,
                self.speed,
                self.attitude,
                self.survival
            ])
        ratings["typical"] = int(sum(ratings.values()) / 3)
        ratings["total"] = sum(ratings.values())
        return ratings


# Random Encounter Calculator UI Class
class RandomEncounterCalculatorUI:
    def __init__(self, master):
        self.window = master
        self.window.title("Random Encounter Calculator")

        self.base_path = self.get_base_path()
        self.encounter_data = EncounterData()

        self.biomes = {name: EncounterEntity.from_dict(name, data) for name, data in self.encounter_data.get_biomes().items()}
        self.seasons = {name: EncounterEntity.from_dict(name, data) for name, data in self.encounter_data.get_seasons().items()}
        self.times_of_day = {name: EncounterEntity.from_dict(name, data) for name, data in self.encounter_data.get_times_of_day().items()}

        self.setup_variables()
        self.setup_ui()

    def get_base_path(self):
        return os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'code', 'helper', 'src_game', 'Entities', 'pop', 'Random_Encounters')

    def setup_variables(self):
        self.biome_var = StringVar(self.window, value="ATMOSPHERE")
        self.season_var = StringVar(self.window, value="Winter")
        self.time_of_day_var = StringVar(self.window, value="Morning")
        self.traffic_var = StringVar(self.window, value="Barren")
        self.temp_var = StringVar(self.window, value="Cold")
        self.wind_var = StringVar(self.window, value="Strong")
        self.precipitation_var = StringVar(self.window, value="Normal")
        self.speed_var = StringVar(self.window, value="Normal")
        self.attitude_var = StringVar(self.window, value="Neutral")
        self.survival_var = StringVar(self.window, value="0-11")
        self.encounter_var = StringVar(self.window, value="TYPICAL")

        self.stored_encounter_ratings = None
        self.calendar_window = None
        self.boxes = []
        self.encounter_log = []
        self.encounter_results = []
        self.roll_results = [[0 for _ in range(4)] for _ in range(7)]
        self.first_day = 0  # Default value is Monday

    def setup_ui(self):
        self.setup_image_label()
        self.create_option_menus()
        self.create_buttons()
        self.create_text_box()

    def setup_image_label(self):
        self.image_label = Label(self.window)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.update_image(self.biome_var.get())

    def create_option_menus(self):
        self.add_option_menu("Biome:", 1, self.biome_var, self.biomes.keys(), self.on_select_change)
        self.add_option_menu("Season:", 2, self.season_var, self.seasons.keys())
        self.add_option_menu("Time of Day:", 3, self.time_of_day_var, self.times_of_day.keys())
        self.add_option_menu("Traffic:", 4, self.traffic_var, self.encounter_data.get_traffic().keys())
        self.add_option_menu("Temperature:", 5, self.temp_var, self.encounter_data.get_temp().keys())
        self.add_option_menu("Wind:", 6, self.wind_var, self.encounter_data.get_wind().keys())
        self.add_option_menu("Precipitation:", 7, self.precipitation_var, self.encounter_data.get_precipitation().keys())
        self.add_option_menu("Speed:", 8, self.speed_var, self.encounter_data.get_speed().keys())
        self.add_option_menu("Attitude:", 9, self.attitude_var, self.encounter_data.get_attitude().keys())
        self.add_option_menu("Survival:", 10, self.survival_var, self.encounter_data.get_survival_mods().keys())
        self.add_option_menu("Encounter:", 11, self.encounter_var, self.encounter_data.get_encounters())

    def add_option_menu(self, label, row, variable, options, command=None):
        Label(self.window, text=label).grid(row=row, column=0, padx=5, pady=5)
        OptionMenu(self.window, variable, *options, command=command).grid(row=row, column=1, padx=5, pady=5)

    def create_buttons(self):
        Button(self.window, text="See Encounter Ratings", command=self.calculate_encounter_ratings).grid(row=12, column=0)
        Button(self.window, text="Check Encounter Type", command=lambda: self.check_encounter_type(self.calculate_encounter_ratings())).grid(row=13, column=0)
        Button(self.window, text="Check For Encounter", command=lambda: self.check_for_encounter(self.calculate_encounter_ratings())).grid(row=13, column=1)
        Button(self.window, text="Clear", command=self.clear_all).grid(row=15, column=4)
        Button(self.window, text="Calendar", command=self.open_calendar_window).grid(row=15, column=1)
        Button(self.window, text="Save Results", command=self.save_encounter_results).grid(row=14, column=0)

    def create_text_box(self):
        # Create a Text widget and a Scrollbar, and link them together
        self.encounter_text = Text(self.window, height=10, width=60, wrap='word')  # wrap='word' for word wrapping
        self.encounter_text.grid(row=15, column=2, padx=5, pady=5)

        # Configure the scrollbar and link it to the text widget
        scrollbar = Scrollbar(self.window, orient="vertical", command=self.encounter_text.yview)
        scrollbar.grid(row=15, column=3, sticky='ns')

        # Set the text widget to update its yscrollcommand to the scrollbar
        self.encounter_text.config(yscrollcommand=scrollbar.set)


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

    def calculate_encounter_ratings(self):
        biome = self.biomes[self.biome_var.get()]
        season = self.seasons[self.season_var.get()]
        time_of_day = self.times_of_day[self.time_of_day_var.get()]
        traffic = self.encounter_data.get_traffic()[self.traffic_var.get()]
        temp = self.encounter_data.get_temp()[self.temp_var.get()]
        wind = self.encounter_data.get_wind()[self.wind_var.get()]
        precipitation = self.encounter_data.get_precipitation()[self.precipitation_var.get()]
        speed = self.encounter_data.get_speed()[self.speed_var.get()]
        attitude = self.encounter_data.get_attitude()[self.attitude_var.get()]
        survival = self.encounter_data.get_survival_mods()[self.survival_var.get()]

        calculator = EncounterCalculator(
            biome, season, time_of_day, traffic, temp, wind, precipitation, speed, attitude, survival
        )
        ratings = calculator.calculate_ratings()
        self.update_encounter_text(self.format_ratings(ratings))
        return ratings

    def format_ratings(self, ratings):
        return (
            f"Humanoid ER: {ratings['humanoid']}\n"
            f"Fauna ER: {ratings['fauna']}\n"
            f"Flora ER: {ratings['flora']}\n"
            f"Typical ER: {ratings['typical']}\n"
            f"Total Rating: {ratings['total']}\n\n"
        )

    def check_encounter_type(self, ratings):
        type_roll = random.random()
        encounter_type = self.determine_encounter_type(type_roll, ratings)
        sub_type = self.determine_sub_type(encounter_type)
        self.update_encounter_text(f"{round(type_roll, 3)}% {encounter_type}:{sub_type}\n")
        return sub_type, encounter_type

    def determine_encounter_type(self, roll, ratings):
        cumulative_probability = 0
        for encounter_type, weight in [("humanoid", ratings["humanoid"]), ("fauna", ratings["fauna"]), ("flora", ratings["flora"]), ("typical", ratings["typical"])]:
            cumulative_probability += weight / ratings["total"]
            if roll < cumulative_probability:
                return encounter_type

    def determine_sub_type(self, encounter_type):
        sub_type_roll = random.randint(1, 100)
        if sub_type_roll <= 75:
            return encounter_type
        elif sub_type_roll <= 89:
            return f"Special {encounter_type}"
        else:
            return f"Dead {encounter_type}"

    def check_for_encounter(self, ratings):
        sub_type, encounter_type = self.check_encounter_type(ratings)
        roll = random.randint(1, 20)
        survival_mod = self.encounter_data.get_survival_mods()[self.survival_var.get()]
        check = survival_mod + roll
        base_type = sub_type.split()[1] if " " in sub_type else sub_type

        encounter_happened = check <= ratings.get(base_type.lower(), 0)
        self.update_encounter_text(f"Encounter Happened: {encounter_happened} | Roll: {roll} | Type: {encounter_type}\n")

        if encounter_happened:
            encounter_details = self.generate_random_encounter(self.biome_var.get(), encounter_type)
            self.update_encounter_text(f"Encounter Details: {encounter_details}\n")

        return encounter_happened, roll, encounter_type

    def generate_random_encounter(self, biome, encounter_type):
        excel_file_path = os.path.join(self.base_path, 'Master_Biome_Encounter_Lists.xlsx')
        try:
            # Load the Excel file
            df = pd.read_excel(excel_file_path)

            # Convert both the 'Encounter' column and the encounter_type to uppercase for comparison
            filtered_df = df[(df['Biome'] == biome) & (df['Encounter'].str.upper() == encounter_type.upper())]

            # Check if the filtered DataFrame is empty
            if filtered_df.empty:
                return "No encounters found for the chosen biome and encounter type."

            # Return a random sample from the filtered DataFrame
            return self.format_encounter(filtered_df.sample(n=1))

        except FileNotFoundError:
            messagebox.showerror("Error", f"Excel file not found: {excel_file_path}")
            return "Error: Excel file not found."

    def format_encounter(self, encounter):
        return '\n'.join([f"{column.rjust(5)}: {str(value).rjust(5)}" for column, value in zip(encounter.columns.tolist(), encounter.values.tolist()[0])])

    def clear_all(self):
        self.encounter_text.delete('1.0', tk.END)

    def save_encounter_results(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.encounter_text.get('1.0', tk.END))

    def update_encounter_text(self, text):
        self.encounter_text.insert(tk.END, text)

    def open_calendar_window(self):
        if self.calendar_window is None or not self.calendar_window.winfo_exists():
            self.calendar_window = tk.Tk()
            self.calendar_window.title("1 Week")
            self.calendar_window.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.week_calendar()

    def week_calendar(self):
        # Clear existing boxes if any
        for widget in self.boxes:
            widget.destroy()

        self.boxes.clear()
        for _ in range(7):  # Creating 7 text boxes for each day of the week
            box_frame = tk.Frame(self.calendar_window, width=222, height=400)
            box_frame.grid(row=0, column=len(self.boxes))

            box = Text(box_frame, width=22, height=60, wrap=tk.WORD)
            box.grid(row=0, column=0, sticky="nsew")
            self.boxes.append(box)

        # Generate results for the week and update the calendar
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
                    encounter_happened = encounter_prob  # encounter_prob is already a boolean
                    text += f"{time_of_day[j]}:\n"
                    text += f"ER Humanoid: {humanoid_er}\n"
                    text += f"ER Fauna: {fauna_er}\n"
                    text += f"ER Flora: {flora_er}\n"
                    text += f"ER Typical: {typical_er}\n"
                    text += F"Total ER: {total_rating}\n"
                    if encounter_happened:
                        text += f"Encounter happened: True (Roll: {roll})\n"
                        text += f"Encounter Type: {encounter_type}\n\n"
                        encounter_details = self.generate_random_encounter(self.biome_var.get(), encounter_type)
                        text += f"{encounter_details}\n\n"
                    else:
                        text += "No encounter.\n\n"

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
                ratings = self.calculate_encounter_ratings()
                encounter_prob, roll, encounter_type = self.check_for_encounter(ratings)
                day_results.append((encounter_prob, roll, encounter_type, ratings['humanoid'], ratings['fauna'], ratings['flora'], ratings['typical'], ratings['total']))
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

def main():
    root = tk.Tk()
    app = RandomEncounterCalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
