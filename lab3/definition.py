class Software:
    __license = False
    __open_source = False

    def __init__(self):
        print("Constructor Software")
        self.__license = True
        self.__open_source = True

    def __del__(self):
        print("Destructor Software")


class TextProcessor(Software):
    __gui = False

    def __init__(self):
        print("Constructor TextProcessor")
        __GUI = True

    def __del__(self):
        print("Destructor TextProcessor")


class Word(TextProcessor):
    def __init__(self):
        print("Constructor Word")

    def __del__(self):
        print("Destructor Word")


class Virus(Software):
    __reestr = False
    def __init__(self):
        print("Constructor Virus")
        __reestr = True

    def __del__(self):
        print("Destructor Virus")


class Game(Software):
    __free = False
    __people = 0
    __name = ""

    def __init__(self, peop, str):
        print("Constructor Game")
        self.__free = True
        self.__people = peop
        self.__name = str

    def __del__(self):
        print("Destructor Game")

    def get_name(self):
        return self.__name


class Saper(Game):
    def __init__(self):
        print("Constructor Saper")

    def __del__(self):
        print("Destructor Saper")


class Developer:
    __count = 0
    def __init__(self):
        print("Constructor Developer")
        self.__count = 1

    def __del__(self):
        print("Destructor Developer")

    def add_human(self):
        return self.__count


class Development:
    def __init__(self, game, count):
        print("Constructor Development")
        self.nameGame = game
        self.people = count

    def add_dev(self):
        self.people += Developer().add_human()

    def display(self):
        print("Name game " + self.nameGame)
        print("Developers in team " + str(self.people))

    def __del__(self):
        print("Destructor Development")

