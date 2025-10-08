#!/usr/bin/python3
"""Module qui lance un serveur HTTP simple
    avec plusieurs endpoints : /, /data, /status"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyServer(BaseHTTPRequestHandler):
    """Classe qui gère les requêtes HTTP du serveur (GET uniquement)"""

    def do_GET(self):
        """Gère les requêtes HTTP GET
            selon le chemin demandé (/ , /data , /status)"""

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyServer)
    print("Serveur lancé sur le port 8000...")
    httpd.serve_forever()
