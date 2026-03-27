def tip_calculator():
    try:
        bill = float(input("Enter total bill amount: ₹"))
        tip_percent = float(input("Enter tip percentage (%): "))
        people = int(input("Enter number of people: "))

        tip_amount = (bill * tip_percent) / 100
        total_amount = bill + tip_amount
        per_person = total_amount / people

        print("\n----- Result -----")
        print(f"Tip Amount: ₹{tip_amount:.2f}")
        print(f"Total Amount: ₹{total_amount:.2f}")
        print(f"Each Person Pays: ₹{per_person:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

tip_calculator()
