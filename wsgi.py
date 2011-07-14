import web

urls = ("/.*", "hello")
application = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

if __name__ == "__main__":
    application.run()

