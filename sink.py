import http.server
import socketserver

PORT=8081
ADDRESS="0.0.0.0"

class handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])

        post_data = self.rfile.read(content_length)

        print(f"Received POST data: {post_data.decode('utf-8')}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_message = b"POST request received successfully!\n"
        self.wfile.write(response_message)

    def do_GET(self):
        print(f"Received GET data: {self.connection}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_message = b"GET request received successfully!\n"
        self.wfile.write(response_message)



with socketserver.TCPServer((ADDRESS, PORT), handler) as httpd:
    print(f"Serving at {ADDRESS} on port {PORT}")
    httpd.serve_forever()