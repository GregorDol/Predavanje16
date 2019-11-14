from flask import Flask, render_template, request, redirect, make_response
from modeli import Komentar, db


app = Flask(__name__)
db.create_all()



@app.route("/")
def prva_stran():
    ime = request.cookies.get("ime")

    #Preberemo vse komentarje
    komentarji = db.query(Komentar).all()

    return render_template("prva_stran.html", ime=ime, komentarji=komentarji)


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




@app.route("/prijava", methods=["POST"])
def prijava():
    ime = request.form.get("ime")

    odgovor = make_response(redirect("/"))
    odgovor.set_cookie("ime", ime)
    return odgovor


@app.route("/komentar", methods=["POST"])
def poslji_komentar():
    vsebina_komentarja = request.form.get("vsebina")

    # Tukaj se bo shranil kometar v podatkovno bazo

    komentar = Komentar(
        avtor=request.cookies.get("ime"),
        vsebina = vsebina_komentarja
    )
    db.add(komentar)

    db.commit()

    return redirect("/")


@app.route("/o_meni")
def o_meni():
    return render_template("o_meni.html")

if __name__ == '__main__':
    app.run(debug=True)