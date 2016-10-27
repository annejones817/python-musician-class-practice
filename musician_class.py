from random import randint

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
            

class Bassist(Musician): 
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Clang", "Crash"])
        
    def count(self, number): 
        for num in range(1,number): 
            print(num)
        
    def combust(self): 
        print("I have spontaneously combusted!")
        
class Band: 
    def __init__(self, name): 
        self.name = name
        self.bandMembers=[]
	
    def hire(self, musicianHired):
        self.bandMembers.append(musicianHired)
	
    def fire(self, musicianFired):
        self.bandMembers.remove(musicianFired)
		
    def play(self, drummer):
        drummer.count(5), 
        for member in self.bandMembers: 
            member.solo(randint(5,10))

if __name__ == '__main__':
    myBand = Band("myBand")
    
    musician1=Guitarist()
    musician2=Drummer()
    musician3=Bassist()
    musicians=[musician1, musician2, musician3]
    
    for musician in musicians: 
    	myBand.hire(musician)
    
    myBand.play(musician2)