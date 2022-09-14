import json
from random import randint

IMG_URL = {
    'sleep': 'https://images.pexels.com/photos/969147/pexels-photo-969147.jpeg?cs=srgb&dl=pexels-grace-robertson-969147.jpg&fm=jpg',
    'not_sleep': 'https://idsb.tmgrup.com.tr/ly/uploads/images/2021/09/08/thumbs/800x531/142774.jpg'
}


class Cat():
    def __init__(self, name :str, age: int=3, mood: int=75, satiety: int=50, state_sleep: bool=False) -> None:
        self.name = name
        self. age = age
        self.mood = mood
        self.satiety = satiety
        self.max_satiety = 100
        self.state_sleep = state_sleep
        if self.state_sleep == False:
            self.img_url = IMG_URL['not_sleep']
        else:
            self.img_url = IMG_URL['sleep']


    def save(self):
        to_json = self.__dict__
        with open('cat_app/services/cat.json', 'w') as f:
            json.dump(to_json, f)

    
    def feed(self):
        if self.state_sleep == False:
            self.satiety += 15
            
            if self.satiety > self.max_satiety:
                self.mood -= 30
                if self.mood < 0:
                    self.mood = 0
            else:
                self.mood += 5


    def play(self):
        if self.state_sleep == True:
            self.state_sleep = False
            self.img_url = IMG_URL['not_sleep']

            self.mood -= 5
            if self.mood < 0:
                self.mood = 0
        else:
            if randint(1, 100) > 33:
                self.mood += 15
                self.satiety -= 10
                if self.satiety < 0:
                    self.satiety = 0
            else:
                self.mood = 0


    def sleep(self):
        self.state_sleep = True
        self.img_url = IMG_URL['sleep']
   