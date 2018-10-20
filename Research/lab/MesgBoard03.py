from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs as pq
memory=[]
form = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Message Board</title>
</head>
<body>
	<form method="POST" action="http://localhost:9000/">
		<textarea name="message"></textarea>
		<br>
		<br>
		<button type="submit">Post it!</button>
	</form>
</body>
<pre>{}</pre>
</html>'''


class MessageHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		length = int(self.headers.get('Content-length', 0))
		data = self.rfile.read(length).decode()
		message = pq(data)["message"][0]
		message = message.replace("<","&It;")
		memory.append(message)
		self.send_response(303)
		self.send_header('Location','/')
		self.end_headers()


	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html;charset=utf-8')
		self.end_headers()
		mesg = form.format("\n".join(memory))
		self.wfile.write(mesg.encode())


if __name__ == '__main__':
	server_address = ('', 9000)
	httpd = HTTPServer(server_address, MessageHandler)
	httpd.serve_forever()
