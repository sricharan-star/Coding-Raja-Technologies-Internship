import csv
from datetime import datetime

# Define the file name for storing food expenses
file_name = 'food_expenses.csv'

# Function to add a food expense
def add_food_expense(amount, description=''):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    category = 'Food'
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print(f"Added food expense: ${amount} for {description}.")

# Function to view all food expenses
def view_food_expenses():
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No food expenses found. Add a food expense first.")

# Function to get total food expenses
def get_total_food_expenses():
    total = 0
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
    except FileNotFoundError:
        print("No food expenses found. Add a food expense first.")
    print(f"Total food expenses: ${total}")

# Main menu
def main():
    while True:
        print("\nFood Expense Tracker")
        print("1. Add a food expense")
        print("2. View all food expenses")
        print("3. Get total food expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ")
            add_food_expense(amount, description)
        elif choice == '2':
            view_food_expenses()
        elif choice == '3':
            get_total_food_expenses()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()