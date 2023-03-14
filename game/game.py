"""game.py"""


class Room():
    """Room"""
    def __init__(self, name):
        """ """
        self.linked_rooms = []
        self.name = name
        self.character = None
        self.item = None

    def set_description(self, description):
        """ """
        self.description = description

    def link_room(self, other, path):
        """ """
        self.linked_rooms.append([other, path])

    def set_character(self, character):
        """ """
        self.character = character

    def get_item(self):
        """ """
        return self.item

    def get_details(self):
        """ """
        print(self.description)
        for room in self.linked_rooms:
            print("The " + room[0].name + " is " + room[-1])

    def get_character(self):
        """ """
        return self.character

    def set_item(self, item):
        """ """
        self.item = item

    def move(self, direction):
        """ """
        for room in self.linked_rooms:
            if room[-1] == direction:
                return room[0]
        return self

defent = 0
class Enemy():
    """Enemy"""
    defent = 0
    def __init__(self, name, description):
        """ """
        self.name = name
        self.description = description

    def set_conversation(self, conversation):
        """ """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """ """
        self.weakness = weakness

    def describe(self):
        """ """
        print(self.name + " is here!")
        print(self.description)

    def talk(self):
        """ """
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with):
        """ """
        print(f"You fend {self.name} off with the {fight_with}")
        if fight_with == self.weakness:
            Enemy.defent += 1
            return True

    def get_defeated(self, defent = defent):
        """ """
        return Enemy.defent


class Item():
    """Item"""
    def __init__(self, name):
        """ """
        self.name = name

    def get_name(self):
        """ """
        return self.name

    def set_description(self, description):
        """ """
        self.description = description
    
    def get_name(self):
        """ """
        return self.name

    def describe(self):
        """ """
        print(f"The [{self.name}] is here - {self.description}")