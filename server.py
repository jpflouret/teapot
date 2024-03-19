from http.server import BaseHTTPRequestHandler, HTTPServer

bindAddress = ""
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.server_version = 'Teapot/1.0.0'
    self.sys_version = 'Coffee/1.0.0'
    self.send_response(418)
    self.send_header("Content-type", "text/plain; charset=utf-8")
    self.end_headers()
    self.wfile.write(bytes("I'm a teapot.\n", "utf-8"))

if __name__ == "__main__":
  webServer = HTTPServer((bindAddress, serverPort), MyServer)
  print("Server listening on %s:%s" % (bindAddress, serverPort))

  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass

  webServer.server_close()
  print("Server stopped.")
