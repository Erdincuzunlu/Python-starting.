from typing import Dict, List

print("Hello world")

print("hello AI Era")

#### sayılar ve karakter dizileri


### ondaklı sayılara float denir ###
### karakter ve stringler arasında ki farkı tırnak koyarak yapacağız.

print(9.2)

type(9.2)

type(9)

type("MRB")


## atamalar ve değişkenker.

a = 9 ## a ifadesi bir değişkendir = ifadesi atama için kullanılır

#### sayılar : integer

x = 46
type(x)



### Liste

x = ["btc", "eth", "xrp"]
type(x)

## sözlük oluşturma (dictionary)

x = {"name": "peter", "age": 36}
type (x)


#### Tuple

x = ("python", "ml", "ds")
type(x)

 ## set

y = {"python", "numpy", "arrays"}
type(y)




print("johh")

"john"


## atama işlemi yapalım

name = "john"
name

### çok satırlı karakter dizileri
long_str = """buraya yazılacak her satırı her hangi
bir atama yaptıktan
sonra erişebişirsin her şeye"""


long_str



name[0]
name[2]

name[0:2]   ### burada 0 dan 2 ye kadar karakteri sayarak o harfleri yazdırır 0 1 ''2'' dahil değildir
name



long_str

"buraya" in long_str  ## buraya yazdığım kelime long str atadığım cümlenin içinde var mı yok mu onu sorgulamak için



####  String methodları ( karakter dizisi ) metodları

dir(str)

name
type(name)
type(len)


### stringlerde boyutuna bakacağız.... len ile

len(name)


len("vahitkeskin")
len("miuul")


#### upper ve lower büyük küçük dönüşümler.
"miull".upper()
"MİULL".lower()

#### type(upper) class içinde yer alıyorsa bir methottur.


hi = "Hello AI Era"
hi.replace("l","p")

#### split : Böler

"hello AI Era".split()

#### strip : kırpar

" ofofof".strip()
"ofofof".strip("o")


"foo".capitalize()


dir("foo")


sayı1 = int((input("birincisayı:"))
sayı2 = int(input("ikincisayı:"))
toplam = sayı1 + sayı2
print("toplam:" toplam)

sayi3 = int(input("bir sayı gir:"))
karesi = sayi3 * sayi3
print("karesi:" karesi)

sayı4 = int(input("bir sayı gir :"))
a = sayı4 + 10
print(a)


text = ("The goal is to find out if a number is greater than or equal to zero")
### verilen tüm string ifadeleri büyük harfe çeviriniz.
type(text)

text.count("zero")
len(text)

str.upper(text)

text = text.replace(",", "").replace(".", "")

words = text.split(" ")

print(words)


list = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
### adım bir verilen listenin eleman sayısına bakın
len(list)



## adım 2--  0. ve 10. indextekie elemanları çağırın.
list[0],list[10]

## Adım3: Verilenlisteüzerinden["D", "A", "T", "A"] listesioluşturunuz

yeni_list = list[0:4]
print(yeni_list)
#### sekizinci indeksteki elemanı silmek.
list.pop(8)

### adım 5. yeni bir eleman ekleyiniz.

list.append(99)

#### sekizinci indekste sildiğimiz N elemanını tekrar ekleyiniz.

list.pop(11)

list.insert(8, "N")

### son elemanı sil

list.pop(11)
print(list)


#### verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {"christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["italy", 25]}


### Adım 1 key değerlerine erişiniz.

dict.keys()

### adım 2 value değerlerine erişiniz

dict.values()

### adım 3 Daisy key değerine ait 12 değerini 13 olarak güncelle

dict["Daisy"][1] = 13
dict.keys()
dict.values()

### Adım4: Key değeriAhmet value değeri[Turkey,24] olanyeni birdeğerekleyiniz

dict["Ahmet"] = ["Turkey", 24]
dict.keys()

### Adım5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")


###AlıştırmalarGörev 5:Argümanolarakbirlistealan, listenin içerisindeki tek ve çift sayıları ayrı listele
# atayan ve bu listeleri return eden fonksiyon yazınız

list = [10, 23, 44, 21, 45, 29, 28]

def tek_ve_cift_sayilari_ayir(list):
    tek_sayilar = []
    cift_sayilar = []
    for i in list:
        if i % 2 == 0:
            cift_sayilar.append(i)
        else:
            tek_sayilar.append(i)

    return tek_sayilar, cift_sayilar

print(tek_ve_cift_sayilari_ayir(list))


### Görev 6

students = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

for index,  student in enumerate(students):
    if index < 3 :
        fakultesi = "Mühendislik fakultesi"
    else:
        fakultesi = "Tıp fakultesi"
    print(f"{student} - {fakultesi}")


#### Görev 7 bir diğer alıştırma .

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

#### zip kullanarak ders bilgilerini bastıralım.

ders_bilgileri = zip(ders_kodu, kredi, kontenjan)
for ders, kredi, kontenjan, in ders_bilgileri:
    print(f"ders_kodu: {ders}, kredi: {kredi}, kontenjan: {kontenjan}")
    print(f"kredisi {kredi} olan {ders} kodlu dersin kontenjanı {kontenjan} kişidir")



#### 2. kümenin 1. kümeden farkını yazdıracağız.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


kume1.union(kume2)
kume1.intersection(kume2)
kume1.difference(kume2)
kume1.isdisjoint(kume2)


### boolen
True
False

type(True)

1 == 1

type(1 == 1)

x = ["btc", "eth", "xrp"]
type(x)

### sözlük...

x = {"name": "peter", "age": 36}
type(x)
x.keys()
x.values()
x.items()

### tuple #### normal parantez... Listenin huysuz aksi kardeşidir ...

x = (1, 2, 3)
type(x)

### setler....

### kümeler gibi düşünürüz

x = {"python", "numpy", "arrays"}
type(x)

 #### NOT LİSTE , TUPLE , SET ,VE DİCTİONARY VERİ YAPILARI AYNI ZAMANDA PYTHON COLLECTİON ( ARRAYS) OLARAKTA GEÇER.



 b = 10.6
type(b)
a = 19
int(b)
b

float(a * b / 10)

#### karakter dizileri ( strings)

print("John")

"John"

##### ekrana bilgi paylaşmak istiyorsak o zaman print yazdırmak zorundayız... print yazmadan da işlemler yapabilirsiniz.

name = "John"

type(name)

long_str = """ veri yapıları : hızlı özet,
sayılar numbers : int , float , complex yapılar
boolean / true false """

name[0]

#### karakter dizilerinde slice işlemiiiiii

name


### sıfırıncı ve 2. string ifadelere erişmek istiyorum


name[0:2]

### string içersinde karakter sorgulama

"veri" in long_str

"comlex" in long_str

"hızlı" in long_str

"özet" in long_str


dir()


dir(str)

methods_and_attributes = dir(str)
for item in methods_and_attributes:
    print(item)


dir(int)

x = dir(int)
for item in x:
    print(item)


name = "John"

type(name)
len(name)

#### stinglerde boyut bilgisini öğrenmek için yazarız....

len("ismailerdincuzunlu")

#### python içinde gömülü olarak gelen bir method bir fonksiyondur....

#### upper() lower() küçük büyük dönüşümleri

"miuul".upper()
"MIUUL".lower()

##### replace : karakter değiştirir....
hi = "Hello world"
hi.replace("l", "p")


#### split methodu : Böler....

"Hello world".split()


#### strip kırpar

" ofofo".strip("o")

dir("foo")

#### yaygın kullanılanlar replace , upper lower , len fonksiyonu....

text = "banana"
text.upper()

text.replace("a", "o")

text.split()
hi.split("o")


##### Liste ( list) değiştirilebilir , sıralayıcıdır ve kapsayıcıdır.

notes = [1, 2, 3, 4, 5]
type(notes)

dir(notes)

x = dir(notes)
for item in x:
    print(item)


len(notes)

notes

notes.append(100)
notes.append("A")
notes

#### pop methodu indexe göre siler ...

notes.pop(6)

#### eleman eklemek istersekte insert methodu kullanırız.

notes.insert(2, 222)
notes

####1.	Liste Oluşturma ve Erişim:
	###fruits adında bir liste oluşturun ve "apple", "banana", "cherry" elemanlarını ekleyin. Daha sonra bu listeden "banana" elemanına nasıl erişeceğinizi gösterin.

fruits = ["apple", "banana", "cherry"]

fruits[1]

#### 2.	Liste Eleman Ekleme:
	##Yukarıdaki fruits listesine "orange" elemanını eklemek için hangi metodu kullanırsınız? Kodunuzu yazın.

fruits.append("orange")

### 3.	Liste Elemanlarını Güncelleme:
    #fruits listesindeki "banana" elemanını "blueberry" ile değiştirin. Bu işlemi nasıl yaparsınız?

dir(fruits)
type(fruits)
fruits
fruits.pop(1)
fruits.insert(1, "blueberry")
fruits
## 4.	Liste Eleman Silme:
	## fruits listesindeki "apple" elemanını silmek için hangi metodu kullanırsınız? Kodunuzu yazın.

fruits.pop(0)

## 5.	Liste Uzunluğu:
	##fruits listesinin uzunluğunu bulun. Hangi fonksiyonu kullanırsınız?

len(fruits)

##6.	Liste İçerisinde Arama:
##	fruits listesinde "cherry" elemanının olup olmadığını kontrol edin ve sonucu ekrana yazdırın.

"cherry" in fruits
if "cherry" in fruits:
    print("cherry")

##	Listeyi Ters Çevirme:
	##fruits listesindeki elemanları ters sıraya çevirin. Bunu hangi metotla yaparsınız?

fruits.reverse()
fruits

#### dictionary

### sırasız (3.7 'den sonra sıralı )
## kapsayıcı

## key - values

dictionary = {"REG": "Regression",
              "Log": "Logistic Regression",
              "CART": "Classification and regression" }

dictionary["REG"]


dictionary: = {"REG": ["Regression",19],
              "Log": ["Logistic Regression",21],
              "CART": ["Classification and regression", 31]}

dictionary["Log"][0]
dictionary["Log"][1]

dictionary.keys()
dictionary.values()

"Regression" in dictionary
"Classification and regression" in dictionary
"REG" in dictionary

"Classification and regression" in dictionary

"Logistic Regression" in dictionary

dictionary["REG"] = ["Regression",13]

"CART" in dictionary

dictionary.keys()
dictionary.values()

### tüm çiftleri tuple halinde listeye çevirme

dictionary.items()

dictionary.update({"CART":["Classification  regression",31]})

dictionary.update({"ER": [12, 33]})

## 1.	Sözlük Oluşturma:
	#	car adında bir sözlük oluşturun ve "brand", "model", "year" anahtarlarını "Toyota", "Corolla", 2020 değerleriyle tanımlayın.

car = {"brand": "toyota",
       "model": "Corolla",
       "year": 2020,}

## 2.	Anahtar Değerine Erişim:
	#	car sözlüğünden "model" anahtarına karşılık gelen değeri nasıl alırsınız?

car["model"]

##3.	Sözlüğe Yeni Eleman Ekleme:
##	car sözlüğüne "color" anahtarı ile "blue" değerini ekleyin.

car.update({"color": "blue"})

##4.	Bir Değeri Güncelleme:
	#	car sözlüğündeki "year" anahtarını 2021 olarak güncelleyin.
car.update({"year": 2021})

## 5.	Bir Elemanı Silme:
#	car sözlüğünden "model" anahtarını silin.

car.pop("model")


### 1.	Arkadaş İsimlerini İçeren Bir Liste Oluşturun
      #Liste adı: friends
	#İsimler: "Ali", "Ayşe", "Mehmet", "Elif"

friends = ["Ali", "Ayşe", "Mehmet", "Elif"]

# 2.	Listeye Yeni Bir İsim Ekleyin
# 	•	Yeni isim: "Burak"

friends.append("Burak")

#3.	Listenin Sonundaki İsimden Kurtulun
	#Listenin sonundaki elemanı silin.

len(friends)
friends.pop(4)

#4.	Listenin İlk İsimlerini Güncelleyin
	# İlk isim: "Ali" yerine "Ahmet" olarak değiştirin.

friends.insert(0, "Ahmet")
friends.remove("Ali")
friends




##5.	Liste İçerisinde Bir İsim Arayın
	# İsim: "Elif" liste içinde var mı diye kontrol edin.

"Elif" in friends

## 6.	Listeyi Alfabetik Sıraya Göre Sıralayın
	# Listeyi alfabetik sıraya göre sıralayın.

friends.sort()
friends


#### Demet Tuple..

### değiştirelemez...
### Sıralıdır..
## kapsayıcıdır.

t = ("john", "mark", 1, 2)

type(t)

t[0]
t[0:3]

#### küme işlemleri SET

## değiştirilebilir
## Sırasız + Eşsizdir..
## kapsayıcıdır.



set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

type(set1)

### set 1 de olup set 2 de olmayanlar...

set1.difference(set2)

### symetric_difference iki kümede de birbirlerine göre olmayanlar..

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#### iki kümenin kesişimi

set1.intersection(set2)
set2.intersection(set1)

### iki küme birleşimii
set1.union(set2)
set2.union(set1)

#### iki kümenin kesişimi boş mu ??

set1.isdisjoint(set2)
set2.isdisjoint(set1)

### Bir küme diğer kümenin lat kümesi midir ?

set1.issubset(set2)
set2.issubset(set1)

#### Bir küme diğer kümeyi kapsıyor mu ?

set1.issuperset(set2)
set2.issuperset(set1)


