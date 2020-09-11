from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/AboutUs")
# def about():
#     return render_template("AboutUs.html")

# @app.route("/OurWork")
# def our():
#     return render_template("OurWork.html")

# @app.route("/JoinUs")
# def us():
#     return render_template("JoinUs.html")

app.run(debug= True)