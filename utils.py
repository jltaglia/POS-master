import random

def generate_id(length=6):
    """Generate a random string of characters for use as a unique ID"""
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.choice(characters) for i in range(length))
