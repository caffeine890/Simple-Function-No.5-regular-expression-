
# Python Regular Expression Examples

This repository contains Python scripts that demonstrate the use of regular expressions for various common tasks such as validating email addresses, extracting URLs, and finding phone numbers within text. Below is a brief overview of each script and its functionality.

## Scripts Overview

### 1. Email Address Validation (`mail_add_check.py`)

This script checks if an input email address is in a valid format using a regular expression. It matches email addresses that follow the general pattern of `username@domain.tld`, where:

- `username` can include alphanumeric characters, dots (.), underscores (_), percent signs (%), plus signs (+), and hyphens (-).
- `domain` consists of alphanumeric characters and hyphens (-).
- `tld` (top-level domain) is at least two characters long, consisting of letters only.

#### Usage Example

```python
email = "example@example.com"

print(is_valid_email(email))  # Outputs: True or False
```


### 2. URL Extraction (`URL_check.py`)

This script extracts URLs from a given text using a regular expression. It can match both HTTP and HTTPS URLs, including those with paths and query parameters. The pattern is designed to match URLs that:

- Start with `http://` or `https://`.
- Include domain names with alphanumeric characters and possibly hyphens (-).
- Optionally include paths, query parameters, and fragments.

#### Usage Example

```python
text = "Visit https://example.com or http://support.example.com for more information."
print(extract_urls(text))
```


### 3. Phone Number Extraction (`phone_num_check.py`)

This script extracts Japanese-style phone numbers from text. The regular expression matches phone numbers that:

- Start with a 2 to 5 digit area code.
- Followed by a 1 to 4 digit local exchange.
- End with a 4 digit number.
- Each section is separated by hyphens (-).

#### Usage Example

```python
text = "Contact us at 0120-000-0000 or visit our office at 03-1234-5678."
print(extract_phone_numbers(text)
```



## Requirements

- Python 3.x
- No external libraries are required as all scripts use the built-in `re` module for regular expressions.

## Note

These scripts are designed for educational purposes and to serve as a starting point for more complex regular expression tasks. Depending on your specific needs, the regular expressions may require adjustments.

