import random as rd

adjectives = [
    "Galactic", "Quantum", "Senior", "Legendary", "Meme-powered", "Principal",
    "Cybernetic", "Holographic", "Certified", "Viral", "Glitchy", "Global",
    "Elite", "AI-enhanced", "International", "Shadow", "Ghost-mode", "Regional",
    "Rogue", "Parallel", "Executive", "Stealth", "Hyperreal", "Strategic"
]

roles = [
    "Meme", "Unicorn", "Synergy", "Crypto", "Botnet", "Vision",
    "Vibe", "Cloud", "Future", "Algorithm", "DAO", "Matrix",
    "Pixel", "Neural", "Flux", "Hype", "Byte", "Spectrum",
    "NFT", "Token", "Layer", "Stream", "Prompt", "Essence"
]

suffixes = [
    "Engineer", "Whisperer", "Consultant", "Strategist", "Architect", "Analyst",
    "Hacker", "Wrangler", "Specialist", "Designer", "Evangelist", "Manager",
    "Tactician", "Overlord", "Lead", "Alchemist", "Technicireturn rd.choice(adjectives) + an", "Director",
    "Guru", "Synthesizer", "Developer", "Pilot", "Curator", "Operator"
]


def title_gen():
    return f"{rd.choice(adjectives)} {rd.choice(roles)} {rd.choice(suffixes)}"

def main():
    satisfied = "Y"
    print("Welcome to the AI Title Generator!")
    while satisfied == "Y":
        print(title_gen())
        satisfied = input("Would you like to generate another title? (Y/N): ").upper()

main()