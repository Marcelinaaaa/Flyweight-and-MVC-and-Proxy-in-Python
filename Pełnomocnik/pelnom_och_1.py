from abc import ABC, abstractmethod


class SensitiveInfo(ABC):
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    @abstractmethod
    def metodaabstrakcyjna(self):
        pass

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')

    def delete(self, user):
        self.users.remove(user)
        print(f'Deleted user {user}')


class Info(SensitiveInfo):
    """protection proxy to SensitiveInfo"""
    def metodaabstrakcyjna(self):
        pass

    def __init__(self):
        super().__init__()
        #self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        super().read()
        #self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        super().add(user) if sec == self.secret else print("That's wrong!")
        #self.protected.add(user) if sec == self.secret else print("That's wrong!")

    def delete(self, user):
        super().delete(user)
        #self.protected.delete(user)


def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. quit |==| 4. remove')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        elif key == '4':
            name = input('choose username: ')
            info.delete(name)
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    main()
    #a = SensitiveInfo()

# Należało zaimportować pakiety: ABC oraz abstractmethod.
# Następnie w klasie bazowej (SensitiveInfo), która teraz dziedziczy po sztucznej klasie ABC
# zdefiniowana została metoda abstrakcyjna, opatrzona dekoratorem @abstractmethod.
# Poprzez to stała się ona klasą abstrakcyjną i nie możemy stworzyć instancji tej klasy bazowej.
# Klasa Info dziedziczy po SensitiveInfo, a także nadpisuje jej metody.
# Dzięki temu mamy możliwość odczytywania, dodawania, usuwania użytkowników i wyjścia z programu.
#