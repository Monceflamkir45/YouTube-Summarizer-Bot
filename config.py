import os

class Telegram:
    API_ID = int(os.environ.get('22784345'))
    API_HASH = os.environ.get('5fe063ba8f41c81043b9abb9a6bbab17')
    BOT_TOKEN = os.environ.get('7515355666:AAHnKhhpkk5f8NK6aLqhK3DoO2bpQfqPPJg')
    AUTH_USER_ID = int(os.environ.get('6097677058'))
    
class Ai:
    GROQ_API_KEY = os.environ.get('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')

class Database:
    REDIS_URI = os.environ.get('redis-13156.c321.us-east-1-2.ec2.redns.redis-cloud.com:13156')
    REDIS_PASSWORD = os.environ.get('bE4PBM0CPallkb7VlWMrH0qudolSEpmi')
