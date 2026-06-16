# Часть 1 - Внешние зависимости
from faker import Faker
from faker.providers import internet

# Эта библиотека нужна для генерации фейковых данных для отображения
fake = Faker()
fake.add_provider(internet)

print(fake.ipv4_private())

# Эта библиотека нужна для вывода цветного текста в терминале, окрашивания
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

# Эта библиотека нужна для отправки HTTP запросов и упрощенного использования
import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

# Часть 2 - Алгоритм (LeetCode)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
