# van http.server importeren we BaseHTTPRequestHandler en HTTPServer, de libraries die we nodig hebben voor onze http server
# https://docs.python.org/3/library/http.server.html
from http.server import BaseHTTPRequestHandler, HTTPServer;
# als port nemen we best default port 80 of 8080
PORT = 80

# we maken de MyServer class en gebruiken de geïmporteerde library BaseHTTPRequestHandler
class MyServer(BaseHTTPRequestHandler):
  # we maken een nieuwe functie die reageert op alle GET requests (self)
  def do_GET(self):
    # we sorteren hier de gekregen GET requests
    # als het path van de gekregen GET request eindigt op / of /home
    if self.path.endswith("/") or self.path.endswith("/home"):
      # dan sturen we een OK response terug (code 200)
      self.send_response(200)
      # dan zetten we de header van Content-Type naar text/html, zodat de response die de requester (client) krijgt als text/html beschouwd wordt
      self.send_header("Content-type", "text/html")
      # we sluiten/eindigen de headers
      self.end_headers()

      # we openen de index.html file uit dezelfde directory om hem te lezen
      with open("index.html", "rb") as file: 
        # dan sturen we de gelezen data uit deze file als response (met utf-8 encoding) terug naar de requester
        self.wfile.write(file.read())

    # als het path van de gekregen GET request niet eindigt op / of /home
    else:
      # dan sturen we een OK response terug (code 200)
      self.send_response(200)
      # dan zetten we de header van Content-Type naar text/html, zodat de response die de requester (client) krijgt als text/html beschouwd wordt
      self.send_header("Content-type", "text/html")
      # we sluiten/eindigen de headers
      self.end_headers()
      # en dan sturen we "hier is niet..." als response (met utf-8 encoding) terug naar de requester
      self.wfile.write(bytes("hier is niets...", "utf-8"))

# als de main.py file wordt gerund
if __name__ == "__main__":
  # definiëren we onze webServer via de geïmporteerde HTTPServer library met de gegeven PORT en de class MyServer voor onze GET request handling
  webServer = HTTPServer(("", PORT), MyServer)
  # als de server gestart en online is, printen we de url en PORT in de console
  print("Server started https://%spython.kobevervoort1.repl.co:%s" % ("", PORT))

  # we proberen de webServer online te krijgen
  try:
    webServer.serve_forever()
  # maar als er zich een KeyboardInterrupt voordoet, doen we een pass statement (pass als placeholder voor error)
  except KeyboardInterrupt:
    pass
