# SonOyuncu Web Scraping Araci

 Bu basit arac, SonOyuncu web sitesinden oyun siralamalarini almaniza yardimci olur.

 - `gswusername` fonksiyonuyla bir kullanicinin adina gore siralamayi ve puani alabilirsiniz. 
 
 - `gswrank` fonksiyonuyla belirli bir siralama numarasina gore kullanicinin adi ve puanini alabilirsiniz.

 - `listrank` fonksiyonyla ise belirlediginiz tarih icerisindeki siralamadaki butun siralamasi kullanici adlari ve puanini alabilirsiniz.

 ## Kurulum

 Bu araci kullanmak icin, Python'un `requests` ve `beautifulsoup4` kutuphanelerini yuklemeniz gerekmektedir. Bunlari yuklemek icin terminal veya komut istemcisine su komutlari girin:

 ```bash
 pip install requests
 pip install beautifulsoup4
 ```

## Kullanim

 ### **Kullanici Adina Gore Siralama ve Puan Alma**

 ```python

 username = "lumiin"
 game = "thebridge"  # Oyun adi (bedwars,skywars)
 time = "2024"     # Zaman periyodu (062023, 2022, bos birakilirsa kalici siralama)

 siralama_info = gswusername(username, game, time)
 print(siralama_info)
 ```

 ### **Siralama Numarasina Gore Kullanicinin Adi ve Puan Alma**

 ```python

 rank = "1."          # Siralama numarasi
 game = "thebridge"  # Oyun adi (bedwars,skywars)
 time = "2024"     # Zaman periyodu (062023, 2022, Bos birakilirsa kalici siralama)

 siralama_info = gswrank(rank, game, time)
 print(siralama_info)
 ```

 ### **Oyun Adina Gore Tum Kullanicilarin Siralamasi Adi ve Puanini Alma**
 
 #### Siralamalari Kullanici Adlarini ve Puanlari Yazdirir

 ```python
 game = "thebridge" # Oyun adi
 time = "2024"     # Zaman periyodu (062023, 2022, Bos birakilirsa kalici siralama)

 siralama_info = listrank(game,time)
 print(siralama_info)
 ```

 #### Sadece Kullanici Adlarini Yazdirir

 ```python
 game = "thebridge" # Oyun adi
 time = "2024"     # Zaman periyodu (062023, 2022, Bos birakilirsa kalici siralama)

 siralama_info = listrank(game,time)
 for user in siralama_info:
    print(user['username'])
 ```

 #### Siralama Ve Kullanici Adi Yazdirir

  ```python
 game = "thebridge" # Oyun adi
 time = "2024"     # Zaman periyodu (062023, 2022, Bos birakilirsa kalici siralama)

 siralama_info = listrank(game,time)
 for user in siralama_info:
    print(user['siralama']+user['username'])
 ```