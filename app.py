from flask import flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("homepage.html")

if __name__ == "__main__":
  app.debug = False
  app.run()