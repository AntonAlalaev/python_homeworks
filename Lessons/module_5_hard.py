from time import sleep


class User:
    def __init__(self, nik, password, age):
        self.nikname = nik
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nikname == other.nikname

    def __str__(self):
        return self.nikname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.videos = []

    def log_in(self, nikname, password):
        for item in self.users:
            if item.nikname == nikname and item.password == hash(password):
                self.current_user = item

    def register(self, nikname, password, age):
        user = User(nikname, password, age)
        if user in self.users:
            print(f"Пользователь {user.nikname} уже существует")
            self.current_user = user
        else:
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for item in args:
            if isinstance(item, Video):
                if not item in self.videos:
                    self.videos.append(item)

    def get_videos(self, word):
        cap_word = str(word).lower()
        video_list = []
        for item in self.videos:
            str_title = str(item.title).lower()
            if cap_word in str_title:
                video_list.append(item.title)
        return video_list

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for item in self.videos:
            str_title = str(item.title).lower()
            if str(title).lower() == str_title:
                if self.current_user.age < 18:
                    if item.adult_mode:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                for i in range(item.time_now, item.duration + 1):
                    print(i, ' ', end='')
                    sleep(1)
                print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
