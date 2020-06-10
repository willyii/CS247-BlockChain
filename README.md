# CS247-BlockChain

- ***Usage***:
  ### Start with 5 nodes
  - Enter the project folder
  - Using command ""./start.sh"". It will start 5 nodes with ip 0.0.0.0 and port 100, 200, 300, 400, 500
  - You can visit http://0.0.0.0:+prot, like http://0.0.0.0:400/ to see the status of this node. If this node have balance more than 1. It will trigger a transaction to random node with random money
  - If you see the false in "message", that means have problem in get random transaction. In most time, it due to lack of balance 
  - Use command ""ps"" to find your process and use command ""kill"" to kill them. The output of the nodes are in no*.log file

  ### Start with single node
  - Enter the project folder
  - Using command ""python app.py -p portnum"". It will start single node, you can see the address of that node in your terminal, default port is 5000
  - You can visiti that address and you will see the information of that node.
