import socketserver
import socket
import threading
import pickle
import io
import argparse
import select
import queue

class GameCustomServer(socketserver.ThreadingTCPServer):
    def __init__(self, server_address, request_handler_class):
        super().__init__(server_address, request_handler_class, True)
        self.clients = set()

    def add_client(self, client):
        self.clients.add(client)
        print("added client")

    def broadcast(self, source, data):
        for client in tuple(self.clients):
            if client is not source:
                client.request.send(data)
                print("Sent client data")

    def remove_client(self, client):
        self.clients.remove(client)
        print("Removed client")
