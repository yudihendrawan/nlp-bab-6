# gunakan google collaboration

import spacy

# Mengunduh model bahasa Inggris dengan dukungan medis dari spaCy
# (Pastikan untuk menjalankan ini hanya sekali)
# python -m spacy download en_core_med7_lg
nlp = spacy.load("en_core_web_sm")

# Contoh catatan medis
catatan_medis = """
Pasien mengeluhkan nyeri dada yang berlanjut selama satu jam. Tidak ada riwayat serangan jantung sebelumnya.
Tekanan darah sistolik tinggi, mencapai 160 mmHg. Pasien merokok sejak 10 tahun terakhir.
Pemeriksaan fisik menunjukkan denyut jantung yang cepat dan sesak napas.
"""

# Proses catatan medis menggunakan spaCy
doc = nlp(catatan_medis)

# Ekstraksi gejala
gejala = [ent.text for ent in doc.ents if ent.label_ == "SYMPTOM"]
if gejala:
    print("Gejala yang diekstraksi:", gejala)
else:
    print("Tidak ada gejala yang diekstraksi.")

# Ekstraksi riwayat penyakit
riwayat_penyakit = [ent.text for ent in doc.ents if ent.label_ == "DISEASE"]
if riwayat_penyakit:
    print("Riwayat penyakit yang diekstraksi:", riwayat_penyakit)
else:
    print("Tidak ada riwayat penyakit yang diekstraksi.")
