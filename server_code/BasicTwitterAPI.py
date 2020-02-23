from twitter import Twitter, OAuth
import secrets
import json
import http.server

global session


class JSONHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(session.statuses.user_timeline(screen_name="TweetOrYeet1")).encode())


if __name__ == '__main__':
    session = Twitter(auth=OAuth(secrets.token, secrets.token_secret, secrets.consumer_key, secrets.consumer_secret))
    httpd = http.server.HTTPServer(('', 8080), JSONHTTPRequestHandler)
    httpd.serve_forever()
