from collections import Counter

def analisis_angka_ikut(histori):
    if len(histori) < 11:
        return {"error": "Minimal 11 putaran diperlukan."}

    window_size = 10
    results = []
    akurasi_count = 0

    for i in range(window_size, len(histori)):
        window = histori[i - window_size:i]
        
        weighted_digits = []
        for j, nomor in enumerate(window):
            if j >= 5:
                weighted_digits.extend(list(nomor))
                weighted_digits.extend(list(nomor))
            else:
                weighted_digits.extend(list(nomor))
        
        frekuensi = Counter(weighted_digits)
        angka_ikut = [d for d, _ in frekuensi.most_common(6)]
        angka_set = set(angka_ikut)
        
        hasil_kini = histori[i]
        digit_hasil = set(hasil_kini)
        
        status = "MASUK" if digit_hasil.issubset(angka_set) else "KELUAR"
        if status == "MASUK":
            akurasi_count += 1
        
        results.append({
            "putaran": i + 1,
            "hasil": hasil_kini,
            "angka_ikut": ''.join(angka_ikut),
            "status": status
        })

    total = len(histori) - window_size
    akurasi = round(akurasi_count / total * 100, 1)

    window_terakhir = histori[-10:]
    weighted_digits = []
    for j, nomor in enumerate(window_terakhir):
        if j >= 5:
            weighted_digits.extend(list(nomor))
            weighted_digits.extend(list(nomor))
        else:
            weighted_digits.extend(list(nomor))
    frekuensi = Counter(weighted_digits)
    angka_ikut_next = ''.join([d for d, _ in frekuensi.most_common(6)])

    return {
        "results": results,
        "ringkasan": {
            "total_masuk": akurasi_count,
            "total": total,
            "akurasi": akurasi
        },
        "rekomendasi": angka_ikut_next
    }
