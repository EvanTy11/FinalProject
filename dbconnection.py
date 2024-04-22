import yaml
import neo4j


class dbconnection:
    '''Class used for db connection'''

    def __init__(self, configfile):
        '''init constructor for our dbconfig class'''
        self.configfile = configfile

    def load_config():
        '''Parses config file and returns python obj'''
        with open("config.yaml", "r") as file:
            return yaml.safe_load(file)
    # stores obj for later use
    config = load_config()

    def get_neo_connection(self):
        '''takes in self.config
        returns a redis obj'''
        uri = "bolt://localhost:7687"
        driver = neo4j.GraphDatabase.driver(uri,auth=("neo4j","password"))
        return driver
