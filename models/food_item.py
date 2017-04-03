from mongoengine import *

class FoodItem(Document):
    scr = StringField()
    title = StringField()
    description = StringField()

