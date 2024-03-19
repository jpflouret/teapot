from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys
import threading
import time

bindAddress = ""
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
    x_forwarded_for = self.headers.get('X-Forwarded-For')
    if x_forwarded_for:
      self.client_address = (x_forwarded_for.split(',')[0], self.client_address[1])
    self.server_version = 'Teapot/1.0.0'
    self.sys_version = 'Coffee/1.0.0'
    if self.path == '/healthz':
      self.healthz()
    else:
        self.teapot()

  def teapot(self):
    self.send_response(418)
    self.send_header("Content-type", "text/plain; charset=utf-8")
    self.end_headers()
    self.wfile.write(bytes("I'm a teapot.\n", "utf-8"))

  def healthz(self):
    self.send_response(200)
    self.send_header("Content-type", "text/plain; charset=utf-8")
    self.end_headers()
    self.wfile.write(bytes("OK\n", "utf-8"))

  def log_request(self, code='-', size='-'):
    if self.path == '/healthz':
      return
    return super().log_request(code, size)

if __name__ == "__main__":
  webServer = HTTPServer((bindAddress, serverPort), MyServer)

  def stop(signal_number, frame):
    print('Server shutting down.')
    webServer.shutdown()
    sys.exit(0)

  signal.signal(signal.SIGTERM, stop)
  signal.signal(signal.SIGINT, stop)

  thread = threading.Thread(target=webServer.serve_forever)
  thread.daemon = True
  thread.start()

  print("Server listening on %s:%s" % (bindAddress, serverPort))

  while True:
      time.sleep(1)
