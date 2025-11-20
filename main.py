def generate_profile(age):

    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"



def main():
    # Welcome message
    print("Welcome to the Mini-Profile Generator!")
    print("-" * 40)

    # Get user's basic information
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")

    # Convert and calculate age
    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year

    # Collect hobbies
    hobbies = []
    print("\nLet's collect your favorite hobbies!")

    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()

        if hobby.lower() == "stop":
            break
        elif hobby:  # Only add non-empty hobbies
            hobbies.append(hobby)

    # Generate profile and life stage
    life_stage = generate_profile(current_age)

    # Create user profile dictionary
    user_profile = {
        "name": user_name,
        "age": current_age,
        "stage": life_stage,
        "hobbies": hobbies
    }

    # Display the profile summary
    print("\n" + "=" * 50)
    print("Profile Summary:")
    print("=" * 50)
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['stage']}")

    # Display hobbies
    if not user_profile['hobbies']:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile['hobbies']:
            print(f"- {hobby}")  # ← Этой строке нужен отступ (4 пробела)

    print("=" * 50)


# Run the program
if __name__ == "__main__":
    main()