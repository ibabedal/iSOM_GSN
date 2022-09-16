FROM tensorflow/tensorflow:1.15.5
RUN apt-get update && apt-get install -y git python3-pip
RUN pip3 install keras==2.3.1 keras_metrics
#&& pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl 
RUN pip install pandas sklearn matplotlib pathlib networkx
WORKDIR /
COPY ./M* /
COPY ./en* /
RUN chmod +x /entry_script.sh

ENTRYPOINT [ "/entry_script.sh" ]
