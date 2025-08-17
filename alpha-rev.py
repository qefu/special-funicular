import itertools

# Allowed characters (no underscore at front or end initially)
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

# Validate username against rules
def is_valid(username: str) -> bool:
    if len(username) < 3 or len(username) > 20:
        return False
    if username[0] == '_' or username[-1] == '_':
        return False
    if username.count('_') > 1:
        return False
    return True

# Generator for usernames in reverse lexicographic order
def username_generator():
    length = 20
    while length >= 3:
        for combo in itertools.product(reversed(CHARS), repeat=length):
            username = ''.join(combo)
            if is_valid(username):
                yield username
        length -= 1

# Write first 100,000 usernames in reverse order
with open("usernames_reverse.txt", "w", encoding="utf-8") as f:
    gen = username_generator()
    for i in range(100_000):
        f.write(next(gen) + "\n")
