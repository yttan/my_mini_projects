import BaseHTTPServer
import sys, os, time

class http_request_handler(BaseHTTPServer.BaseHTTPRequestHandler):


    error_template = '''<html>
    <body>
    <h1>Error accessing {path}</h1>
    <p>{error}</p>

    <p>This is your request information</p>
    <table><tr><td>Headers</td><td>{headers}</td></tr>
    <tr><td>Time</td><td>{time}</td></tr>
    <tr><td>Client</td><td>{client}</td></tr>
    <tr><td>Command</td><td>{command}</td></tr>
    <tr><td>Path</td><td>{path}</td></tr>
    </table></body></html>'''

    def do_GET(self):
        try:
            path = os.getcwd() + self.path
            if os.path.exists(path):
                if os.path.isfile(path):
                    self.genertate_html_file(path)
                else:
                    raise server_exception("'{}' is not a vaild file".format(self.path))
            else:
                raise server_exception("'{}' does not exist".format(self.path))
        except Exception as do_get_exception:
            self.handle_error(do_get_exception)

    def handle_error(self, error_message):
        values = {
        'path':self.path,
        'error':error_message,
        'headers' : self.headers,
        'time'   : self.date_time_string(),
        'client' : self.client_address,
        'command'     : self.command,
        }
        page = self.error_template.format(**values)
        self.send_page(page)

    def genertate_html_file(self,path):
        try:
            with open(path, 'rb') as myfile:
                data = myfile.read()
            self.send_page(data)
        except IOError as file_exception:
            self.handle_error(file_exception)


    def send_page(self,page):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

class server_exception(Exception):
    pass

if __name__ == '__main__':
    server_address = ('', 8080)
    server = BaseHTTPServer.HTTPServer(server_address, http_request_handler)
    print time.asctime(), "Server Starts"
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print time.asctime(), "Server Stops"
