import sqlite3

connect = sqlite3.connect('cinema.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR (50) NOT NULL,
        genre VARCHAR (50) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id  INTEGER NOT NULL,
        movie_id  INTEGER NOT NULL,
        rating FLOAT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )
''')

connect.commit()

# ЧАСТЬ 1 — СОЗДАНИЕ И ДАННЫЕ
def create_users():
    users = [
        ('Ardager',),
        ('Oleg',),
        ('Slava',),
        ('John',),
        ('Michael',),
    ]
    cursor.executemany(
        'INSERT INTO users(name) VALUES(?)',
        users
    )
    connect.commit()
    print('Пользователи созданы!!')

def create_movies():
    movies = [
        ('Adalin', 'romance, drama'),
        ('The Lord of the Rings', 'epic fantasy'),
        ('Aquaman', 'action, adventure, fantasy'),
        ('Forest Gump', 'comedy-drama'),
        ('Avatar', 'action')
    ]
    cursor.executemany(
        'INSERT INTO movies(title, genre) VALUES(?, ?)',
        movies
    )
    connect.commit()
    print('Фильмы созданы!!')

def create_reviews():
    reviews = [
        (1, 1, 9),  # Ardager (Adaline) 9
        (1, 2, 10),  # Ardager (LOTR) 10
        (2, 3, 7),  # Oleg (Aquaman) 7
        (2, 5, 8),  # Oleg (Avatar) 8
        (3, 2, 10),  # Slava (LOTR) 10
        (3, 4, 9),  # Slava (Forrest Gump) 9
        (4, 1, 6),  # John (Adaline) 6
        (4, 5, 8),  # John (Avatar) 8
        (5, 3, 7),  # Michael (Aquaman) 7
        (5, 4, 10),  # Michael (Forrest Gump) 10
        (5, 2, 9),  # Michael (LOTR) 9
    ]
    cursor.executemany(
        'INSERT INTO reviews(user_id, movie_id, rating) VALUES(?, ?, ?)',
        reviews
    )
    connect.commit()
    print('Отзывы созданы!!')

create_users()
create_movies()
create_reviews()

# ЧАСТЬ 2 — JOIN
def show_reviews():
    cursor.execute('''
           SELECT users.name, movies.title, reviews.rating
           FROM reviews
           JOIN users ON reviews.user_id = users.id
           JOIN movies ON reviews.movie_id = movies.id
       ''')

    result = cursor.fetchall()
    print('\nОтзывы:')
    for name, title, rating in result:
        print(f'{name}: {title} - {rating}')

def show_all_movies():
    cursor.execute('''
        SELECT users.name, movies.title, reviews.rating
        FROM movies
        LEFT JOIN reviews ON movies.id = reviews.movie_id
        LEFT JOIN users ON reviews.user_id = users.id
    ''')
    result = cursor.fetchall()
    print('\nВсе фильмы (даже без отзывов):')
    for name, title, rating in result:
        if rating is None:
            print(f'{title} - нет отзывов')
        else:
            print(f'{name}: {title} - {rating}')

show_reviews()
show_all_movies()

# ЧАСТЬ 3 — АГРЕГАЦИИ
def show_aggregation():
    cursor.execute('''
        SELECT AVG(rating), MAX(rating), MIN(rating)
        FROM reviews
    ''')
    avg, mx, mn = cursor.fetchone()
    print('\nАгрегации:')
    print(f'Средняя оценка: {round(avg, 2)}')
    print(f'Максимальная оценка: {mx}')
    print(f'Минимальная оценка: {mn}')

show_aggregation()