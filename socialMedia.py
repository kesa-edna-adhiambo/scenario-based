class SocialMediaApp:
    def __init__(self):
        self.followers = {}

    def add_follower(self, user, follower):
        if user not in self.followers:
            self.followers[user] = set() 
        self.followers[user].add(follower)

    def get_followers(self, user):
        return self.followers.get(user, set())


app = SocialMediaApp()
app.add_follower("user1", "Edna")
app.add_follower("user1", "Kesa")
app.add_follower("user2", "Brenda")
app.add_follower("user2", "Levin")
app.add_follower("user3", "Edna")
app.add_follower("user3", "Brenda")


print(app.get_followers("user1"))
print(app.get_followers("user2"))
print(app.get_followers("user3"))




