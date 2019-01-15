# docker

## Installation and setup
Installation instructions are available from the docker homepage
https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Test docker version
```bash
docker --version
```
More information available via
```bash
docker info
```

## Help commands
```
docker
docker container --help
```

## Cleanup
Delete all containers
```
docker rm $(docker ps -a -q)
```
Delete all images
```
docker rmi $(docker images -q)
```

## Test docker installation
Testing the installation via running the simple Docker image `hello-world`
```
docker container run hello-world
```

List the `hello-world` image that was downloaded to your machine:
```bash
docker image ls
```
List the hello-world container (spawned by the image) which exits after displaying its message. If it were still running, you would not need the --all option:
```
docker container ls --all
```

## Define container via a docker file
In the past, if you were to start writing a Python app, your first order of business was to install a Python runtime onto your machine. But, that creates a situation where the environment on your machine needs to be perfect for your app to run as expected, and also needs to match your production environment.

With Docker, you can just grab a portable Python runtime as an image, no installation necessary. Then, your build can include the base Python image right alongside your app code, ensuring that your app, its dependencies, and the runtime, all travel together.

These portable images are defined by something called a `Dockerfile`.

### Build the image
```
cd flask-example
docker build --tag=friendlyhello .
```
### Check the built image
```bash
docker image ls
```

### Run the app
Run the app, mapping your machine’s port 4000 to the container’s published port 80 using `-p`:
```bash
docker run -p 4000:80 friendlyhello
```
Web application running on http://localhost:4000.
```bash
curl http://localhost:4000
```

# About services
In a distributed application, different pieces of the app are called “services”. For example, if you imagine a video sharing site, it probably includes a service for storing application data in a database, a service for video transcoding in the background after a user uploads something, a service for the front-end, and so on.

Luckily it’s very easy to define, run, and scale services with the Docker platform -- just write a `docker-compose.yml` file.

We require an additional database (redis) for our application.
This is defined in the `docker-compose.yml`. 
The containers can than be started via
```
docker-compose up
```

