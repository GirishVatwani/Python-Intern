# Color Psychology Recommender
# This program recommends a color based on the user's mood using color psychology principles.
# It uses a dictionary to map colors to associated adjectives and moods.
# The user is prompted to input their mood, and the program returns a recommended color.
# The program is structured with functions for getting the mood, recommending a color, and the main execution flow.


COLORS = {
    "red": ["energetic", "passionate", "confident"],
    "blue": ["calm", "trustworthy", "stable", "serene", "relaxed"],
    "yellow": ["optimistic", "happy", "cheerful", "friendly"],
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

OUTFITS = {
    "red": ["Bold red blazer or dress for powerful presentations",
            "Red sneakers or top for an energetic casual look", 
            "Statement red lipstick with black attire for confidence"],
    
    "blue": ["Navy blue suit for a professional appearance",
            "Light blue shirt with jeans for a relaxed yet stylish look",
            "Blue accessories like a scarf or watch for a calming touch"],

    "yellow": ["Bright yellow sundress for a cheerful summer day",
            "Yellow cardigan over a white top for a friendly vibe",
            "Yellow sneakers to add a pop of color to your outfit"],

    "green": ["Olive green jacket for a nature-inspired look",
            "Forest green sweater with jeans for a balanced outfit",
            "Emerald green dress for a peaceful evening out"],

    "black": ["Classic black suit for formal occasions",
            "Black leather jacket for an authoritative edge",
            "Little black dress for timeless elegance"],

    "pink": ["Soft pink blouse for a nurturing and romantic look",
            "Pink sneakers for a casual and compassionate vibe",
            "Pink accessories like a handbag or scarf for a soft touch"],

    "purple": ["Lavender dress for a creative and mystical appearance",
            "Deep purple blazer for a luxurious and royal touch",
            "Purple accessories like earrings or a bracelet for a pop of color"],
    
    "orange": ["Bright orange t-shirt for an energetic casual look",
            "Orange dress for a warm and exciting vibe",
            "Orange sneakers to add enthusiasm to your outfit"],

    "brown": ["Earthy brown sweater for a reliable and stable look",
            "Brown leather jacket for a natural and rugged style",
            "Brown boots for a grounded and earthy touch"],

    "gray": ["Charcoal gray suit for a sophisticated appearance",
            "Light gray sweater for a neutral and casual look",
            "Gray accessories like a watch or belt for a subtle touch"],

    "white": ["Crisp white shirt for a clean and fresh look",
            "White dress for an innocent and elegant appearance",
            "White sneakers for a pure and casual vibe"],

    "gold": ["Gold dress for a glamorous evening out",
            "Gold accessories like earrings or a bracelet for a luxurious touch",
            "Gold heels to add prestige to your outfit"],

    "silver": ["Silver dress for a modern and sleek appearance",
            "Silver accessories like a watch or necklace for an elegant touch",
            "Silver shoes to add a high-tech and stylish element to your outfit"],

    "teal": ["Teal blouse for a refreshing and soothing look",
            "Teal dress for a tranquil and elegant appearance",
            "Teal accessories like a scarf or handbag for a pop of color"],

    "turquoise": ["Turquoise t-shirt for an invigorating casual look",
            "Turquoise dress for a friendly and energetic vibe",
            "Turquoise accessories like earrings or a bracelet for a creative touch"],

    "default": ["Casual outfit with neutral colors for any mood",
                "Comfortable loungewear for a relaxed day at home",
                "Versatile jeans and a t-shirt for everyday wear"]
    
}

def get_mood():
    mood = input("How are you feeling today? \n(happy, sad, angry, relaxed, anxious, stressed): ").strip().lower()
    return mood

def recommend_color(mood):
    for color, adjectives in COLORS.items():
        if mood in adjectives:
            return color
    return None

def reccomend_outfit(color):
    if color in OUTFITS:
        return OUTFITS[color]
    else:
        return OUTFITS["default"]

def main():
    mood = get_mood()
    recommended_color = recommend_color(mood)

    if recommended_color is None:
        print("Try with other words to describe your mood.")
        return main()
    
    outfit_recommendations = reccomend_outfit(recommended_color)
    
    print(f"Based on your mood '{mood}', we recommend the color: {recommended_color}")
    print("Here are some outfit recommendations:")
    for outfit in outfit_recommendations:
        print(f"- {outfit}")

if __name__ == "__main__":
    main()

