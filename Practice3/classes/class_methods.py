class User:
    count = 0

    def __init__(self, username):
        self.username = username
        User.count += 1

    @classmethod
    def total_users(cls):
        return cls.count

u1 = User("a")
u2 = User("b")

print(User.total_users())
