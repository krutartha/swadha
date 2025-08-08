#!/usr/bin/env python3
"""
Enhanced development server with WebSocket live reload
"""

import http.server
import socketserver
import os
import time
import threading
import webbrowser
import json
import base64
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# WebSocket implementation for live reload
class WebSocketHandler:
    def __init__(self, request):
        self.request = request
        self.connected = False
        
    def handle_websocket(self):
        # Simple WebSocket handshake
        headers = self.request.recv(1024).decode()
        if 'Upgrade: websocket' in headers:
            # Send WebSocket upgrade response
            response = (
                "HTTP/1.1 101 Switching Protocols\r\n"
                "Upgrade: websocket\r\n"
                "Connection: Upgrade\r\n"
                "Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r\n\r\n"
            )
            self.request.send(response.encode())
            self.connected = True
            return True
        return False

class LiveReloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/livereload.js':
            self.send_livereload_script()
            return
        return super().do_GET()

    def send_livereload_script(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/javascript')
        self.end_headers()
        
        script = """
        (function() {
            var ws = new WebSocket('ws://localhost:8001');
            ws.onmessage = function(event) {
                if (event.data === 'reload') {
                    window.location.reload();
                }
            };
            ws.onclose = function() {
                console.log('Live reload disconnected');
            };
        })();
        """
        self.wfile.write(script.encode())

def inject_livereload_script(html_content):
    """Inject live reload script into HTML"""
    script_tag = '<script src="/livereload.js"></script>'
    if '</head>' in html_content:
        return html_content.replace('</head>', f'    {script_tag}\n</head>')
    return html_content

class LiveReloadServer:
    def __init__(self, port=8000, ws_port=8001):
        self.port = port
        self.ws_port = ws_port
        self.clients = []
        self.file_watcher_running = False
        
    def start_websocket_server(self):
        """Start WebSocket server for live reload"""
        import socket
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('localhost', self.ws_port))
        server.listen(5)
        
        print(f"🔌 WebSocket server started on port {self.ws_port}")
        
        while self.file_watcher_running:
            try:
                client, addr = server.accept()
                print(f"🔌 WebSocket client connected: {addr}")
                self.clients.append(client)
            except:
                break
                
        server.close()

    def notify_clients(self, message):
        """Notify all connected WebSocket clients"""
        disconnected = []
        for client in self.clients:
            try:
                client.send(message.encode())
            except:
                disconnected.append(client)
        
        # Remove disconnected clients
        for client in disconnected:
            self.clients.remove(client)

    def watch_files(self):
        """Watch for file changes and notify clients"""
        last_modified = {}
        
        while self.file_watcher_running:
            for file_path in Path('.').rglob('*.html'):
                if file_path.is_file():
                    current_mtime = file_path.stat().st_mtime
                    if str(file_path) not in last_modified or last_modified[str(file_path)] != current_mtime:
                        last_modified[str(file_path)] = current_mtime
                        print(f"🔄 File changed: {file_path}")
                        self.notify_clients('reload')
                        break
            
            for file_path in Path('.').rglob('*.css'):
                if file_path.is_file():
                    current_mtime = file_path.stat().st_mtime
                    if str(file_path) not in last_modified or last_modified[str(file_path)] != current_mtime:
                        last_modified[str(file_path)] = current_mtime
                        print(f"🔄 File changed: {file_path}")
                        self.notify_clients('reload')
                        break
            
            time.sleep(1)

    def start(self):
        """Start the development server"""
        self.file_watcher_running = True
        
        # Start WebSocket server in a separate thread
        ws_thread = threading.Thread(target=self.start_websocket_server, daemon=True)
        ws_thread.start()
        
        # Start file watcher in a separate thread
        watcher_thread = threading.Thread(target=self.watch_files, daemon=True)
        watcher_thread.start()
        
        # Start HTTP server
        with socketserver.TCPServer(("", self.port), LiveReloadHandler) as httpd:
            print(f"🚀 Live development server starting on http://localhost:{self.port}")
            print(f"📁 Serving files from: {os.getcwd()}")
            print(f"🔄 Live reload enabled - changes will automatically refresh the browser")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Open browser
            webbrowser.open(f'http://localhost:{self.port}')
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n⏹️  Server stopped by user")
                self.file_watcher_running = False
                httpd.shutdown()

def main():
    server = LiveReloadServer()
    server.start()

if __name__ == "__main__":
    main()
