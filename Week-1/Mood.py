def mood(user):
    moods = {"happy": "😊", "sad": "😔", "angry": "😠", "excited": "😃", "bored": "😒", "neutral": "😐", "committed": "😤", "Shocked": "😶", "Stunt": "🫥", "may be": "🙃", "party": "🥳", "jocker": "🤡"}
    return moods.get(user, "😑 I dont't know this mood")  # return a default value if the user


def main():
    user = input("Enter Mood: ").lower()
    print(mood(user))

main()