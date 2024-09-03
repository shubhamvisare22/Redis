import json
from redis_operations import RedisOperations


class RedisConsumer(RedisOperations):

    def consume_jobs(self):
        while True:
            _, job_data_str = self.redis_client.brpop(self.queue_name)
            job_data = json.loads(job_data_str)
            self.process_job(job_data)

    def process_job(self, job_data):
        if isinstance(job_data, list):
            for i in range(len(job_data)):
                print(f"Record Data {i}: {job_data[i]}")
        else:
            print(f"Record Data : {job_data}")


if __name__ == "__main__":
    consumer = RedisConsumer()
    consumer.consume_jobs()
