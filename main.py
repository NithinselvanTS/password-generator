import secrets
import string

n = int(input("Password length: "))
c = string.ascii_letters + string.digits + string.punctuation
p = "".join(secrets.choice(c) for _ in range(n))
print("Generated password:", p)