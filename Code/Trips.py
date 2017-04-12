
#viaje auto
class Car():
    def __init__(self, price, space, pilot):
        self.avalaible_space = space
        self.is_full = False
        self.price = price
        self.pilot = pilot
        self.passengers = list
        self.destino = None
        self.punto_inicio = None
        self.hora_salida = None
        self.started = False
        self.finished = False
        self.automatic_add = True

    def delete_passenger(self, passenger):
        #Aca falta borrar passenger
        if len(self.passengers) < self.avalaible_space:
            self.is_full = False

    def add_passenger(self, passenger):
        if not self.is_full:
            pass
        #ACA FALTA AGREGAR EL PASSENGER
        if len(self.passengers) >= self.avalaible_space:
            self.is_full = True

    def start_trip(self):
        self.started = True
        self.alert_passengers()  #Alert message...

    def alert_passengers(self, message=None, passenger=None):
        if not passenger:
            #Se manda el mensaje a todos los pasajeros
            pass
        else:
            #Mandamos el mensaje al pasajero indicado
            pass

    def end_trip(self):
        self.started = True
        self.finished = True

        self.alert_passengers()  # Alert message...

    def automatic_switch(self):
        if self.automatic_add:
            self.automatic_add = False
        else:
            self.automatic_add = True






#viajes constantes
class Commited_trip():
    def __init__(self):
        self.registro = dict
        self.open = True

    def reset_trip(self):
        pass

    def close_inscription(self):
        self.open = False
        #mandar señal para cerrar add option en GUI

    def rename_trip(self):
        pass

    def member_join(self, user, driver_schedule, passenger_schedule):
        pass

    def member_quit(self, user):
        pass
