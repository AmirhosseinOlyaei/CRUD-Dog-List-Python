dogs = []  # list[str]
# add a dog
# - max of 25
# - name can't be duplicate
# update a dog (not now)
# remove a dog
# - remove by its name
# exit


def read_required_string(prompt):
    """
    Reads a non-empty string from the user.

    Parameters:
    - prompt (str): The prompt to display to the user.

    Returns:
    str: The non-empty string entered by the user.
    """
    value = ""
    while not value:
        value = input(prompt).strip()
        if not value:
            print("Value required")

    return value


NAME_PROMPT = "Dog's name: "


def add_dog():
    """
    Adds a dog to the list.

    Checks if the list has reached its maximum capacity (25) and if the dog's name is not a duplicate.
    """
    print("Add a dog")
    if len(dogs) >= 25:
        print("Maximum capacity reached. Cannot add more dogs.")
        return
    name = read_required_string(NAME_PROMPT)
    while name in dogs:
        print("Dog already exists")
        name = read_required_string(NAME_PROMPT)
    dogs.append(name)
    print("Dog added")


def display_dog():
    """
    Displays the list of dogs with their index.
    """
    for index, name in enumerate(dogs):
        if name:
            print(f"{index + 1}. {name}")

    if not dogs:
        print("The list is empty")


def remove_dog():
    """
    Removes a dog from the list by its name.
    """
    print("Remove a dog")
    name = read_required_string(NAME_PROMPT)
    if name in dogs:
        dogs.remove(name)
        print(f"{name} removed")
    else:
        print("Dog not found")


def run():
    """
    Main function to run the program.
    """
    print("Curious Hounds")
    option = ""
    while option != "0":
        print()
        print("0. Exit")
        print("1. Add a dog")
        print("2. Display a dog")
        print("3. Remove a dog")
        option = read_required_string("Select [0-3]: ")
        if option == "0":
            print("Goodbye!")
        elif option == "1":
            add_dog()
        elif option == "2":
            display_dog()
        elif option == "3":
            remove_dog()
        else:
            print("I don't understand that command.")


if __name__ == "__main__":
    run()
