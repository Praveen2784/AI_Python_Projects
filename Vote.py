try:
    age = int(input("Enter your age: "))
    print("You're a minor. You're not eligible to vote!" if age < 18 else (f"In {country}, you're eligible to vote!" if (country := input("Enter your country name: ").strip()) else "You're not a citizen."))
except ValueError:
    print("Please enter a valid numeric age.")