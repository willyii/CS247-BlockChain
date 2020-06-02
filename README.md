# CS247-BlockChain

## meeting 1:
- understand concepts of Blockchain.  
- set up Docker locally.  
- implement basic chain locally.  
- connect nodes between team members.  
  
## Meeting 2, May 30 2020:
- ***Done***:
  - Designed and implemented the structure of Node, Block, BlockChain and Transaction
- ***Plan***: 
  - BlockChain: ZhuoCheng
  - mine function in node: Zeyu
  - Others: Xinlong
- ***TODO***:
  - Test.py for each function
  - Web module
  - Communication between nodes

## May 31, 2020:
- ***Done***:
  - Finished code for block chain part. Pass the local test, check in testnode.py.
- ***TODO***:
  - Communication between nodes
  - Flask Application

## June 1, 2020:
- ***Done***:
  - Single node mode, can run single node
  - Communication between two node already coded, test communication tomorrow. Note: ip for these two node are hard coded
  - Finished basic structure of web application in app.py.

- ***TODO***:
  - Move mine function in thread level
  - add new function in app.py to generate random transaction

## 2nd update, June 1, 2020:
- ***Done***:
  - Move mine function into thread
  - Finishe two node communication, done a simple pass in app.py

- ***TODO***:
  - new function in app.py to generate random transaction 
  - maybe three or more nodes?
  - bounce coin for miner who find it out 

- ***Usage***
  - Enter project folder 
  - Use command "python3 app.py --port 5000" to start one node. this node will have 50 coins as initial
  - Use command "python3 app.py --port 100" to start another node in other terminal.
  - Visit http://0.0.0.0:5000/ to trigger one transaction. In this transaction, 5000 will send 50 coins to 100. Then every guys starts to mine. You will see which one will mined out the block in terminal
