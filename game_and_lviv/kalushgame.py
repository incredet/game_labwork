"""labwork"""


class Room():
    """This is a class for room with actions in it."""
    def __init__(self, name):
        """init function for Room class
        attributes:
        linked_rooms
        name
        character
        item
        """
        self.linked_rooms = []
        self.name = name
        self.character = None
        self.item = None
        self.description = None

    def set_description(self, description):
        """this func sets description attribute for Room class"""
        self.description = description

    def link_room(self, other, path):
        """this func links one room to another using diff directions"""
        self.linked_rooms.append([other, path])

    def set_character(self, character):
        """this func sets character attribute for class item"""
        self.character = character

    def get_item(self):
        """gets item attribute from class"""
        return self.item

    def get_details(self):
        """this func returns some detail about class instance"""
        print(self.description)
        for room in self.linked_rooms:
            print("The " + room[0].name + " is " + room[-1])

    def get_character(self):
        """gets character attribute from class"""
        return self.character

    def set_item(self, item):
        """sets item attribute in class"""
        self.item = item

    def move(self, direction):
        """this func is used to move from one place to another"""
        for room in self.linked_rooms:
            if room[-1] == direction:
                return room[0]
        return self


class Enemy():
    """Enemy class. Used for all types for Enemies"""
    defent = 0

    def __init__(self, name, description):
        """init function for enemy class"""
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        """sets conversation attribute for class instance"""
        self.conversation = conversation

    def set_weakness(self, weakness):
        """sets weakness object attribute for class object"""
        self.weakness = weakness

    def describe(self):
        """used for describing the Enemy class object"""
        print(self.name + " is here!")
        print(self.description)

    def talk(self):
        """used for talking to Enemy object"""
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with):
        """used for fighting with Enemy instance"""
        print(f"You fend {self.name} off with the {fight_with}")
        if fight_with == self.weakness:
            Enemy.defent += 1
            return True
        return False

    def get_defeated(self):
        """used for counting loses of enemy"""
        return Enemy.defent


class Boss(Enemy):
    """This is the Boss. Has two lives"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 1

    def fight(self, fight_with):
        """fight function. slightly different because this enemy has two lives"""
        if fight_with in self.weakness:
            if self.health == 1:
                print("Yes! You got 50% of enemy's life!")
            elif self.health == 0.5:
                print("Yes! You got 100% of enemy's life!")
            self.weakness.remove(fight_with)
            self.health = 0.5
            Enemy.defent += 0.5
        return self.weakness == []

    def get_health(self):
        """gets health attribute from class"""
        return self.health

class Item():
    """Item. Can be anything."""
    def __init__(self, name):
        """init func
        attributes:
        name
        description
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """sets description attribure for class instance"""
        self.description = description

    def get_name(self):
        """gets name attribute from class"""
        return self.name

    def describe(self):
        """used for describing an item"""
        print(f"The [{self.name}] is here - {self.description}")


class Friend():
    """Friend class"""
    def __init__(self, name, description):
        """init func
        attributes:
        name
        description
        item
        conversation
        """
        self.name = name
        self.description = description
        self.item = None
        self.conversation = None
        self.hint = None

    def get_name(self):
        """gets name attribute"""
        return self.name

    def set_conversation(self, conversation):
        """sets conversation attribute"""
        self.conversation = conversation

    def set_description(self, description):
        """sets description attribute for class instance"""
        self.description = description

    def set_hint(self, hint):
        """sets hint description for class instance"""
        self.hint = hint

    def get_hint(self):
        """gets hint attribute"""
        print(f"The hint is: {self.hint}")

    def set_item(self, item):
        """sets item attribute"""
        self.item = item

    def get_item(self):
        """gets item attribute"""
        return self.item

    def describe(self):
        """used for describing the class instance"""
        print(f"The [{self.name}] is here for you - {self.description}")

    def talk(self):
        """used for talking to a Friend instance"""
        print(f"[{self.name} says]: {self.conversation}")
