from flask import Flask, render_template, request
import re
from analisis_angka_ikut import analisis_angka_ikut

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil_analisis = None
    error = None
    input_text = ""

    if request.method == "POST":
        raw_input = request.form["histori"].strip()
        input_text = raw_input
        
        entries = [s.strip() for s in re.split(r"[,\n\s]+", raw_input) if s.strip()]
        
        valid = True
        histori = []
        for entry in entries:
            if not entry.isdigit() or len(entry) != 4:
                valid = False
                break
            histori.append(entry)
        
        if not valid:
            error = "Semua entri harus berupa angka 4 digit (contoh: 1234). Pisahkan dengan koma, spasi, atau enter."
        else:
            hasil_analisis = analisis_angka_ikut(histori)

    return render_template("index.html", 
                         hasil=hasil_analisis, 
                         error=error, 
                         input=input_text)

if __name__ == "__main__":
    app.run(debug=True)
