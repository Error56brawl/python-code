emails = [
    "abc@gmail.com",
    "xyz@gmail.com",
    "pqr@gmail.com",
    "abc@gmail.com",
    "hello@gmail.com",
    "xyz@gmail.com"
]
seen = set()
duplicates = set()

for email in emails:
    if email in seen:
        duplicates.add(email)
    else:
        seen.add(email)

print("Duplicate emails:", duplicates)

