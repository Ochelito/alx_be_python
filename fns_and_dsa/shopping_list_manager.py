def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
    
        choice = input("Enter your choice: "))
        print ("Invalid input. Please Enter a number from 1-4")
    
        if choice == '1':
            available_items = ["Orange", "Mango", "Grape"]
            print ("Available Items:", available_items)
            add_item = input("Which item would you like to add: ").strip().lower()
            
            if add_item in available_items:
                shopping_list.append(add_item)
                print (f"{add_item} Added to your Cart!")
            else:
                print (f"{add_item} is not Available!")
            
        elif choice == '2':
            if shopping_list:
                print ("Items in your Cart: ", shopping_list)
                remove_item = input(" Which Item would you like to remove? ").strip().lower()
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
                    print(f"{remove_item} Has been removed from your Cart")
                else:
                    print (f"{remove_item} is not present in your cart")
            else:
                print ("Your Cart is Empty! Add Items.")
        
        elif choice == '3':
            print (shopping_list)
             
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


"""
Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

Task Description:
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

Requirements:
Core Functionality:

Your script should start with an empty list named shopping_list.
Implement functionality to add items to the list, remove items, and display the current list.
User Interface:

Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
For adding items, prompt the user for the item name and append it to shopping_list.
For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
To view the list, print each item in shopping_list to the console.
Ensure your script handles invalid menu choices gracefully.


shopping_list = []
print ("Shopping List Manager")
operation = input("""
"""What would you like to do?

    #'Add' - To add an item to your cart
    #'Remove' - To remove an item from your cart
    'View List' - To display the items in your cart
    'Exit' - To exit

 ).strip().lower()
while True:
    if operation == "add":
        choice = input("Which item would you like to add- Orange, Mango, Grape: ").strip().lower()
        
        if choice == "orange":
            shopping_list.append(choice)
            print (f"{choice} Added to your Cart!")
        elif choice == "mango":
            shopping_list.append(choice)
            print (f"{choice} Added to your Cart!")
        elif choice == "grape":
            shopping_list.append(choice)
            print (f"{choice} Added to your Cart!")
        else:
            print (f"{choice} is not Available!")

    elif operation == "remove":
        if shopping_list != []:
            print ("Items in your Cart: ", shopping_list)
            remove_item = input(" Which Item would you like to remove? ").strip().lower()
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print (f"{remove_item} is not present in your cart")
        else:
            print ("Your Cart is Empty! Add Items.")

    elif operation == "display":
        print (shopping_list)

    elif operation == "exit":
        print ("Goodbye..")
        break

    else:
        print ("Invalid Command! Please try again")"""

"""def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    available_items = ["orange", "mango", "grape"]

    while True:
        display_menu()
    
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print ("Invalid input. Please Enter a number from 1-4")
            continue
    
        if choice == 1:
            print ("Available Items:", available_items)
            add_item = input("Which item would you like to add: ").strip().lower()
            
            if add_item in available_items:
                shopping_list.append(add_item)
                print (f"{add_item} Added to your Cart!")
            else:
                print (f"{add_item} is not Available!")
            
        elif choice == 2:
            if shopping_list != []:
                print ("Items in your Cart: ", shopping_list)
                remove_item = input(" Which Item would you like to remove? ").strip().lower()
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
                    print(f"{remove_item} Has been removed from your Cart")
                else:
                    print (f"{remove_item} is not present in your cart")
            else:
                print ("Your Cart is Empty! Add Items.")
        
        elif choice == 3:
            if shopping_list:
                print ("\nYour Cart:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}.{item}")

        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()"""