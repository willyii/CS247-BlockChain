nohup python3 app.py --port 100 > no1.log &
sleep 5s
nohup python3 app.py --port 200 > no2.log &
sleep 5s
nohup python3 app.py --port 300 > no3.log &
sleep 5s
nohup python3 app.py --port 400 > no4.log &
sleep 5s
nohup python3 app.py --port 500 > no5.log &
