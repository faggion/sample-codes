import ConfigParser, os, logging

config = ConfigParser.ConfigParser()
#config.read(os.path.join(os.path.dirname(__file__), 'eventregist.password'))
config.read('/etc/eventregist/api.password')
