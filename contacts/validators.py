import re

def is_valid_email(text):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email_bool = bool(re.search(email_pattern, text))
    return email_bool

def is_valid_phone(text):
    phone_pattern = r"^(?:\+?1[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$"
    phone_bool = bool(re.search(phone_pattern, text))
    return phone_bool