import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check for length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short. Use at least 8 characters.")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $).")

    # Determine password strength level
    if strength >= 5:
        strength_level = "Strong"
    elif 3 <= strength < 5:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"
    
    # Provide feedback to the user
    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password is strong.")

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()
