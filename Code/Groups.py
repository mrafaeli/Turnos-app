from Code import Trips
from queue import deque
import threading
import time


class Groups:
    def __init__(self, name, admin, desc=None):
        self.open = True
        self.nombre = name
        self.admin = admin
        self.participantes = {}
        self.picture = None
        self.description = desc
        self.recorrido = None
        self.chat = None
        self.historial = None
        self.rule_set = "Private"   #Private/public


        self.avalaible_cars = []
        self.full_cars = []
        self.waiters = []

        update_thread = threading.Thread(target=self.update_waiters(), name="Update waiters", daemon=True)
        update_thread.start()


    def create_waitlist(self):
        pass

    def edit_description(self, new_description):
        self.description = new_description
        #send update

    def edit_name(self, new_name):
        self.nombre = new_name

    def add_participant(self, user):
        self.participantes[user._id] = user

    def kick_participant(self, user):
        del self.participantes[user._id]

    def create_free_ride_trip(self, car):
        pass
        #self.cars[car.hora_salida].append(car)

    def remove_free_ride_trips(self, car):
        pass
        #self.cars[car.hora_salida].remove(car)


    def update_waiters(self):
        while self.open:
            i = 0
            for waiter in self.waiters:
                self.check_waiters(waiter, i)
                i += 1
                #aca podria abrir otro thread que chequee para los ajustados.
    #input: lista,
    def check_waiters(self, waiter, i):
        #No adjust avalaible now
        time = waiter[0]
        n_car = 0
        for car in self.avalaible_cars:
            if car.time == time:  #me falta arreglar el adjust
                self.waiters.pop(i)  #me salgo de los waiters
                car.add_passenger(waiter)
                if car.is_full:



            n_car += 1

                #Chequeo si el auto esta lleno, si lo esta lo saco de los avalaible cars y lo meto a los fulls.

    def check_avalaible_cars(self):
        # Thread encargado de revisar los autos que no hayan partido, si partieron son borrados de la lista.
        pass

    def check_full_cars(self):
        pass

a = Groups("hola", "ed elric")