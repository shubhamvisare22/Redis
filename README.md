
# Redis Job Queue with Producer-Consumer Pattern

This project demonstrates a Redis-based job queue implementation using Python. It includes a producer (ingester) that adds jobs to a Redis queue and a consumer that processes the jobs. The project uses logging for tracking activities and operations.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Modules Description](#modules-description)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project implements a simple producer-consumer pattern using Redis as a message broker. It allows you to add jobs to a queue (`RedisIngester`) and consume those jobs (`RedisConsumer`). The project is designed with scalability in mind, making it easy to add new job processing logic or extend functionality.

## Features

- **Producer (`ingester.py`)**: Adds jobs to a Redis queue.
- **Consumer (`consumer.py`)**: Consumes jobs from the Redis queue and processes them.
- **Redis Operations (`redis_operations.py`)**: Handles Redis connections and basic queue operations.
- **Logging (`logger.py`)**: Logs actions with optional file-based logging.

## Project Structure

```plaintext
.
├── config.py                # Configuration settings
├── consumer.py              # Consumer to process jobs from Redis queue
├── ingester.py              # Producer to add jobs to Redis queue
├── logger.py                # Logging utility
├── redis_operations.py      # Redis operations for queue management
├── README.md                # Project documentation
└── log_files/               # Directory for log files
```


## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/redis-job-queue.git
   cd redis-job-queue
   ```
2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Redis:** Make sure Redis is installed and running on your local machine or a server.
4. **Set environment variables (optional):** See [Environment Variables](#environment-variables) for details.

## Environment Variables

The application can be configured via environment variables. Below are the optional environment variables you can set:

- `REDIS_HOST`: Redis server hostname (default: `localhost`)
- `REDIS_PORT`: Redis server port (default: `6379`)
- `REDIS_DB`: Redis database number (default: `0`)
- `REDIS_QUEUE_NAME`: Name of the Redis queue (default: `test_queue`)
- `LOG_HANDLER`: If `True`, logs to file; otherwise, logs to console (default: `False`)

## Usage

### Running the Producer (Ingester)

The ingester adds jobs to the Redis queue. Run the following command to start adding jobs:

```bash
python ingester.py
```

### Running the Consumer

The consumer processes jobs from the Redis queue. Run the following command to start consuming jobs:

```bash
python consumer.py
```

## Modules Description

- **`config.py`**: Configures application settings using environment variables.
- **`redis_operations.py`**: Handles all Redis-related operations such as creating, updating, deleting, and checking queues.
- **`ingester.py`**: A producer script that generates job records and pushes them to the Redis queue.
- **`consumer.py`**: A consumer script that reads job records from the Redis queue and processes them.
- **`logger.py`**: A utility for logging with support for file-based logging using `TimedRotatingFileHandler`.

## Logging

Logging is set up using the `Logger` class in `logger.py`. By default, logs are printed to the console, but can be configured to save logs in files based on a job name using environment variables.

Logs are stored in `log_files/<job_name>.log`, rotating daily and keeping backups for 90 days.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
