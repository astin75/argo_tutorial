FROM python:3.8

RUN apt-get update
RUN apt-get upgrade -y
 
RUN apt-get install git -y
RUN cd /home/
RUN git clone https://github.com/astin75/argo_tutorial.git /home/argo_tutorial/
workdir /home/argo_tutorial/python_task
RUN pip3 install -r requirements.txt
# docker run -it argo_tutorial:0.0.1 python  time_count.py --sec 5