from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def prva_stran():
    return render_template("prva_stran.html")

@app.route("/kontakt")
def kontakt():
    emaili = ["ime@example.com", "ime@gmail.com", "ime@hotmail.com"]
    return render_template("kontakt.html", emaili=emaili)

@app.route("/o_meni")
def o_meni():
    return render_template("o_meni.html")

if __name__ == '__main__':
    app.run()