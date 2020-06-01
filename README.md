# Communication between docker containers
    
## Docker way 1

Follow the instructions below to create a local Docker container:

1. Clone this repository.
2. Build the docker container.

```
$ docker build -t blockchain .
```

3. Run one container and give a name to it.

```
$ docker run --rm -p 80:5000 --name hi blockchain
```

4. Run another container and give a name to it and build a link to the previous one.

```
$ docker run --rm -p 81:5000 --name hello --link hi blockchain
```

5. Test by using Postman:
(1) Mine 3 blocks in container hi (use "Get" button).

> http://0.0.0.0:80/mine

![Api1](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way1_pic/mine.png?raw=true)

(2) Get the chain of container hi, we can see that there are 4 blocks, including the initial one (use "Get" button).

> http://0.0.0.0:80/chain

(3) At the same time, we can see that the container hello has only one initial block (use "Get" button).

> http://0.0.0.0:81/chain

(4) Register the node hi to node hello. The way to write the address is important. You can use the name of the container with its port (use "Post" button).

> http://0.0.0.0:81/nodes/register

>{
    "nodes": ["http://hi:5000"]
}

(5) Resolve the conflict. We can see "Our chain was replaced" (use "Get" button).

> http://0.0.0.0:81/nodes/resolve

## Docker way 2

Follow the instructions below to create a local Docker container:

1. Clone this repository.
2. Build the docker container.

```
$ docker build -t blockchain .
```

3. Run one container and give a name to it.

```
$ docker run --rm -p 80:5000 --name hi blockchain
```

4. Run another container and give a name to it and build a link to the previous one.

```
$ docker run --rm -p 81:5000 --name hello blockchain
```

5. Get the fisrt container's real address.

(1) Get the CONTAINER ID of the container hi. 
```
$ docker ps
```

(2) Get the real address of the container hi by using its CONTAINER ID. Here the address is "172.17.0.2".
```
$ docker inspect --format='{{.NetworkSettings.IPAddress}}' e6165f89f9c0
```

5. Test by using Postman:
(1) Mine 3 blocks in container hi (use "Get" button).

> http://0.0.0.0:80/mine

(2) Get the chain of container hi, we can see that there are 4 blocks, including the initial one (use "Get" button). 

> http://0.0.0.0:80/chain

(3) At the same time, we can see that the container hello has only one initial block (use "Get" button).

> http://0.0.0.0:81/chain

(4) Register the node hi to node hello. Here we use container hi's real address "172.17.0.2". You can use the real address of the container with its port (use "Post" button).

> http://0.0.0.0:81/nodes/register

>{
    "nodes": ["http://172.17.0.2:5000"]
}

(5) Resolve the conflict. We can see "Our chain was replaced" (use "Get" button).

> http://0.0.0.0:81/nodes/resolve

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

