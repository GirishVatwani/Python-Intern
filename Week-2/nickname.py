import random

# Step 1: Get user input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Step 5: Ask for preferred style
style = input("Preferred nickname style (short, fun, formal, creative): ").strip().lower()

# Helper functions
def short_style(f, l):
    return [
        f[:3] + l[-2:],  # first 3 of first + last 2 of last
        f[0] + l[:2],    # initials with twist
        f[:2] + l[:2],
        (f + l)[:5]
    ]

def fun_style(f, l):
    emojis = ["😎", "🔥", "✨", "🎉", "💥"]
    return [
        f[:2].capitalize() + l[-3:].lower() + str(random.randint(10, 99)),
        f.capitalize() + "_" + l.capitalize() + random.choice(emojis),
        l[::-1] + f[0].upper(),
        f[1:] + l[0].upper() + "X"
    ]

def formal_style(f, l):
    return [
        f.capitalize() + " " + l.capitalize(),
        f[0].upper() + ". " + l.capitalize(),
        f[:1].upper() + l.capitalize(),
        l.capitalize() + ", " + f.capitalize()
    ]

def creative_style(f, l):
    return [
        f[:2].upper() + l[-2:].lower() + str(random.randint(100, 999)),
        f[::-1] + l[::-1],
        f[0].upper() + l[0].lower() + "_" + str(random.randint(1, 50)),
        f[:2] + "_" + l[:2] + "_" + str(random.randint(10, 99))
    ]

# Step 4: Generate combinations based on style
if style == "short":
    nicknames = short_style(first_name, last_name)
elif style == "fun":
    nicknames = fun_style(first_name, last_name)
elif style == "formal":
    nicknames = formal_style(first_name, last_name)
else:
    nicknames = creative_style(first_name, last_name)

# Step 6: Display nicknames
print("\nHere are your generated nicknames:")
for i, nick in enumerate(nicknames, start=1):
    print(f"{i}. {nick}")

# Step 7: Ask if user wants to save
save = input("\nDo you want to save these nicknames to a file? (yes/no): ").strip().lower()
if save == "yes":
    with open("generated_nicknames.txt", "w") as file:
        for nick in nicknames:
            file.write(nick + "\n")
    print("Nicknames saved to 'generated_nicknames.txt'.")
