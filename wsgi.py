import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

# Turn our web.py app into a WSGI app
application = app.wsgifunc()

# But make this file runnable with Python for local dev mode
if __name__ == "__main__":
    app.run()

