# JobScout

A project for AI job search.
Just enter your job preference and it will search for you.

## Features

- SEARCHES JOB OFFERS ON hh.ru;
- SUBMITS AN APPLICATION FOR VACANCIES;

## Installation

1. Clone project with *git clone [repository_name]*
2. Set your environment variables *set in env.example and rename it to .env'
3. Wake it up =) *docker-compose up -d*

## Configuration

|    Option        | Default | Description                  |
|------------------|---------|------------------------------|
|    APP_ENV       | NONE    | Your APP environment level   |
|    LOG_LEVEL     | NONE    | The level of logging         |
|    DB_NAME       | NONE    | Name of database             |
|    DB_USER       | NONE    | Name of database user        |
|    DB_PASSWORD   | NONE    | Password of database user    |
| 	 REDIS_URL     | NONE    | Redis URL                    |

|    AI_Option        | Default | Description                  |
| 	 MISTRAL_API_KEY  | NONE    | API KEY FOR MISTRAL          |
| 	 MISTRAL_MODEL    | NONE    | Mistral model to work with   |
| 	 OLLAMA_BASE_URL  | NONE    | OLLAMA BASE URL              |
| 	 OLLAMA_MODEL     | NONE    | Ollama model to work with    |

## License

[MIT](LICENSE)
