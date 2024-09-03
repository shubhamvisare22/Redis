import os

class Config:
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    REDIS_DB = int(os.getenv('REDIS_DB', 0))
    REDIS_QUEUE_NAME = os.getenv('REDIS_QUEUE_NAME', 'test_queue')
    LOG_HANDLER = os.getenv("LOG_HANDLER", False)
    print(LOG_HANDLER)

config = Config()