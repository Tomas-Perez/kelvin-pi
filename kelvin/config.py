from logging import INFO

# sensors
GPSD_PORT = '2947'
DHT_PIN = 4
LDR_PIN = 17

# db
MONGO_PORT = 27017
DB = 'kelvin'
COLLECTION = 'points'

# Amazon SQS url
QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/011354114873/kelvin'

# timings
GATHER_TIMEOUT = 2
SEND_TIMEOUT = 10

# logging
LOG_FORMAT = '%(asctime)s : %(levelname)s : %(message)s'
GATHER_FILE = 'datagather.log'
SEND_FILE = 'datasend.log'
LOG_LEVEL = INFO
