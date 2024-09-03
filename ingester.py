import json
import random
from redis_operations import RedisOperations
from logger import Logger


class RedisIngester(RedisOperations):
    logger = Logger("Ingester").log_obj

    def add_job(self):
        job_data = self.generate_record()
        if isinstance(job_data, (dict, list)):
            job_data_str = json.dumps(job_data)
            self.redis_client.lpush(self.queue_name, job_data_str)
            self.logger.info(f"Added job to queue: {len(job_data)}")
            return True
        print("Job data must be a dictionary or valid json list")
        return False

    def generate_record(self):
        return [
            {
                "id": _,
                "name": f"User{_}",
                "email": f"user{_}@example.com",
                "age": random.randint(18, 60),
                "score": random.uniform(0, 100),
            }
            for _ in range(201, 301)
        ]


if __name__ == "__main__":
    ingester = RedisIngester()
    ingester.add_job()
