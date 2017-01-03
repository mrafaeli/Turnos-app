

class User():
    def __init__(self):
        self._id = None
        self.name = None
        self.viajes_recurrentes = {}
        self.rating = 0
        self.rated_by = 0


    def update_rating(self, value):
        self.rating = (value + self.rating * self.rated_by) / (self.rated_by + 1)
        self.rated_by += 1

