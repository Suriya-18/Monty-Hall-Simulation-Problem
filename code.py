import random
from tkinter import StringVar, Label, Tk, Entry

# Set up the main application window
window = Tk()
window.geometry("400x100")
window.title("Monty Hall Simulation")
window.resizable(0, 0)

# Variables to store results
same_choice = StringVar()
switched_choice = StringVar()
same_choice.set(0)
switched_choice.set(0)

# Input field for number of simulations
no_sample = Entry()

# Labels for displaying results and inputs
Label(text="Same choice").place(x=80, y=8)
Label(text="Switched choice").place(x=80, y=40)
Label(textvariable=same_choice, font=(15)).place(x=180, y=8)
Label(textvariable=switched_choice, font=(15)).place(x=180, y=40)
no_sample.place(x=100, y=70)

# Simulation function triggered on Enter key
def simulate(event):
    same_choice_result = 0
    switched_choice_result = 0
    samples = int(no_sample.get())  # Get the number of simulations from user input
    doors = ["gold", "goat", "bed"]  # Possible doors
    for _ in range(samples):
        simulated_doors = doors.copy()
        random.shuffle(simulated_doors)  # Shuffle doors
        first_choice = random.choice(simulated_doors)  # Player's initial choice
        simulated_doors.remove(first_choice)  # Remove the initial choice from the options

        # Host opens a door that is not the "gold" door
        opened_door = (
            simulated_doors[0] if simulated_doors[0] != "gold" else simulated_doors[1]
        )
        simulated_doors.remove(opened_door)  # Remove the opened door

        # Remaining door is the switched choice
        switched_second_choice = simulated_doors[0]

        # Update results
        if first_choice == "gold":
            same_choice_result += 1
            same_choice.set(same_choice_result)  # Update displayed value
        elif switched_second_choice == "gold":
            switched_choice_result += 1
            switched_choice.set(switched_choice_result)  # Update displayed value
        else:
            print("This will never happen")  # Defensive programming

# Bind the Enter key to trigger the simulation
no_sample.bind("<Return>", simulate)

# Start the application loop
window.mainloop()
