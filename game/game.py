"""game.py"""


class Room():
    """Room class"""
    def __init__(self, name):
        """init func for class Room
        attributes:
        linked rooms
        name
        character
        item
        description
        """
        self.linked_rooms = []
        self.name = name
        self.character = None
        self.item = None
        self.description = None

    def set_description(self, description):
        """sets description attribute for class instance"""
        self.description = description

    def link_room(self, other, path):
        """func is used to link different rooms to each other"""
        self.linked_rooms.append([other, path])

    def set_character(self, character):
        """sets character attribute"""
        self.character = character

    def get_item(self):
        """gets item attribute"""
        return self.item

    def get_details(self):
        """used for getting detailed info about class instance"""
        print(self.description)
        for room in self.linked_rooms:
            print("The " + room[0].name + " is " + room[-1])

    def get_character(self):
        """gets character attribute"""
        return self.character

    def set_item(self, item):
        """sets item attribute"""
        self.item = item

    def move(self, direction):
        """used for moving from one room to another"""
        for room in self.linked_rooms:
            if room[-1] == direction:
                return room[0]
        return self


class Enemy():
    """Enemy"""
    defent = 0
    def __init__(self, name, description):
        """init func
        attributes:
        name
        description
        conversation
        weakness
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        """sets conversation attribute"""
        self.conversation = conversation

    def set_weakness(self, weakness):
        """sets weakness attribute"""
        self.weakness = weakness

    def describe(self):
        """used for describing class instance"""
        print(self.name + " is here!")
        print(self.description)

    def talk(self):
        """used for talking to class instance"""
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with):
        """used to fighting with Enemy instance"""
        print(f"You fend {self.name} off with the {fight_with}")
        if fight_with == self.weakness:
            Enemy.defent += 1
            return True
        return False

    def get_defeated(self):
        """determines if the enemies lost"""
        return Enemy.defent


class Item():
    """Item class"""
    def __init__(self, name):
        """init function
        attributes:
        name
        description
        """
        self.name = name
        self.description = None

    def get_name(self):
        """gets name attribute"""
        return self.name

    def set_description(self, description):
        """sets description attribute"""
        self.description = description

    def describe(self):
        """used for describing Item instance"""
        print(f"The [{self.name}] is here - {self.description}")
