import tkinter as tk
import random

def roll_dice():
    pass  # Placeholder for logic (already implemented below)
    # Get the number of dice and sides from the input fields
    try:
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
        
        if show_detailed_results.get():
            result_label.config(text=f"Result: {', '.join(map(str, dice_result))}")
        else:
            result_label.config(text="Result: (Detailed results hidden)")
        total_label.config(text=f"Total: {total}")
    except ValueError:
        if not dice_count_entry.get().isdigit():
            result_label.config(text="Error: Number of dice must be an integer")
        elif not sides_count_entry.get().isdigit():
            result_label.config(text="Error: Number of sides must be an integer")
        else:
            result_label.config(text="Error: Enter valid numbers")
        total_label.config(text="Total: ")

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

# Add a variable to track the toggle state
show_detailed_results = tk.BooleanVar(value=True)
root.mainloop()