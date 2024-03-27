"""
JSON (JavaScript Object Notation) adalah format file berbasis teks yang umumnya digunakan dalam proses pertukaran data antara server dan klien.

Python memiliki paket bawaan bernama json, yang dapat digunakan untuk bekerja dengan data JSON.
    1. JSON adalah sintaks untuk menyimpan dan bertukar data.
    2. JSON adalah teks yang ditulis dengan notasi objek JavaScript.

1. JSON dengan Python
    import json
2. Parsing JSON - Konversi dari JSON ke Python
    a. Jika Anda memiliki string JSON, Anda dapat menguraikannya dengan menggunakan json.loads() metode ini.
    b. Hasilnya akan menjadi dict Python .
3. Konversi dari Python ke JSON
    Jika Anda memiliki objek Python, Anda dapat mengubahnya menjadi string JSON dengan menggunakan json.dumps()metode ini
4. Anda dapat mengonversi objek Python dari tipe berikut, menjadi string JSON:
    Python	        JSON
    dict	        Object
    list	        Array
    tuple	        Array
    str	            String
    int	            Number
    float	        Number
    True	        true
    False	        false
    None	        null
5. Format the Result
    a. Contoh di atas mencetak string JSON, tetapi tidak mudah dibaca, tanpa lekukan dan jeda baris.
    b. Metode ini json.dumps() memiliki parameter untuk memudahkan membaca hasilnya
        - Gunakan indent parameter untuk menentukan jumlah indentasi
        - Gunakan separators parameter untuk mengubah pemisah default, nilai defaultnya adalah (", ", ":")
6. Order the Result
    Metode ini json.dumps() memiliki parameter untuk mengurutkan kunci dalam hasil
        Gunakan sort_keys parameter untuk menentukan apakah hasilnya harus diurutkan atau tidak
"""
## Parsing JSON - Konversi dari JSON ke Python
# 1. Konversi dari JSON ke Python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# 2. Konversi dari Python ke JSON
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# 3. Ubah objek Python menjadi string JSON, dan cetak nilainya
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# 4. Konversikan objek Python yang berisi semua tipe data legal
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

## 5. Format the Result
# indent parameter
print(json.dumps(x, indent=4))

# separators parameter
print(json.dumps(x, indent=4, separators=(". ", " = ")))

## 6. Order the Result
# sort_keys parameter
print(json.dumps(x, indent=4, sort_keys=True))