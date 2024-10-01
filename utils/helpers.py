# utils/helpers.py
import random
import string

def generate_unique_email():
    return f"test-{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@example.com"
