import re

# Task 1: Listing Numbers

# Task 2: Prime Numbers

# Task 3: Regular Expressions
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email")
    else:
        print("Invalid email")

validate_email("alex_wilber@contoso.com")
validate_email("alex_wilber@contoso")
validate_email("asdgdgdgdgdgdgdgdgdgdgdg")
validate_email("alexwilber@contoso.com")