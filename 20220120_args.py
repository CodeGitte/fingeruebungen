#playing around with *args (parameter that allows for as many arguments as wanted)
def nice_people(person_one, *args):
    print(person_one, 'says hello')
    for person_other in args:
        print(person_other, 'also says hi')
        
nice_people('Margit', 'Corinna', 'Theresa')


#playing around with **kwargs (accepts any number of keyword arguments)
def score(game, **kwargs):
    print(game, 'scores:')
    for key, value in kwargs.items():
        print(key, value)
        
score('Rommee', Margit = 5, Edith = 85, Fritz = 23)