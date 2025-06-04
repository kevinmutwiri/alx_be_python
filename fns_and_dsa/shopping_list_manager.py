def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add(shopping_list):
    item = input("Enter item to add: ")
    shopping_list.append(item)


def remove(shopping_list):
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found.")


def display(shopping_list):
    for item in shopping_list:
        print(item)


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add(shopping_list)
        elif choice == '2':
            remove(shopping_list)
        elif choice == '3':
            display(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()