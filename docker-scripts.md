### Build docker container with tag

`docker build -t gen-ai-experiments .`

### Run docker container with live code mounting (recommended for development)

`docker run -it -v "$(pwd)/src:/src" gen-ai-experiments`

### Development workflow example:

#### One terminal: Start container with live mounting

`docker run -it -v "$(pwd)/src:/src" gen-ai-experiments`

#### Another terminal: Edit code in VS Code

`code src/projects/2-chains/my_experiment.py`

#### Back in container: Run immediately

`python projects/2-chains/my_experiment.py`

### moving to docker-compose

`docker-compose build`

### running with docker-compose network

`docker-compose exec gen-ai-experiments bash`
