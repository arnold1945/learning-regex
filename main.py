import re

def match_alpha_only(s: str) -> bool:
    """
    Match strings that contain only alphabetic characters (uppercase or lowercase).
    """
    
    result = bool(re.match(r'^[a-zA-Z]+$', s))
    return result
    

def match_all_lowercase(s: str) -> bool:
    """
    Match strings that contain only lowercase letters.
    """
    result = bool(re.match(r'^[a-z]+$', s))
    print(result)
    return result

def match_all_uppercase(s: str) -> bool:
    """
    Match strings that contain only uppercase letters.
    """
    result = bool(re.match(r'^[A-Z]+$',s))
    return result

def match_email_format(s: str) -> bool:
    """
    Match a valid email address format (e.g., example@domain.com).
    """
    result = bool(re.match(r'^[\w\.-]+@[\w\.-]+\w\.com$', s))
    return result

def match_us_phone(s: str) -> bool:
    """
    Match a US phone number format: 123-456-7890
    """
    result = bool(re.match(r'^(\d{3})-(\d{3})-(\d{4})',s))
    return result

def match_date_mmddyyyy(s: str) -> bool:
    """
    Match a date in the format MM/DD/YYYY.
    """
    result = bool(re.match(r'^(0[1-9]|1[1-2])/([0-2][0-9]|3[0-1])/(\d{4})', s))
    return result

def match_postal_code(s: str) -> bool:
    """
    Match a 5-digit US ZIP code.
    """
    result = bool(re.match(r'^(\d{5}$)',s))
    return result

def match_hex_color(s: str) -> bool:
    """
    Match a hex color code (e.g., #FFF or #FFFFFF).
    """
    result=bool(re.match(r'^#(\w+|W+)$', s))
    return result

def match_time_24h(s: str) -> bool:
    """
    Match a time in 24-hour format (e.g., 14:30).
    """
    result = bool(re.match(r'^(0[1-9]|1[0-9]|2[0-3]):([0-5][0-9])',s))
    return result

def match_valid_username(s: str) -> bool:
    """
    Match a username that contains only letters, numbers, and underscores, and is 3–16 characters long.
    """
    result = bool(re.match(r'^[a-zA-Z0-9_]{3,16}$',  s))
    return result


def match_url(s: str) -> bool:
    """
    Match a simple HTTP or HTTPS URL.
    """
    result = bool(re.match(r'^[https?]', s))
    return result

def match_credit_card(s: str) -> bool:
    """
    Match a credit card number format: 4 groups of 4 digits separated by spaces or hyphens.
    """
    result = bool(re.match(r'^(\d{4})([-|\s])(\d{4})([-|\s])(\d{4})([-|\s])(\d{4})$', s))
    return result

def match_hashtag(s: str) -> bool:
    """
    Match a valid hashtag that begins with # and is followed by alphanumeric characters.
    """
    result = bool(re.match(r'^#[\d\w]+$',s))
    return result

def match_ip_address(s: str) -> bool:
    """
    Match a valid IPv4 address.
    """
    result = bool(re.match(r'^(\d{3}).(\d{3}).(\d*).([\d*])$', s))
    return result

def match_strong_password(s: str) -> bool:
    """
    Match a strong password (at least 8 characters, one uppercase, one lowercase, one digit, and one special character).
    """
    result =bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$', s))
    return result
