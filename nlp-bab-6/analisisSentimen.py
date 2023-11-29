from textblob import TextBlob

# Teks harus menggunakan bahasa inggris
# jika text menggunakan bahasa Indonesia hasilnya netral semua

# Teks ulasan produk
text = "This product is very good and I really like it"

# Analisis sentimen
analysis = TextBlob(text)
sentiment = analysis.sentiment.polarity

print (sentiment)
if sentiment > 0:
 print('Sentimen positif')
elif sentiment < 0:
 print('Sentimen negatif')
else:
 print('Sentimen netral')


# contoh 1 
# Teks ulasan produk
text1 = "The quality of this item is terrible, and I'm really disappointed."

# Analisis sentimen
analysis1 = TextBlob(text1)
sentiment1 = analysis1.sentiment.polarity

print(sentiment1)
if sentiment1 > 0:
    print('Sentimen positif')
elif sentiment1 < 0:
    print('Sentimen negatif')
else:
    print('Sentimen netral')


# contoh 2

# Teks ulasan produk
text2 = "I'm indifferent towards this product; it neither impressed me nor disappointed me."

# Analisis sentimen
analysis2 = TextBlob(text2)
sentiment2 = analysis2.sentiment.polarity

print(sentiment2)
if sentiment2 > 0:
    print('Sentimen positif')
elif sentiment2 < 0:
    print('Sentimen negatif')
else:
    print('Sentimen netral')


# contoh 3
# Teks ulasan produk
text3 = "I have mixed feelings about this item; some features are great, but others need improvement."

# Analisis sentimen
analysis3 = TextBlob(text3)
sentiment3 = analysis3.sentiment.polarity

print(sentiment3)
if sentiment3 > 0:
    print('Sentimen positif')
elif sentiment3 < 0:
    print('Sentimen negatif')
else:
    print('Sentimen netral')


