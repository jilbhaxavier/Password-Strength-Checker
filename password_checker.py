
import string

print("===================================")
print("     PASSWORD STRENGTH CHECKER")
print("===================================")

# Get password from user
password = input("Enter your password: ")

# Check password conditions
length = len(password) >= 8

uppercase = any(char.isupper() for char in password)

lowercase = any(char.islower() for char in password)

number = any(char.isdigit() for char in password)

special = any(char in string.punctuation for char in password)

# Calculate score
score = sum([length, uppercase, lowercase, number, special])

# Display password analysis
print("\n---------- PASSWORD ANALYSIS ----------")

print("Length (8 or more):", length)
print("Uppercase letter:", uppercase)
print("Lowercase letter:", lowercase)
print("Number:", number)
print("Special character:", special)

# Classify password strength
print("\n---------- PASSWORD STRENGTH ----------")

if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MEDIUM")

else:
    print("Password Strength: STRONG")

# Give suggestions
print("\n---------- SUGGESTIONS ----------")

if not length:
    print("- Use at least 8 characters.")

if not uppercase:
    print("- Add an uppercase letter.")

if not lowercase:
    print("- Add a lowercase letter.")

if not number:
    print("- Add a number.")

if not special:
    print("- Add a special character.")

if score == 5:
    print("Great! Your password meets all five checks.")

print("\nThank you for using Password Strength Checker!")
