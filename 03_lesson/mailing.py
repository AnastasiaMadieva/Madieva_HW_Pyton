from adress import Adress

class Mailing:
    def __init__ (self,to_address, from_address, cost, track):
        self.to_adr = to_address
        self.from_adr = from_address
        self.cost = cost
        self.track = track

    def __str__ (self):
        return f"Отправление: {self.track} из {self.to_adr} в {self.from_adr} стоит {self.cost} рублей"
