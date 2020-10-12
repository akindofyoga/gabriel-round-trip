FROM ubuntu:18.04

RUN apt-get update && apt-get install -y libgl1-mesa-glx python3 python3-pip


COPY requirements.txt .

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 9099

ENTRYPOINT ["./main.py"]
