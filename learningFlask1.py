from flask import Flask, redirect, url_for

app = Flask(__name__)

# make a homepage with header
@app.route("/")
def home():
    return "<h1>On home page<h1>"
    
# make a page for whatever the user types after the slash
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
    
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
    
# run
if __name__ == "__main__":
    app.run()