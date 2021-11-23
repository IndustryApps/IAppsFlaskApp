from flask import Flask, send_from_directory, send_file, redirect
from flask_eureka import Eureka

APPCODE = ''
HOSTNAME = ''

if not APPCODE:
    print('AppCode cannot be null or empty. You can find the appCode in your app\'s publish page')
    exit(0)
if not HOSTNAME:
    print('A proper hostname should be provided. You can provide your app\'s public domain name')
    exit(0)

app = Flask(__name__)
app.config.update(
    SERVICE_NAME=APPCODE,
    EUREKA_SERVICE_URL='https://servicediscovery.uat.industryapps.net/',
    EUREKA_INSTANCE_HOSTNAME=HOSTNAME,
    EUREKA_INSTANCE_PORT=80
)

eureka = Eureka(app)
eureka.register_service(name=APPCODE)


@app.route('/healthcheck')
def health_check():
    return redirect("/")


@app.route("/<path:path>")
def static_dir(path):
    if path is None:
        return send_file("index.html")
    else:
        return send_from_directory("", path)


@app.route('/')
def entry():
    return send_file("index.html")


if __name__ == "__main__":
    app.run()
