from mongoengine import *

class Experience(Document):
    title = StringField()
    from_ = StringField()
    to_ = StringField()
    description = StringField()
    image = FileField()
