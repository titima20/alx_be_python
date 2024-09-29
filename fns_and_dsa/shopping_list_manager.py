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
        choice = input("Enter your choice: ")

        if choice == '1':
            added_item = input('inter the item you want to add ')
            shopping_list.append(added_item)
            pass
        elif choice == '2':
            removed_item = input('inter the item you want to remove ')
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
            else: 
                print(f'{removed_item} is not in the list ')
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()