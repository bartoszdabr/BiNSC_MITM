FROM python:3.12-slim

COPY . .
RUN apt-get update && apt-get install -y iptables tcpdump dsniff iproute2 tmux dnsutils
RUN pip3 install -r requirements.txt

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"