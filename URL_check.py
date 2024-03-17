import re

def extract_urls(text):
    pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=]*)?'
    return re.findall(pattern, text)

# Usage examples
text = "For more details, please visit https://example.com. Additionally, support is available at http://support.example.com."
print(extract_urls(text))