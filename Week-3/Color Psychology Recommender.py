# Color Psychology Recommender
# This program recommends a color based on the user's mood using color psychology principles.
# It uses a dictionary to map colors to associated adjectives and moods.
# The user is prompted to input their mood, and the program returns a recommended color.
# The program is structured with functions for getting the mood, recommending a color, and the main execution flow.


COLORS = {
    "red": ["energeitcic", "cassionate", "confident"],
    "blue": ["calm", "trustworthy", "stable", "serene", "relaxed"],
    "yellow": ["optimiscic", "happy", "cheerful", "friendly"],
    "green": ["balanced", "nature inspired", "peaceful", "harmonious"],
    "black": ["powerful", "formal", "authoritative"],
    "pink": ["compassionate", "soft", "nurturing", "romantic"],
    "purple": ["creative", "mystical", "luxurious", "royal"],
    "orange": ["energetic", "enthusiastic", "warm", "exciting"],
    "brown": ["earthy", "reliable", "stable", "natural"],
    "gray": ["neutral", "sad", "broken", "sophisticated"],
    "white": ["pure", "clean", "innocent", "fresh"],
    "gold": ["rich", "luxurious", "wealthy", "prestigious", "glamorous"],
    "silver": ["modern", "sleek", "high-tech", "elegant"],
    "teal": ["refreshing", "soothing", "tranquil"],
    "turquoise": ["invigorating", "creative", "friendly", "energetic"],
}

def get_mood():
    mood = input("How are you feeling today? \n(happy, sad, angry, relaxed, anxious, stressed): ").strip().lower()
    return mood

def recommend_color(mood):
    for color, adjectives in COLORS.items():
        if mood in adjectives:
            return color
    return "No specific color found for your mood."

def main():
    mood = get_mood()
    recommended_color = recommend_color(mood)
    print(f"Based on your mood, we recommend the color: {recommended_color}")

if __name__ == "__main__":
    main()

