class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    pass
try:
    text = input('Введите что-нибудь -->')
    if len(text) < 3:
        raise ShortInputException()
    # Здесь может происходить обычная работа
except ShortInputException as ex:
    ex("Маленькая длина текста: " % len(text))
else:
    print('Не было исключений.')