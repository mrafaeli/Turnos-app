import itertools

class User():
    new_id = itertools.count()
    def __init__(self, info):
       # self.commited_trips = {}
        self.likes = 0
        self.dislikes = 0
        self.groups = []
        self._id = next(User.new_id)
        self.user_data = info

    def give_like(self):
        self.likes += 1

    def give_dislike(self):
        self.dislikes += 1

    def join_trip(self):
        pass

    def leave_trip(self):
        pass

    def join_group(self):
        pass

    def leave_group(self):
        pass

    def queue_for_trip(self, group, hora_salida, delay, es_ida):
        pass

