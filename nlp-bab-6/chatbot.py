# import random

# pertanyaan_jawaban = {
#  "Siapa namamu?" : "Saya adalah ChatBot.",
#  "Apa kabar?" : "Saya baik. Bagaimana dengan Anda?",
#  "Apa yang bisa kamu lakukan?" : "Saya bisa menjawab pertanyaan dan membantu Anda dengan informasi.",
#  "Terima kasih" : "Sama-sama! Jika Anda memiliki pertanyaan lebih lanjut, tanyakan saja."
# }

# def chatbot (pertanyaan):
#  jawaban = pertanyaan_jawaban.get(pertanyaan,"Maaf, saya tidak tahu jawabannya.")
#  return jawaban

# while True:
#  input_pengguna = input("Pertanyaan: ")
#  if input_pengguna.lower()== "selesai":
#   print("Terima kasih, sampai jumpa!")
#   break
#  jawaban_chatbot = chatbot(input_pengguna)
#  print("ChatBot: ", jawaban_chatbot)



import random

pertanyaan_jawaban = {
    "Siapa penemu gravitasi?" : "Gravitasi ditemukan oleh Sir Isaac Newton.",
    "Apakah bumi datar?" : "Tidak, bumi berbentuk bulat.",
    "Apa makanan favoritmu?" : "Sebagai ChatBot, saya tidak memiliki makanan favorit.",
    "Apa tujuan hidupmu?" : "Tujuan saya adalah membantu Anda dengan pertanyaan dan informasi.",
    "Terima kasih" : "Sama-sama! Jika ada pertanyaan lain, silakan tanyakan."
}

def chatbot(pertanyaan):
    jawaban = pertanyaan_jawaban.get(pertanyaan, "Maaf, saya tidak tahu jawabannya.")
    return jawaban

while True:
    input_pengguna = input("Pertanyaan: ")
    if input_pengguna.lower() == "selesai":
        print("Terima kasih, sampai jumpa!")
        break
    jawaban_chatbot = chatbot(input_pengguna)
    print("ChatBot: ", jawaban_chatbot)
