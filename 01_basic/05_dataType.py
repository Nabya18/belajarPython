'''
1. Built-in Data Types
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set,frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
2. Mengatur tipe data tertentu
    Jika ingin menentukan tipe data, dapat menggunakan fungsi konstruktor berikut:
    x = str("Hello World")	                        str
    x = int(20)	                                    int
    x = float(20.5)	                                float
    x = complex(1j)	                                complex
    x = list(("apple", "banana", "cherry"))	        list
    x = tuple(("apple", "banana", "cherry"))	    tuple
    x = range(6)	                                range
    x = dict(name="John", age=36)	                dict
    x = set(("apple", "banana", "cherry"))	        set
    x = frozenset(("apple", "banana", "cherry"))	frozenset
    x = bool(5)	                                    bool
    x = bytes(5)	                                bytes
    x = bytearray(5)	                            bytearray
    x = memoryview(bytes(5))	                    memoryview
3. Binary Type
    digunakan untuk bekerja dengan data biner dan tampilan memori data biner.
    untuk tugas-tugas seperti menangani file biner, komunikasi jaringan, dan manipulasi data tingkat rendah.
    - byte => tipe urutan yang tidak dapat diubah untuk mewakili urutan byte (nilai 8-bit)
        a. Setiap elemen dalam suatu bytesobjek adalah bilangan bulat dalam rentang [0, 255]
        b. untuk menangani data biner, seperti membaca/menulis file, komunikasi jaringan, atau menyandikan/mendekode data.
    - bytearray => objek dapat dimodifikasi setelah pembuatan
        untuk mengubah data biner yang ada, seperti saat memproses file biner atau protokol jaringan
    - memoryview => untuk membuat “tampilan” memori yang berisi data biner
        a. memberikan tampilan ke dalam memori tempat data disimpan
        b. berguna untuk memanipulasi data dalam jumlah besar secara efisien tanpa menyalinnya.
        c. digunakan dalam skenario tingkat lanjut yang memerlukan manipulasi memori langsung, seperti pada aplikasi berperforma tinggi.
4. None => mewakili nilai khusus yang menunjukkan tidak adanya nilai.
'''

a = "Hello World"
print(type(a))

# Contoh byte
my_bytes = b'Hello, World!'
print(type(my_bytes))

# contoh bytearray
my_bytearray = bytearray([72, 101, 108, 108, 111])
print(type(my_bytearray))

# contoh memoryview
data = bytearray([1, 2, 3, 4, 5])
mem_view = memoryview(data)
print(type(mem_view))

# contoh None
no_value = None
print(type(no_value))