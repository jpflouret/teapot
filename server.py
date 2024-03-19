from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys
import threading
import time

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
