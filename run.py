import http.server
import socketserver
import json
import sys

PORT = 9090

if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        print(f"Invalid port specified: {sys.argv[1]}.")

class AdvanceHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response_data = {
                "status": "online",
                "message": "Welcome to the imageExplainer"
            }
            
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        
        else:
            return super().do_GET()
        
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), AdvanceHttpRequestHandler) as httpd:
        print(f"Server is running at port: {PORT}")
        print(f"Go to http:127.0.0.1:{PORT} in your browser.")

        httpd.serve_forever()