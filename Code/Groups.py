from Code import Trips


class Groups:
    def __init__(self):
        self.Nombre = None
        self.participantes = dict
        self.Admin = None
        self.picture = None
        self.Description = None
        self.Recorrido = None
        self.chat = None
        self.historial = None
        self.commit_trips = Trips.Commited_trip()
        self.queue_trips = None
        self.rule_set = None

    def edit_Description(self, new_description):
        self.Description = new_description

    def edit_Name(self, new_name):
        self.Nombre = new_name

    def add_participant(self):
        pass

    def kick_participant(self):
        pass

    def create_free_ride_trip(self):
        pass

    def remove_free_ride_trips(self):
        pass

    def create_commit_trip(self):
        pass

    def edit_commit_trip(self):
        pass

    def find_trip(self):
        pass


