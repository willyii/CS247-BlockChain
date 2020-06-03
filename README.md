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

## June 2, 2020:
- ***Done***:
  - Random transaction function
  - bonus transaction for miner 
  - Support more than two nodes
  - Banlance feature

- ***TODO***:
  - Singature
  - increase the number of transaction in each block when length of chain up to 100 or higher
  - PPT and report

- ***Usage***:
  - Enter the project folder
  - Using command ""./start.sh"". It will start 5 nodes with ip 0.0.0.0 and port 100, 200, 300, 400, 500
  - You can visit http://0.0.0.0:+prot, like http://0.0.0.0:400/ to see the status of this node. If this node have balance more than 1. It will trigger a transaction to random node with random money
  - If you see the false in "message", that means have problem in get random transaction. In most time, it due to lack of balance 
  - Use command ""ps"" to find your process and use command ""kill"" to kill them. The output of the nodes are in no*.log file
  - Good Luck

