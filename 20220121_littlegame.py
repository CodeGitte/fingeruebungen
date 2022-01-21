# recap of classes
# credit to https://www.youtube.com/watch?v=2AK7j8pIh-0

class AngryPerson:                                              #CamelCase
    def __init__(self, name, lifestage, max_health=100):        #=None makes it not required anymore, but optional
        self.name = name
        self.lifestage = lifestage
        self.health = max_health
        self.max_health = max_health

    def __repr__(self):                                     #__init__ and __repry__ are instance method: on each Pokemon instnace
        return f'Angry person: {self.name}, {self.lifestage}, {self.health} health score'
    
    #making an angry person stronger
    def exercise(self):
        if self.health < self.max_health:
            self.health = self.health +5
            print(f'{self.name} has a health score of {self.health}!')
        else:
            print(f'{self.name} is already fit!')
    
    #making it possible for angry people to battle against each other 
    def battle(self, other):
        print(f'Battle: {self.name} is starting to fight against {other.name}!')
        result = self.typewheel(self.lifestage, other.lifestage)
        #scenario: losing
        if result == 'lost':
            self.health -= 10 
            other.health +=10
            print(f'{self.name} fought against {other.name} and {result}! New health score: {self.health}')   
        #scenario: tie
        if result == 'got a tie':
            self.health == self.health 
            print(f'{self.name} fought against {other.name} and {result}! Health score is still: {self.health}')
        #scenario: wining
        if result == 'won':
            self.health += 10 
            other.health -=10
            print(f'{self.name} fought against {other.name} and {result}! New health score: {self.health}')   
        
    #deciding on who wins a
    @staticmethod
    def typewheel(type1, type2):                      
        result = {-1: 'lost', 0: 'got a tie', 1: 'won'}
        # mapping between the types and the result conditions
        game_map = {'youngster': 0, 'boring adult': 1, 'cool adult': 2}
        # implement win-lose matrix
        win_lose_matrix = [
            [0, 1, -1],  #youngster
            [-1, 0, -1], #boring adult
            [1, 1, 0]    #cool adult
        ]
        # declare a winner
        win_lose_result = win_lose_matrix[game_map[type1]][game_map[type2]]
        return result[win_lose_result]
        
    
    
    

if __name__ == '__main__':
    # creating an angry person 1
    Margit = AngryPerson(name='Margit', lifestage='cool adult')
    
    # checking if the if / else statement worked 
    Margit.exercise()
    Margit.health
    print(Margit)
    
    # creating an angry person 2
    Justin = AngryPerson(name='Justin', lifestage='youngster')
    print(Justin)
    
    # battle between angry person 1 and 2
    Margit.battle(Justin)
    
    # checking the score of self.health and other.health after a battle
    print(Margit.health)
    print(Justin.health)
    
    #checking if .exercises works to improve Justin´s health after loosing a battle
    print(Justin.exercise())