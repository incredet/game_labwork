"""main.py"""
import kalushgame

library = kalushgame.Room("Бібліотека ім. Тараса Шавченка")
library.set_description("Тут дуже багато книжок")

heroes_square = kalushgame.Room("Площа Героїв")
heroes_square.set_description("Головна площа Калуша. Тут багато дивних людей...")

drug_store = kalushgame.Room("Аптека '36.6'")
drug_store.set_description("Тут кожним лікам знайдуть дорожчу заміну!")

church = kalushgame.Room("Церква")
church.set_description("It's a safe place! Не хвилюйся :)")

palace = kalushgame.Room("Мінерал")
palace.set_description("Це палац культури! Тут дуже культурні люди!")

coffee_shop = kalushgame.Room("Кав'ярня 'Кориця'")
coffee_shop.set_description("Тут можна збиратися після навчання для... навчання...")

grammar_school = kalushgame.Room("Калуська гімназія ім. Дмитра Бахматюка")
grammar_school.set_description("Обережно!!! Тут багато розумних людей!!!")

#linking all the rooms to each other
# library.link_room(grammar_school, 'east')
library.link_room(heroes_square, 'south')

heroes_square.link_room(library, 'north')
heroes_square.link_room(church, 'east')
heroes_square.link_room(drug_store, 'south')

drug_store.link_room(heroes_square, 'north')

church.link_room(heroes_square, 'west')
church.link_room(palace, 'east')

palace.link_room(church, 'west')
palace.link_room(coffee_shop, 'north')

coffee_shop.link_room(palace, 'south')
coffee_shop.link_room(grammar_school, 'west')

grammar_school.link_room(coffee_shop, 'east')
grammar_school.link_room(library, 'west')

# setting enemies
cymbal = kalushgame.Enemy("Цимбал", "Дуже поважний мужчина, але є один нюанс")
cymbal.set_conversation("Добренький день, мілєді")
cymbal.set_weakness("чічка")
heroes_square.set_character(cymbal)

mych = kalushgame.Enemy("Лайдак Михайло", "Точно не хоче вкрасти ваші речі.")
mych.set_conversation("Скіки грошей маєте?")
mych.set_weakness("камінь")
palace.set_character(mych)

teacher = kalushgame.Boss("Марія Іванівна", "Без форми повз неї краще не проходити...")
teacher.set_conversation("По газонах не ходити!!!")
teacher.set_weakness(["кавуся", "книжка"])
grammar_school.set_character(teacher)

# setting weapons
book = kalushgame.Weapon("книжка")
book.set_description("Дуже цінна книжка. 'Алгебра. 10 клас.'")
library.set_item(book)

flower = kalushgame.Weapon("чічка")
flower.set_description("Ну дуже-дуже гарна чічка!")

coffee = kalushgame.Weapon("кавуся")
coffee.set_description("Дуже гарна КАЛУСЬКА кавуся!!!")
coffee_shop.set_item(coffee)

rock = kalushgame.Weapon("камінь")
rock.set_description("Камінь. Можна кинути.")
heroes_square.set_item(rock)

# setting support
medicine = kalushgame.Support("ліки")
medicine.set_description("Дуже ефективні ліки. Майже подорожник")

# setting friends
priest = kalushgame.Friend("Педрос", "Місцевий священник. Дуже-дуже привітний!!!")
priest.set_conversation("Слава Ісусу Христу!!!")
priest.set_hint("Рухайтесь як серце підкаже! З Богом!")
priest.set_item(flower)
#priest.get_item()
church.set_character(priest)

pharmacist = kalushgame.Friend("Фармація", "Жіночка у білому халаті.")
pharmacist.set_conversation("Атоксілу немає")
pharmacist.set_hint("Не час лікує, ліки лікують!")
pharmacist.set_item(medicine)
#priest.get_item()
drug_store.set_character(pharmacist)


first = True
dead = False
current_room = library
sumka = []
print("Hello!!! You have to kill all enemies and come back here! Good luck!\n")
while dead == False:
    inhabitant = current_room.get_character()
    if current_room == library and first == False and loses == 3:
        print("Congrats!!! You did it!!!")
        dead = True
    else:
        print('\n')
        print("available commands:\n north, south, east, west\n ask for hint, ask for help\n talk, fight, take\n")
        current_room.get_details()
        
        if inhabitant is not None:
            inhabitant.describe()
        
        item = current_room.get_item()
        if item is not None:
            item.describe()
        
        command = input("> ")
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
            first = False

        elif command == "ask for hint":
            if isinstance(inhabitant, kalushgame.Friend):
                inhabitant.get_hint()
            else:
                print("No one to ask here")
                dead = True

        elif command == "ask for help":
            if isinstance(inhabitant, kalushgame.Friend):
                item = inhabitant.get_item()
                if item is not None:
                    print(f"I have a {item.get_name()} for you")
                    print("Put the " + item.get_name() + " in your сумка")
                    sumka.append(item.get_name())
                    inhabitant.set_item(None)
                else:
                    print("Nothing for you(")
            else:
                print("No one to ask here")
                dead = True

        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()

        elif command == "fight":
            if inhabitant is not None:
                if isinstance(inhabitant, kalushgame.Boss):
                    print("What will you fight with?")
                    fight_with = input('> ')
                    if fight_with in sumka:
                        if inhabitant.fight(fight_with) == True:
                            print("Hooray, you won the fight!")
                            current_room.character = None
                            loses = inhabitant.get_defeated()
                            if loses == 3:
                                print("Congratulations, you have vanquished the enemy horde!")
                        elif inhabitant.fight(fight_with) == False and inhabitant.get_health() == 0.5:
                            print("Enemy is not dead yet... Come again!")
                        else:
                            if "ліки" in sumka:
                                print("Oh dear, you lost the fight.")
                                print("You got one more chance! Do you want to use it?")
                                ans = input("> ")
                                if ans == "yes" or ans == "y" or ans == "так":
                                    print("Good Luck!")
                                else:
                                    print("Oh dear, you lost the fight.")
                                    print("That's the end of the game")
                                    dead = True
                            else:
                                print("Oh dear, you lost the fight.")
                                print("That's the end of the game")
                                dead = True
                    else:
                        print("You don't have a " + fight_with)
                elif isinstance(inhabitant, kalushgame.Enemy):
                    print("What will you fight with?")
                    fight_with = input('> ')
                    if fight_with in sumka:
                        if inhabitant.fight(fight_with) == True:
                            print("Hooray, you won the fight!")
                            current_room.character = None
                            loses = inhabitant.get_defeated()
                            if loses == 3:
                                print("Congratulations, you have vanquished the enemy horde!")
                        else:
                            if "ліки" in sumka:
                                print("Oh dear, you lost the fight.")
                                print("You got one more chance! Do you want to use it?")
                                ans = input("> ")
                                if ans == "yes" or ans == "y" or ans == "так":
                                    print("Good Luck!")
                                else:
                                    print("Oh dear, you lost the fight.")
                                    print("That's the end of the game")
                                    dead = True
                            else:
                                print("Oh dear, you lost the fight.")
                                print("That's the end of the game")
                                dead = True
                    else:
                        print("You don't have a " + fight_with)
                else:
                    print("There is no one here to fight with! They want to be friends!")
            else:
                print("There is no one here to fight with")

        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your сумка")
                sumka.append(item.get_name())
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        else:
            print("I don't know how to " + command)
