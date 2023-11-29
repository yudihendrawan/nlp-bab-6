import re

text = "Buku 'Pendekar Hina Kelana' oleh Kho Ping Hoo adalah sebuah karya terkenal."


author_match = re.search(r"'(.*?)' oleh (.*?) adalah",text)

if author_match:
 title = author_match.group(1)
 author = author_match.group(2)
 print(f"Judul buku: {title}")
 print(f"Nama pengarang: {author}")


# contoh 1
import re

teks1 = "Novel 'Laskar Pelangi' oleh Andrea Hirata telah menjadi bestseller."

match_penulis1 = re.search(r"'(.*?)' oleh (.*?) telah", teks1)

if match_penulis1:
 judul1 = match_penulis1.group(1)
 penulis1 = match_penulis1.group(2)
 print(f"Judul buku: {judul1}")
 print(f"Nama pengarang: {penulis1}")


# contoh 2

import re

teks2 = "Film 'Dilan 1990' karya Pidi Baiq berhasil mencuri perhatian penonton."

match_penulis2 = re.search(r"'(.*?)' karya (.*?) berhasil", teks2)

if match_penulis2:
 judul2 = match_penulis2.group(1)
 penulis2 = match_penulis2.group(2)
 print(f"Judul buku: {judul2}")
 print(f"Nama pengarang: {penulis2}")


# contoh 3

import re

teks3 = "Album 'Rumah Kita' oleh God Bless masih menjadi favorit banyak orang."

match_penulis3 = re.search(r"'(.*?)' oleh (.*?) masih", teks3)

if match_penulis3:
 judul3 = match_penulis3.group(1)
 penulis3 = match_penulis3.group(2)
 print(f"Judul buku: {judul3}")
 print(f"Nama pengarang: {penulis3}")
