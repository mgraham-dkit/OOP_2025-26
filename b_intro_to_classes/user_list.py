from users import User

u1 = User("Michelle", "P4ssword1")
u2 = User("Michelle2", "Password")
u3 = User("Michelle3", "p4ssword1")
u4 = User("Michelle4", "P4PPPPPP1")
u5 = User("Michelle5", "P4ssw")

users = [u1, u2, u3, u4, u5]

#print(users)
for u in users:
    print(u)