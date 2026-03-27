import tkinter as tk
from tkinter import messagebox

def calculate_tip():
    try:
        bill = float(entry_bill.get())
        tip_percent = float(entry_tip.get())
        people = int(entry_people.get())

        tip_amount = (bill * tip_percent) / 100
        total_amount = bill + tip_amount
        per_person = total_amount / people

        result.set(
            f"Tip: ₹{tip_amount:.2f}\n"
            f"Total: ₹{total_amount:.2f}\n"
            f"Per Person: ₹{per_person:.2f}"
        )
    except:
        messagebox.showerror("Error", "Please enter valid inputs")

# Window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("300x300")

# Inputs
tk.Label(root, text="Bill Amount (₹)").pack()
entry_bill = tk.Entry(root)
entry_bill.pack()

tk.Label(root, text="Tip (%)").pack()
entry_tip = tk.Entry(root)
entry_tip.pack()

tk.Label(root, text="Number of People").pack()
entry_people = tk.Entry(root)
entry_people.pack()

# Button
tk.Button(root, text="Calculate", command=calculate_tip).pack(pady=10)

# Result
result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
