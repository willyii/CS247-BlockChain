# CS247-BlockChain

## meeting 1:
understand concepts of Blockchain.  
set up Docker locally.  
implement basic chain locally.  
connect nodes between team members.  

## Guide for running blockchain API
### Docker Command
1. go to project folder
   > cd Project folder
2. build docker container
   >  docker build -t [folder name] .
3. running container
   >  docker run --rm -p 5000:80 [folder name]
4. delete all container & images
   > $ docker system prune

### Postman testing API
1. running URL:
   > localhost:5000
2. all required input data are json format
3.  current tested API
    1. add new transaction \
     > localhost:5000/newtrans 
    2. add new nodes \
      >localhost:5000/addnodes
    3. get all current nodes \
      >localhost:5000/getallnodes
    4. initial block with a genesis block \
     > localhost:5000/
    


