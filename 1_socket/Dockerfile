FROM python
WORKDIR ./
COPY server.py preamble.txt big.txt ./
ENV SERVICE_PORT=8042
CMD ["python", "server.py"]
