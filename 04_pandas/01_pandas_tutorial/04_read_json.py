"""
Pandas Read JSON
    1. Kumpulan data besar sering kali disimpan, atau diekstraksi sebagai JSON.
    2. JSON merupakan teks biasa, namun memiliki format objek, dan terkenal di dunia pemrograman, termasuk Pandas.
    3. Tip: gunakan to_string()untuk mencetak seluruh DataFrame.

Dict sebagai JSON
    1. JSON = dict Python
    2. Objek JSON memiliki format yang sama dengan dict Python.
    3. Jika kode JSON Kita tidak ada dalam file, tetapi dalam Kamus Python, Kita dapat memuatnya ke dalam DataFrame secara langsung
"""
## Muat JSON ke dalam DataFrame
import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())

## Muat dict Python ke dalam DataFrame
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)