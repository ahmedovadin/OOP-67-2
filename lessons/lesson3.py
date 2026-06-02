import random
import string
class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance #_ means protected
        self.__password = password

    def get_user_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return 'Не верный пароль'
    def __random_pass(self):
        data = string.ascii_letters + string.digits
        password = ''.join(random.choice(data) for _ in range(6))
        return password

    def get_random_pass(self):
        return self.__random_pass()

# ardager = BankAccount('Adrager', "123321", 1000)



from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def move(self):
        return "Step"

    def make_sound(self):
        return "Gaf Gaf"

gufi = Dog()

# print(gufi.move())
# print(gufi.make_sound())

class SendSms(ABC):
    @abstractmethod
    def send_otp_to_phone(self, phone):
        pass

class KGSendSms(SendSms):
    def request(self, data):
        pass
    def send_otp_to_phone(self, phone):
        data = f'''
            <Phone>{phone}</Phone>
            <Text>Ваш код; 123321</Text>
        '''
        self.request(data)

class RUSendSms(SendSms):
    def request(self, data):
        pass
    def send_otp_to_phone(self, phone):
        data = {
            'phone': phone,
            'text': 'Ваш код: 123321'
        }
        self.request(data)