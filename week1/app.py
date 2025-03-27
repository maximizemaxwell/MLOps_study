from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"


@app.route("/index", methods=["GET"])
def welcome_index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


# ## Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template("result.html", results=res)


## Variable Rule
@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {"score": score, "res": res}

    return render_template("result1.html", results=exp)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")


@app.route("/sucessif/<int:score>")
def successif(score):
    return render_template("result.html", results=score)


if __name__ == "__main__":
    app.run(debug=True)
