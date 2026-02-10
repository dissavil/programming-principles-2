def register_user(username, email, role="user"):
    return {
        "username": username,
        "email": email,
        "role": role
    }

print(register_user("dias", "dias@mail.com"))
print(register_user("admin", "admin@mail.com", "admin"))
