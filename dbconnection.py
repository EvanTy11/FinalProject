import yaml
from neo4j import GraphDatabase


class dbconnection:
    '''Class used for db connection'''

    def __init__(self, configfile):
        '''init constructor for our dbconfig class'''
        self.configfile = configfile
        self.config = self.load_config()

    def load_config(self):
        '''Parses config file and returns python obj'''
        with open(self.configfile, "r") as file:
            return yaml.safe_load(file)

    def get_neo_connection(self):
        '''takes in self.config
        returns a neo4j driver obj'''
        uri = self.config['neo4j']['uri']
        user = self.config['neo4j']['user']
        password = self.config['neo4j']['password']
        driver = GraphDatabase.driver(uri, auth=(user, password))
        return driver