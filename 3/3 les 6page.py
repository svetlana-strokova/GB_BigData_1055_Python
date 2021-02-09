# 6 Задание Реализовать функцию int_func(), принимающую слово из маленьких
#латинских букв и возвращающую его же, но с прописной первой буквой.

def int_func(word):
    latin_chars = 'mnbvcxzasdfghjklpoiuytrewq'
    return word.title() if not set (word).difference(latin_chars) else False



#    word = input('Введите слово')
#    print(word.title())
#    return
#int_func()