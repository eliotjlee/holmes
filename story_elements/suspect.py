class Suspect:
    def __init__(self, name, bio, tags, victim_connection, guilty, id):
        self.name = name
        self.bio = bio
        self.tags = tags
        self.victim_connection = victim_connection
        self.guilty = guilty
        self.id = id
        self.memory_path = ""

    def get_info(self):
        info = f"Name: {self.name}\n"
        info += f"Bio: {self.bio}\n"
        info += f"Tags: {self.tags}\n"
        info += f"Victim connection: {self.victim_connection}\n"
        info += f"Guilty: {self.guilty}\n"
        return info
    
    def get_info_no_guilty(self):
        info = f"Name: {self.name}\n"
        info += f"Bio: {self.bio}\n"
        info += f"Tags: {self.tags}\n"
        info += f"Victim connection: {self.victim_connection}\n"
        return info


    def __getstate__(self):
        # Return the object's state as a dictionary
        return {
            'name': self.name,
            'bio': self.bio,
            'tags': self.tags,
            'victim_connection': self.victim_connection,
            'guilty': self.guilty,
            'id': self.id,
            'memory_path': self.memory_path
        }

    def __setstate__(self, state):
        # Restore the object's state from the given dictionary
        self.name = state['name']
        self.bio = state['bio']
        self.tags = state['tags']
        self.victim_connection = state['victim_connection']
        self.guilty = state['guilty']
        self.id = state['id']
        self.memory_path = state['memory_path']
