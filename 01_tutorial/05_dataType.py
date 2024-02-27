'''
1. Built-in Data Types
    Jenis Teks:	str
    Jenis Numerik:	int, float, complex
    Jenis Urutan:	list, tuple, range
    Jenis Pemetaan:	dict
    Jenis Set:	set,frozenset
    Tipe Boolean:	bool
    Jenis Biner:	bytes, bytearray, memoryview
    Tidak ada Jenis:	NoneType
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
'''

a = "Hello World"

print(type(a))