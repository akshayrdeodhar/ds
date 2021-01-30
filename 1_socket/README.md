## Protocol 

Client sends requests ONLY: Request is a filename whose length is less than 1024 

Server's response:
First 7 bytes: A string- "SUCCESS" or "FAILURE"
Remaining message (server closes connection after serving single request): The
contents of the file, encoded in UTF-8

Communication happens using TCP

## Testing

	python3 server.py # run server

	python3 client.py localhost preamble.txt
