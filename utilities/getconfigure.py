from configparser import ConfigParser

def getconfigure(category, key):
    config = ConfigParser()
    config.read("C:\\Users\\91789\\PycharmProjects\\pytestBy_naveen\\Reports\\config.ini")
    return config.get(category,key)