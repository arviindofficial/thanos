FROM thanosuser/THANOSPRO:latest

RUN git clone https://github.com/rishabh87yhtts/THANOS-PRO.git /root/THANOSPRO

WORKDIR /root/THANOSPRO

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/THANOSPRO/bin:$PATH"

CMD ["python3", "-m", "THANOSPRO"]
