import http.server
import socketserver
handler = http.server.SimpleHTTPRequestHandler
PORT = 8010
socketserver.TCPServer(("",PORT),handler)