import random

def load_items(filename):
    """Load items and their difficulty levels and OS traits from a file into a list of tuples."""
    items = []
    with open(filename, 'r') as file:
        for line in file:
            name, difficulty, trait = line.strip().split(',')
            items.append((name, int(difficulty), trait))
    return items

def choose_items(items, num_items):
    """Randomly select a specified number of items from a list."""
    return random.sample(items, num_items)

def filter_items_by_trait(items, trait):
    """Filter items by a specific trait."""
    if trait == "all":
        return items
    return [item for item in items if item[2].lower() == trait.lower()]

def calculate_average_difficulty(selected_items):
    """Calculate the average difficulty level of the selected items."""
    total_difficulty = sum(item[1] for item in selected_items)
    return total_difficulty / len(selected_items)

def main():
    databases = {
        1: ('database1.txt', 'ProvingGrounds Practice'),
        2: ('database2.txt', 'HackTheBox'),
        3: ('database3.txt', 'TryHackMe'),
        4: ('database4.txt', 'Virtual Hacking Labs'),
        5: ('database5.txt', 'ProvingGrounds Play')
    }

    print("Choose a platform: ")
    for key, (_, name) in databases.items():
        print(f"{key}. {name}")

    while True:
        try:
            db_choice = int(input(f"Enter a number (1-{len(databases)}): "))
            if 1 <= db_choice <= len(databases):
                filename, db_name = databases[db_choice]
                break
            else:
                print(f"Please enter a number between 1 and {len(databases)}.")
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {len(databases)}.")

    items = load_items(filename)
    
    # Updating databases above^

    while True:
        try:
            num_items = int(input("How many machines would you like to attempt? (2-6): "))
            if 2 <= num_items <= 6:
                break
            else:
                print("Please enter a number between 2 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 6.")

    while True:
        trait = input("Which trait do you want to filter by? (Linux, Windows, Active Directory, all): ").strip()
        if trait.lower() in ["linux", "windows", "active directory", "all"]:
            break
        else:
            print("Invalid input. Please enter 'Linux', 'Windows', 'Active Directory', or 'all'.")
   
    filtered_items = filter_items_by_trait(items, trait)

    if len(filtered_items) <num_items:
        print(f"Not enough items with the trait '{trait}'. Showing all available items.")
        selected_items = filtered_items
    else:
        selected_items = choose_items(filtered_items, num_items)

    average_difficulty = calculate_average_difficulty(selected_items)
    
    print("Selected items:")
    for item, difficulty, trait in selected_items:
        difficulty_str = ["easy", "intermediate", "hard"][difficulty - 1]
        print(f"{item} (Difficulty: {difficulty_str}, Trait: {trait})")

    print(f"Average difficulty level: {average_difficulty:.2f}")

if __name__ == "__main__":
    main()