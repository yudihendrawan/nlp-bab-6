class MesinPencari:
    def __init__(self):
        self.dokumen = {
            1: "Penyakit jantung adalah kondisi kesehatan yang melibatkan kerusakan atau kegagalan jantung.",
            2: "Gangguan kardiovaskular dapat mencakup berbagai masalah kesehatan terkait sistem kardiovaskular.",
            3: "Mencegah penyakit jantung melibatkan gaya hidup sehat, termasuk pola makan dan aktivitas fisik.",
            4: "Faktor risiko penyakit jantung termasuk merokok, kekurangan olahraga, dan pola makan tidak sehat.",
            5: "Pola makan mediterania diketahui dapat membantu mengurangi risiko penyakit jantung.",
            6: "Olahraga teratur seperti berlari atau berenang dapat meningkatkan kesehatan jantung.",
            7: "Tekanan darah tinggi merupakan faktor risiko utama untuk penyakit kardiovaskular.",
            8: "Makanan tinggi kolesterol, seperti daging merah, sebaiknya dikonsumsi dengan bijak."
        }

    def cari_informasi(self, query):
        hasil_pencarian = []
        for id_dokumen, konten in self.dokumen.items():
            if query.lower() in konten.lower():
                hasil_pencarian.append((id_dokumen, konten))
        return hasil_pencarian

# Contoh Penggunaan:
mesin_pencari = MesinPencari()

while True:
    query = input("Masukkan pertanyaan atau kata kunci (ketik 'selesai' untuk keluar): ")
    if query.lower() == "selesai":
        print("Terima kasih, sampai jumpa!")
        break

    hasil_pencarian = mesin_pencari.cari_informasi(query)

    if hasil_pencarian:
        print("\nHasil Pencarian:")
        for id_dokumen, konten in hasil_pencarian:
            print(f"Dokumen #{id_dokumen}: {konten}")
    else:
        print("Maaf, tidak ada hasil yang sesuai.")
    print()
