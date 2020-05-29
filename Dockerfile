# this is an official Python runtime, used as the parent image
FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 80

ENTRYPOINT ["python"]

# execute the Flask app
CMD ["blockchain.py"]