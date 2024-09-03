import redis
from config import config


class RedisOperations:
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=config.REDIS_DB
        )
        self.queue_name = config.REDIS_QUEUE_NAME

    def is_queue_exists(self, queue_name=None):
        queue_name = queue_name or self.queue_name
        return self.redis_client.exists(queue_name) > 0

    def create_queue(self, queue_name=None, initial_data=None):
        queue_name = queue_name or self.queue_name
        if initial_data:
            if not isinstance(initial_data, (list, str)):
                raise ValueError("Initial data must be a list or a string")
            if isinstance(initial_data, list):
                for item in initial_data:
                    self.redis_client.lpush(queue_name, item)
            else:
                self.redis_client.lpush(queue_name, initial_data)

        print(f"Queue '{queue_name}' created with initial data.")

    def update_queue(self, new_queue_name):
        if self.is_queue_exists():
            self.redis_client.rename(self.queue_name, new_queue_name)
            self.queue_name = new_queue_name
            print(f"Queue renamed to '{new_queue_name}'")
        else:
            print(f"Queue '{self.queue_name}' does not exist.")

    def delete_queue(self, queue_name=None):
        queue_name = queue_name or self.queue_name
        if self.is_queue_exists(queue_name):
            self.redis_client.delete(queue_name)
            print(f"Queue '{queue_name}' deleted.")
        else:
            print(f"Queue '{queue_name}' does not exist.")


if __name__ == "__main__":
    redis_ops = RedisOperations()

    # Check if queue exists
    if redis_ops.is_queue_exists():
        print(f"Queue '{redis_ops.queue_name}' exists.")
    else:
        print(
            f"Queue '{redis_ops.queue_name}' does not exist. Creating queue.")
        redis_ops.create_queue(initial_data="Initial job data")

    # Update queue name
    new_queue_name = "updated_queue"
    redis_ops.update_queue(new_queue_name)

    # Delete queue
    redis_ops.delete_queue(new_queue_name)
