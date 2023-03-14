"""labwork"""


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

    def get_defeated(self):
        """ """
        return Enemy.defent


class Boss(Enemy):
    """ """
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 1

    def fight(self, fight_with):
        """ """
        if fight_with in self.weakness:
            print("Yes! You got 50% of enemy's life!")
            self.weakness.remove(fight_with)
            self.health = 0.5
            Enemy.defent += 0.5
        return self.weakness == []

    def get_health(self):
        return self.health

class Item():
    """Item"""
    def __init__(self, name):
        """ """
        self.name = name

    def set_description(self, description):
        """ """
        self.description = description
    
    def get_name(self):
        """ """
        return self.name

    def describe(self):
        """ """
        print(f"The [{self.name}] is here - {self.description}")


class Friend():
    """ """
    def __init__(self, name, description):
        """ """
        self.name = name
        self.description = description
    
    def get_name(self):
        """ """
        return self.name
    
    def set_conversation(self, conversation):
        """ """
        self.conversation = conversation
    
    def set_description(self, description):
        """ """
        self.description = description
    
    def set_hint(self, hint):
        """ """
        self.hint = hint
    
    def get_hint(self):
        """ """
        print(f"The hint is: {self.hint}")

    def set_item(self, item):
        """ """
        self.item = item
    
    def get_item(self):
        """ """
        return self.item
    
    def describe(self):
        """ """
        print(f"The [{self.name}] is here for you - {self.description}")
    
    def talk(self):
        """ """
        print(f"[{self.name} says]: {self.conversation}")


class Weapon(Item):
    def __init__(self, name):
        super().__init__(name)


class Support(Item):
    def __init__(self, name):
        super().__init__(name)