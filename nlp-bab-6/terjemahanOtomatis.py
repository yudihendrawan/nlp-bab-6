# from googletrans import Translator

# text = "Hello, how are you?"

# translator = Translator()
# translation = translator.translate(text,src='en',dest='id')
# print("Terjemahan: ", translation.text)

from googletrans import Translator

def terjemahkan(teks, bahasa_destinasi):
 translator = Translator()
 terjemahan = translator.translate(teks, src='en', dest=bahasa_destinasi)
 return terjemahan.text

def tampilkan_menu():
 print()
 print("Pilih terjemahan:")
 print("1. Terjemahan dalam bahasa Indonesia")
 print("2. Terjemahan dalam bahasa Spanyol")
 print("3. Terjemahan dalam bahasa Prancis")

def main():
 teks_asli = "Hello, how are you?"

 while True:
  tampilkan_menu()
  pilihan = input("Masukkan nomor pilihan (1/2/3) atau ketik 'exit' untuk keluar: ")
  print()
  if pilihan == '1':
      terjemahan_id = terjemahkan(teks_asli, 'id')
      print(f"Terjemahan dalam bahasa Indonesia: {terjemahan_id}")
  elif pilihan == '2':
      terjemahan_es = terjemahkan(teks_asli, 'es')
      print(f"Terjemahan dalam bahasa Spanyol: {terjemahan_es}")
  elif pilihan == '3':
      terjemahan_fr = terjemahkan(teks_asli, 'fr')
      print(f"Terjemahan dalam bahasa Prancis: {terjemahan_fr}")
  elif pilihan.lower() == 'exit':
      print("Program selesai.")
      break
  else:
      print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3, atau ketik 'exit' untuk keluar.")

if __name__ == "__main__":
 main()
