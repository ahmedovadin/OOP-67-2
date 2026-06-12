import time

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

admin = User("Ardager", "admin")
user = User("Bek", "user")

def is_admin(func):
    def wrapper(user_param):
        if user_param.role == "admin":
            func(user_param)
        else:
            print('У вас нет доступа')
    return wrapper

@is_admin
def delete_video(user):
    print('Видео удалено')

delete_video(user)
delete_video(admin)

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()  # время после
        print(f'Время выполнения: {round(end - start, 1)} секунд')
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print('Видео загружено')

download_video()

