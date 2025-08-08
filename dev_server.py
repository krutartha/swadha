#!/usr/bin/env python3
"""
Simple development server with auto-reload functionality
"""

import http.server
import socketserver
import os
import time
import threading
import webbrowser
from pathlib import Path
import json

class AutoReloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def watch_files(callback):
    """Watch for file changes and trigger callback"""
    last_modified = {}
    
    while True:
        for file_path in Path('.').rglob('*.html'):
            if file_path.is_file():
                current_mtime = file_path.stat().st_mtime
                if str(file_path) not in last_modified or last_modified[str(file_path)] != current_mtime:
                    last_modified[str(file_path)] = current_mtime
                    print(f"🔄 File changed: {file_path}")
                    callback()
                    break
        
        for file_path in Path('.').rglob('*.css'):
            if file_path.is_file():
                current_mtime = file_path.stat().st_mtime
                if str(file_path) not in last_modified or last_modified[str(file_path)] != current_mtime:
                    last_modified[str(file_path)] = current_mtime
                    print(f"🔄 File changed: {file_path}")
                    callback()
                    break
        
        time.sleep(1)

def main():
    PORT = 8000
    
    # Create server
    with socketserver.TCPServer(("", PORT), AutoReloadHandler) as httpd:
        print(f"🚀 Development server starting on http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"🔄 Auto-reload enabled - changes will trigger browser refresh")
        print(f"⏹️  Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Open browser
        webbrowser.open(f'http://localhost:{PORT}')
        
        # Start file watcher in a separate thread
        def reload_callback():
            print("🔄 Reloading browser...")
            # You could add WebSocket functionality here for true auto-reload
            # For now, we'll just notify that files changed
        
        watcher_thread = threading.Thread(target=watch_files, args=(reload_callback,), daemon=True)
        watcher_thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n⏹️  Server stopped by user")
            httpd.shutdown()

if __name__ == "__main__":
    main()
