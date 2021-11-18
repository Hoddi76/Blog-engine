from sqlalchemy.sql.functions import current_timestamp

from app import db

from datetime import datetime


### Blog ###


def slugify(name):
    """
    Генерируем слаг
    Slug generate и
    транслитим его
    :param name = строке которую надо транслитить
    """
    # Словарь с заменами
    dictionary = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
                  'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                  'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
                  'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
                  'ю': 'u', 'я': 'ya', 'А': 'a', 'Б': 'b', 'В': 'v', 'Г': 'g', 'Д': 'd', 'Е': 'e', 'Ё': 'e',
                  'Ж': 'zh', 'З': 'z', 'И': 'i', 'Й': 'i', 'К': 'k', 'Л': 'l', 'М': 'm', 'Н': 'n',
                  'О': 'o', 'П': 'p', 'Р': 'r', 'С': 's', 'Т': 't', 'У': 'u', 'Ф': 'f', 'Х': 'h',
                  'Ц': 'c', 'Ч': 'ch', 'Ш': 'sh', 'Щ': 'scz', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'e',
                  'Ю': 'u', 'Я': 'ya', ',': '', '?': '', ' ': '-', '~': '', '!': '', '@': '', '#': '',
                  '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '-', '=': '', '+': '',
                  ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
                  '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
                  'Є': 'e'}
    # Циклически заменяем все буквы в строке
    for key in dictionary:
        name = name.replace(key, dictionary[key])
    return name.lower()


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    link_image = db.Column(db.String(200))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=current_timestamp())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)
