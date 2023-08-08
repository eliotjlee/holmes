class Suspect:
    def __init__(self, name, bio, tags, victim_connection, guilty, id):
        self.name = name
        self.bio = bio
        self.tags = tags
        self.victim_connection = victim_connection
        self.guilty = guilty
        self.id = id

    def get_info(self):
        info = f"Name: {self.name}\n"
        info += f"Bio: {self.bio}\n"
        info += f"Tags: {self.tags}\n"
        info += f"Victim connection: {self.victim_connection}\n"
        info += f"Guilty: {self.guilty}\n"
        return info
