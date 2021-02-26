## Protocol 

Client sends requests ONLY: Request is a filename whose length is less than 1024 

Server's response:
First 7 bytes: A string- "SUCCESS" or "FAILURE"
Remaining message (server closes connection after serving single request): The
contents of the file, encoded in UTF-8

Communication happens using TCP

## Testing

	minikube start

	kubectl create -f ds-2021-socket-deployment.yaml # Create a deployment which runs two servers at the same time

	kubectl create -f ds-2021-socket-service.yaml # Create a random load balanced service which exposes these two servers to the network

	kubectl get pods -o yaml # Run command, inspect the hostIP of the pod- that is the IP address on which the servers are serving (in a load-balanced way)

	python3 client.py <host ip> preamble.txt # fetch preamble from HA + FT service and enjoy reading it from stdout

## Note

- On a single node cluster, the Deployment does not provide *much* fault
  tolerance (if the node goes down, I can do nothing). On a multi node
  Kubernetes cluster, however, the moment a node (and the pods running on it go
  down), replicas are created on new nodes. Because there are multiple copies of
  pods, one pod going down leaves the application available

- Requests are Load-Balanced between multiple pods in the deployment. If you
  change the setting of "Type" in the Service specification to "Load-Balanced"
  and run this service on a Cloud Provider, there will be true load-balancing
  happening between pods running on multiple nodes.

