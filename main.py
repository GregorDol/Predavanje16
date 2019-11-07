from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def prva_stran():
    return render_template("prva_stran.html")

@app.route("/kontakt")
def kontakt():
    emaili = ["ime@example.com", "ime@gmail.com", "ime@hotmail.com"]
    return render_template("kontakt.html", emaili=emaili)

@app.route("/poslji-sporocilo", methods=["POST"])
def poslji_sporocilo():
    zadeva = request.form.get("zadeva")
    sporocilo = request.form.get("sporocilo")

    #Tukaj bi shranili te spremenlkjivki v bazo.

    return render_template("sporocilo_poslano.html", zadeva=zadeva)


@app.route("/o_meni")
def o_meni():
    return render_template("o_meni.html")

if __name__ == '__main__':
    app.run()