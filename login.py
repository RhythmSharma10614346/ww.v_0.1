def login(self):
    self.send_response(200) # status ok
    self.send_header('Content-type','text/html')# content type is html file
    self.end_headers() 	# end of headers
    self.wfile.write("<h1>Login Page</h1>")
