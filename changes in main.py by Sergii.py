from servicenote import OPERATORS, note_book # додати 



def func_good_bye(*args):
    book.save(file_name)
    note_book.save_data() # додати 
    print(f"Good bye!")
    exit()


""" Так було:
def parser(text: str):
    for func in FUNCTIONS.keys():
        if text.startswith(func):
            return func, text[len(func) :].strip().split()


def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input.lower())
        current_func = FUNCTIONS.get(func)
        print(current_func(*data))

"""
# так треба ----->

def parser(text: str):
    for func in OPERATORS.keys(): # додати перевірку чи є функція у моєму словнику 
        if text.startswith(func):
            return func, text[len(func) :].strip().split()
        
    for func in FUNCTIONS.keys():
        if text.startswith(func):
            return func, text[len(func) :].strip().split()
    

def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input.lower())
        if func in FUNCTIONS:                     # додати виклик функції, залежно від словника  в якому вона знайдена
            current_func = FUNCTIONS.get(func)
            print(current_func(*data))
        elif func in OPERATORS:                                         
            current_func = OPERATORS.get(func)
            print(current_func(*data))

if __name__ == "__main__":
    main()
