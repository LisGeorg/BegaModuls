def pallindrom():
    word = str(input("Введите слово: "))
    rev = str(word())
    if word == rev:
        print("Паллиндрома", rev)
    else:
        print("Увы, не паллиндрома")
