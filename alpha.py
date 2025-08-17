import itertools
import string

letters_digits = string.ascii_lowercase + string.ascii_uppercase + string.digits
underscore = "_"

def is_valid(username: str) -> bool:
    if len(username) < 3 or len(username) > 20:
        return False
    if username.startswith("_") or username.endswith("_"):
        return False
    if username.count("_") > 1:
        return False
    return True

def username_generator():
    chars = letters_digits + underscore
    length = 3
    while length <= 20:
        for combo in itertools.product(chars, repeat=length):
            username = "".join(combo)
            if is_valid(username):
                yield username
        length += 1

def main():
    limit = 100000
    with open("usernames.txt", "w", encoding="utf-8") as f:
        gen = username_generator()
        for i, username in enumerate(gen, start=1):
            f.write(username + "\n")
            if i >= limit:
                break

if __name__ == "__main__":
    main()
