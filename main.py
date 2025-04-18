from pet import Pet

def main():
    pet_name = input("🐾 Name your pet: ")
    my_pet = Pet(pet_name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Train a trick")
        print("5. Show tricks")
        print("6. Show status")
        print("7. Exit")

        choice = input("Choose an option (1–7): ")

        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            trick = input("What trick should your pet learn? ")
            my_pet.train(trick)
        elif choice == "5":
            my_pet.show_tricks()
        elif choice == "6":
            my_pet.get_status()
        elif choice == "7":
            print(f"Goodbye from you and {my_pet.name}! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

