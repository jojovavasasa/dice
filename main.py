import tkinter as tk
import random

def roll_dice():
    try:
        # Get the number of dice and sides from the input fields
        num_dice = int(dice_count_entry.get())
        num_sides = int(sides_count_entry.get())
        
        # Validate inputs
        if num_dice <= 0 or num_sides <= 0:
            result_label.config(text="Error: Enter positive numbers")
            return
        
        # Roll the dice and calculate the result
        dice_result = [random.randint(1, num_sides) for _ in range(num_dice)]
        result_label.config(text=f"Result: {', '.join(map(str, dice_result))}")
    except ValueError:
        result_label.config(text="Error: Enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Create and place widgets
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 16))
roll_button.pack(pady=20)

# Create and place input fields for number of dice and sides
dice_count_label = tk.Label(root, text="Number of Dice:", font=("Arial", 12))
dice_count_label.pack()
dice_count_entry = tk.Entry(root, font=("Arial", 12))
dice_count_entry.pack()

sides_count_label = tk.Label(root, text="Number of Sides:", font=("Arial", 12))
sides_count_label.pack()
sides_count_entry = tk.Entry(root, font=("Arial", 12))
sides_count_entry.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
result_label.pack(pady=20)
# Add a label to display the total of the dice rolls
total_label = tk.Label(root, text="Total: ", font=("Arial", 16))
total_label.pack(pady=10)

# Update the roll_dice function to calculate and display the total
def roll_dice():
    try:
        # Get the number of dice and sides from the input fields
        num_dice = int(dice_count_entry.get())
        num_sides = int(sides_count_entry.get())
        
        # Validate inputs
        if num_dice <= 0 or num_sides <= 0:
            result_label.config(text="Error: Enter positive numbers")
            total_label.config(text="Total: ")
            return
        
        # Roll the dice and calculate the result
        dice_result = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(dice_result)
        result_label.config(text=f"Result: {', '.join(map(str, dice_result))}")
        total_label.config(text=f"Total: {total}")
    except ValueError:
        result_label.config(text="Error: Enter valid numbers")
        total_label.config(text="Total: ")
# Run the application
root.mainloop()