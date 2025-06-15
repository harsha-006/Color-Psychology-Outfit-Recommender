mood_color={
    "happy": ["yellow", "orange"],
    "cheerful": ["dark pink"],
    "sad": ["blue"],
    "angry": ["red"],
    "stressed": ["blue"],
    "relaxed": ["green"],
    "energetic": ["red", "orange"],
    "calm": ["white"],
    "motivated": ["red"],
    "peaceful": ["green"],
    "serious": ["black"],
    "professional": ["black"],
    "caring": ["pink"],
    "soft": ["pink"],
    "confident": ["red"],
    "bored": ["purple"],
    "lonely": ["grey"]
}

outfits={
    "casual": {
        "red": "a red t-shirt with white sneakers",
        "orange": "an orange polo shirt and khakis",
        "yellow": "a yellow top and denim shorts",
        "blue": "a blue hoodie with jeans",
        "green": "a green kurta and sandals",
        "black": "a black t-shirt and joggers",
        "pink": "a pink sweatshirt and leggings",
        "purple": "a purple graphic tee and jeans",
        "grey": "a grey hoodie and joggers"  },
    "formal": {
        "red": "a red blouse and black skirt",
        "orange": "an orange dress shirt with trousers",
        "yellow": "a yellow formal shirt and beige pants",
        "blue": "a blue blazer and dress pants",
        "green": "a green shirt and navy pants",
        "black": "a black suit or formal dress",
        "pink": "a pink formal shirt or dress",
        "purple": "a purple blazer and formal trousers",
        "grey": "a grey suit with a white shirt" },
    "sporty": {
        "red": "a red dri-fit t-shirt with track pants",
        "orange": "an orange gym tank and shorts",
        "yellow": "a yellow jersey and joggers",
        "blue": "a blue workout hoodie and tights",
        "green": "a green sweatband with shorts",
        "black": "a black sports t-shirt with leggings",
        "pink": "a pink tank and yoga pants",
        "purple": "a purple activewear set",
        "grey": "a grey gym tee with shorts" },
    "ethnic": {
        "red": "a red kurta and white pajama",
        "orange": "an orange saree or kurta",
        "yellow": "a yellow salwar kameez",
        "blue": "a blue lehenga or kurta",
        "green": "a green silk saree or kurta",
        "black": "a black sherwani or churidar",
        "pink": "a pink anarkali or kurti",
        "purple": "a purple saree with silver border",
        "grey": "a grey kurta with pastel dupatta"  },
    "trendy": {
        "red": "a red crop top with ripped jeans",
        "orange": "an orange oversized tee and sneakers",
        "yellow": "a yellow tube top and denim skirt",
        "blue": "a blue tie-dye hoodie and joggers",
        "green": "a neon green top and black cargos",
        "black": "a black graphic tee with boots",
        "pink": "a pink puffer jacket and mom jeans",
        "purple": "a purple hoodie with white sneakers",
        "grey": "a grey flannel with layered chains"}
}

season_colors={
    "summer":["yellow", "orange", "green", "blue", "pink"],
    "winter":["red", "black", "blue", "grey", "purple"],
    "rainy":["blue", "grey", "green", "black"]}

def get_colors_from_mood(mood_input):
    mood_words=mood_input.lower().replace("and", ",").replace("also", ",").split(",")
    matched_colors=set()
    for mood in mood_words:
        mood=mood.strip()
        if mood in mood_color:
            matched_colors.update(mood_color[mood])
    return list(matched_colors)

def suggest_outfits():
    print("Helloo!! Let’s help you pick an outfit that matches your current mood.")

    while True:
        mood_input=input("\nHow are you feeling today? \nSay(e.g.,happy,sad,calm,energetic): ").strip()
        if not mood_input:
            print("Oops! Please tell me at least one mood.")
            continue
        colors=get_colors_from_mood(mood_input)
        if colors:
            break
        print("Hmm,I didn’t recognize those moods. Try something like happy, relaxed, or energetic.")

    styles=list(outfits.keys())
    print(f"\nstyles: {', '.join(styles)}")
    style=input("What style are you in the mood for? (e.g., casual, formal, sporty.): ").strip().lower()
    if style not in outfits:
        print("That style isn't in our wardrobe. I'll go with casual as the default.")
        style="casual"

    season=input("What’s the current season? (summer/winter/rainy): ").strip().lower()
    if season not in season_colors:
        print("No problem! I’ll suggest colors for any season.")
        filtered_colors=colors
    else:
        filtered_colors=[c for c in colors if c in season_colors[season]]
        if not filtered_colors:
            filtered_colors = colors

    print("\nColors that match your mood:", ", ".join(filtered_colors).title())
    print("\nOutfit suggestions just for you:")
    for color in filtered_colors:
        outfit=outfits.get(style,{}).get(color)
        if outfit:
            print(f"-{color.title()}: {outfit}")
        else:
            print(f"-{color.title()}: Rock anything stylish in this color!")

    #Extra Features
    print("\nBonus Style Tips Just for You:")
    print(" - Multi-Mood Matching: You can enter more than one mood (like 'relaxed and cheerful'), and we’ll mix and match the best colors for you.")
    print(" -Outfit Pairing Ideas: Try combining a top in one mood-matching color with bottoms or accessories in another for a balanced look.")
    print(" -Personalized Style Choices: Whether you prefer casual, formal, sporty, trendy, or ethnic styles — we’ve got you covered.")
    print(" -Seasonal Style Suggestions: We recommend light, fresh colors for summer, cozy darks for winter, and water-friendly styles for rainy days.")


if __name__ == "__main__":
    suggest_outfits()

    
