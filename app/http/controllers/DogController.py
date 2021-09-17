""" A DogController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Dog import Dog


class DogController(Controller):
    
    def __init__(self, request:Request):
        self.request = request


    def show(self):
        id = self.request.param("id")
        return Dog.where("id", id).get()

    def index(self):
        return Dog.all()

    def create(self):
        dog = self.request.only("name", "age")
        return Dog.create(dog)

    def update(self):
        id = self.request.param("id")
        dog = self.request.only("name", "age")
        Dog.where("id",id).update(dog)
        return Dog.where("id", id).get()


    def destroy(self):
        id = self.request.param("id")
        dog = Dog.where("id", id).get()
        Dog.where("id",id).delete()
        return dog