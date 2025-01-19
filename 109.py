import re

# Extract email addresses from a given string
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

# Example usage
sample_text = "Contact us at support@example.com or sales@example.com"
emails = extract_emails(sample_text)
print("Extracted email addresses:", emails)
