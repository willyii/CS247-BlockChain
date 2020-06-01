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

![Api2](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way1_pic/80chain.png?raw=true)

(3) At the same time, we can see that the container hello has only one initial block (use "Get" button).

> http://0.0.0.0:81/chain

![Api3](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way1_pic/81chain1.png?raw=true)

(4) Register the node hi to node hello. The way to write the address is important. You can use the name of the container with its port (use "Post" button).

> http://0.0.0.0:81/nodes/register

>{
    "nodes": ["http://hi:5000"]
}

![Api4](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way1_pic/register.png?raw=true)

(5) Resolve the conflict. We can see "Our chain was replaced" (use "Get" button).

> http://0.0.0.0:81/nodes/resolve

![Api5](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way1_pic/resolve.png?raw=true)

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

![Api6](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way2_pic/dockerps.png?raw=true)

(2) Get the real address of the container hi by using its CONTAINER ID. Here the address is "172.17.0.2".
```
$ docker inspect --format='{{.NetworkSettings.IPAddress}}' e6165f89f9c0
```

![Api7](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way2_pic/dockerinspect.png?raw=true)

5. Test by using Postman:
(1) Mine 3 blocks in container hi (use "Get" button).

> http://0.0.0.0:80/mine

![Api8](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way2_pic/mine.png?raw=true)

(2) Get the chain of container hi, we can see that there are 4 blocks, including the initial one (use "Get" button). 

> http://0.0.0.0:80/chain

![Api9](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way2_pic/80chain.png?raw=true)

(3) At the same time, we can see that the container hello has only one initial block (use "Get" button).

> http://0.0.0.0:81/chain

![Api10](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way2_pic/81chain1.png?raw=true)

(4) Register the node hi to node hello. Here we use container hi's real address "172.17.0.2". You can use the real address of the container with its port (use "Post" button).

> http://0.0.0.0:81/nodes/register

>{
    "nodes": ["http://172.17.0.2:5000"]
}

![Api11](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way2_pic/register.png?raw=true)

(5) Resolve the conflict. We can see "Our chain was replaced" (use "Get" button).

> http://0.0.0.0:81/nodes/resolve

![Api12](https://github.com/willyii/CS247-BlockChain/blob/dockercommunication/way2_pic/resolve.png?raw=true)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

