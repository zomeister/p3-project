
class Candidate():
    def __init__(self, name, position, info):
        self.name = name
        self.position = position
        self.info = info
        self.votes = 0
        
    def get_num_votes(self):
        return self.votes
    def get_name(self):
        return self.name
    def get_position(self):
        return self.position
    def get_info(self):
        return self.info
    
    def increment_vote(self):
        self.votes += 1