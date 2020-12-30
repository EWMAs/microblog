import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

"""Pretty simple, right? 
The configuration settings are defined as class variables inside the Config class. 
As the application needs more configuration items, they can be added to this class, and later if I find that I need to have more than one configuration set, I can create subclasses of it."""

"Source: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms"