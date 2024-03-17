import re

def extract_phone_numbers(text):
    # Remove word boundaries
    pattern = r'\d{2,5}-\d{1,4}-\d{4}'
    return re.findall(pattern, text)

# Usage examples
text = "For inquiries, please call 0120-000-0000. Also, our office can be reached at 03-1234-5678."
print(extract_phone_numbers(text))
