# CS247-BlockChain

This repository is course project for CS247 distributed computation at UCR. Our idea is to build a protoype of Bitcoin. 

## Requirements
- Python >= 3.5
- Flask

## Usage:
  Our project used Flask as framework. All nodes runs on same host with differen ports. You can use following cammand to run this project:
  
  ```bash
  git clone https://github.com/willyii/CS247-BlockChain
  cd CS247-BlockChain
  ./start.sh
  ```
  
  As default, it will start 5 nodes. All of them runs on local host with ports 100, 200, 300, 400 and 500.
  
  You can visit the url links with format **http://0.0.0.0:+prot**, eg http://0.0.0.0:400/, to check the status of corresponding node. If visiting node has 
  balance >=1. This visiting operation will trigger a random transaction.
  
  If you see the false in "message", that means have problem in get random transaction. In most time, it due to lack of balance
  
  Use command ""ps"" to find your process and use command ""kill"" to kill them. The output of the nodes are in no*.log file

  ### Start with different number of nodes
  - Enter the project folder
  - Using command **python app.py -p portnum**. It will start single node, you can see the address of that node in your terminal, default port is 5000
  - You can visiti that address and you will see the information of that node.
