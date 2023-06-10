class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        self.members.append(musician)

    def play(self):
        if len(self.members) > 0:
            return f"The band {self.name} is playing!"
        else:
            return f"The band {self.name} has no members."

    def __str__(self):
        member_list = "\n".join([str(member) for member in self.members])
        return f"Band: {self.name}\nMembers:\n{member_list}"