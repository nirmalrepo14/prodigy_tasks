import re

def assess_password_strength(password):
    length = len(password)
    score = 0

    # Check length
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    # Check uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Check lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Check numbers
    if re.search(r'[0-9]', password):
        score += 1

    # Check special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1

    return score

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)

    if strength == 0:
        print("Very weak password")
    elif strength <= 2:
        print("Weak password")
    elif strength <= 4:
        print("Moderate password")
    elif strength <= 6:
        print("Strong password")
    else:
        print("Very strong password")

if __name__ == "__main__":
    main()

#output
Enter your password: Password$123
Strong password
