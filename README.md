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

- ***USAGE***:
  - In project fold run
  
  '''
    python3 testFlask.py --port 101 -t 0
    python3 testFlask.py --port 100 -t 1
  '''
  
  to initialize two web application, and second one will send message to first one every 10s. You will see the result in terminal 
  
  - In project fold run
  
  '''
    python3 app.py --port 100
  '''
  
  to initialize a web application with node. Then goto ***http://0.0.0.0:100/*** in browse. It will trigger a new transaction and broadcast new block and mine and add to self. It will return the node information in browser. 
