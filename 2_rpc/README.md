---
author: 111703013 Akshay Rajesh Deodhar
title: Distributed Systems Assignment 2: File Transfer over RPC
date: 24 February 2021
---

# To Test:

## On Both Client and Server Machines
	# Make the client and server programs
	make

## On Server Machine
	# Start the service needed for portmapper
	sudo systemctl start rpcbind

	# Start serving files
	./fileread_server

## On Client Machine
- Alternately, start a new terminal, and use "localhost" instead of the IP
  address of the machine

  ./fileread_client <ip address of server> preamble.txt

  OR

  ./fileread_client localhost preamble.txt
