FROM tensorflow/tensorflow:1.15.5
RUN apt-get update && apt-get install -y git python3-pip
RUN pip3 install keras==2.3.1 keras_metrics
#&& pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl 
RUN pip install pandas sklearn matplotlib pathlib networkx
WORKDIR /
RUN git clone https://github.com/ibabedal/iSOM_GSN.git 
RUN chmod +x /iSOM_GSN/linux_version_v1/build_script.sh

ENTRYPOINT [ "/iSOM_GSN/linux_version_v1/build_script.sh" ]
