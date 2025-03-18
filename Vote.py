# Ask for the user's age
try:
    age = int(input("Enter your age: "))
    
    # Check if the user is a minor
    if age < 18:
        print("You're a minor. You're not eligible to vote!")
    elif age >= 18:
        # Ask for the country name
        country = input("Enter your country name: ").strip()
        
        if country:
            print(f"In {country}, you're eligible to vote!")
        else:
            print("You're not a citizen.")
    else:
        print("You're exactly 18, congrats! However, you didn't specify voting requirements.")
except ValueError:
    print("Please enter a valid numeric age.")
