from flask import Flask, render_template
app = Flask(__name__)


@app.route("/request-counter")
def request_counter():
    return render_template("counter.html")


@app.route("/request-counter", methods=['POST'])
def request_counter_post():
    return render_template("counter.html")


@app.route("/")
def root():
    return render_template("first.html")


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
