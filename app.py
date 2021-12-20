from flask import send_from_directory, send_file, Flask
from flask_eureka import Eureka
from flask_eureka.eureka import eureka_bp

from controller.aas_controller import aas

APPCODE = ''  # eg: 82a506
HOSTNAME = ''  # eg: b0d3-2405-201-f00f-30a0-a527-2ade-621c-997d.ngrok.io

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
    EUREKA_HOME_PAGE_URL="https://" + HOSTNAME,
    EUREKA_INSTANCE_PORT=80
)

eureka = Eureka(app)
eureka.register_service(name=APPCODE)

app.register_blueprint(eureka_bp)
app.register_blueprint(aas, url_prefix='/aas')


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
    app.run(port=5001)
