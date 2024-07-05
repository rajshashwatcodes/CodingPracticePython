import random

# Word lists categorized by syllables
one_syllable_words = ["moon", "star", "wind", "cloud", "stream", "tree", "sky", "snow", "rain"]
two_syllable_words = ["mountain", "river", "blossom", "autumn", "meadow", "whisper"]
three_syllable_words = ["harmony", "beautiful", "serenity", "butterfly"]

def generate_haiku():
    # Generate each line of the haiku
    line1 = random.choice(one_syllable_words) + " " + random.choice(two_syllable_words) + " " + random.choice(two_syllable_words)
    line2 = random.choice(two_syllable_words) + " " + random.choice(one_syllable_words) + " " + random.choice(two_syllable_words) + " " + random.choice(one_syllable_words)
    line3 = random.choice(three_syllable_words) + " " + random.choice(one_syllable_words) + " " + random.choice(one_syllable_words)
    
    return line1.capitalize() + "\n" + line2.capitalize() + "\n" + line3.capitalize()

# Generate and print a random haiku
print("Here's a random haiku for you:\n")
print(generate_haiku())
