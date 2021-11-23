from flask import Flask, send_from_directory, send_file

app = Flask(__name__)


@app.route("/<path:path>")
def static_dir(path):
    print(path)
    if path is None:
        return send_file("index.html")
    else:
        return send_from_directory("", path)


@app.route('/')
def entry():
    return send_file("index.html")


if __name__ == "__main__":
    app.run()
