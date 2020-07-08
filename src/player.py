# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, startingroom):
        self.name = name
        self.startingroom = startingroom
   
    def __str__(self):
        output = f"{self.name}, Current location {self.startingroom.name}"
        return output