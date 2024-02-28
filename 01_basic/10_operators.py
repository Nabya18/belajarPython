"""
Operator digunakan untuk melakukan operasi pada variabel dan nilai.
Macam-macam operator:
1.  Arithmetic operators => digunakan dengan nilai numerik untuk melakukan operasi matematika umum
    Operator	    Name	            Example
    +	            Addition	        x + y
    -	            Subtraction	        x - y
    *	            Multiplication	    x * y
    /	            Division	        x / y
    %	            Modulus	            x % y
    **	            Exponentiation	    x ** y
    //	            Floor division	    x // y      => Menghilangkan anbgka desimal (dibulatkan)

2.  Assignment operators => digunakan untuk menetapkan nilai ke variabel
    Operator	    Example	            Same As         Explaination
    =	            x = 5	            x = 5           menetapkan nilai 5 ke variabel x.
    +=	            x += 3	            x = x + 3       menambahkan 3 ke nilai variabel x.
    -=	            x -= 3	            x = x - 3       mengurangkan 3 dari nilai variabel x.
    *=	            x *= 3	            x = x * 3       mengalikan nilai variabel x dengan 3.
    /=	            x /= 3	            x = x / 3       membagi nilai variabel x dengan 3.
    %=	            x %= 3	            x = x % 3       nilai x akan diambil sisa pembagiannya dengan 3.
    //=	            x //= 3	            x = x // 3      nilai x akan dibagi dengan 3 lalu dibulatkan.
    **=	            x **= 3	            x = x ** 3      nilai x akan dipangkatkan dengan 3.

    operator-operator dibawah sering digunakan untuk melakukan manipulasi bit pada variabel
    yang berguna dalam situasi-situasi tertentu seperti optimasi performa, pemrograman perangkat keras, dan pengkodean algoritma tertentu.
    &=	            x &= 3	            x = x & 3       nilai variabel x akan di-'AND'-kan bit per bit dengan 3.
    |=	            x |= 3	            x = x | 3       nilai variabel x akan di-'OR'-kan bit per bit dengan 3.
    ^=	            x ^= 3	            x = x ^ 3       nilai variabel x akan di-'XOR'-kan bit per bit dengan 3.
    >>=	            x >>= 3	            x = x >> 3      nilai variabel x akan digeser ke kanan sebanyak 3 bit.
    <<=	            x <<= 3	            x = x << 3      nilai variabel x akan digeser ke kiri sebanyak 3 bit.

3.  Comparison operators => digunakan untuk membandingkan dua nilai
    Operator	    Name	                    Example
    ==	            Equal	                    x == y
    !=	            Not equal	                x != y
    >	            Greater than	            x > y
    <	            Less than	                x < y
    >=	            Greater than or equal to	x >= y
    <=	            Less than or equal to	    x <= y

4.  Logical operators => digunakan untuk menggabungkan pernyataan kondisional
    Operator	    Description	                                                Example	Try it
    and 	        Returns True if both statements are true	                x < 5 and  x < 10
    or	            Returns True if one of the statements is true	            x < 5 or x < 4
    not	            Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

5.  Identity operators => digunakan untuk membandingkan objek
    Operator	    Description	                                                Example
    is 	            Returns True if both variables are the same object	        x is y
    is not	        Returns True if both variables are not the same object	    x is not y

6.  Membership operators => digunakan untuk menguji apakah suatu urutan disajikan dalam suatu objek
    Operator	    Description	                                                                        Example
    in 	            Returns True if a sequence with the specified value is present in the object	    x in y
    not in	        Returns True if a sequence with the specified value is not present in the object	x not in y

7.  Bitwise operators => digunakan untuk membandingkan angka (biner)
    Operator	    Name	                Description	                                                                                                    Example
    & 	            AND	                    Sets each bit to 1 if both bits are 1	                                                                        x & y
    |	            OR	                    Sets each bit to 1 if one of two bits is 1	                                                                    x | y
    ^	            XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                                x ^ y
    ~	            NOT	                    Inverts all the bits	                                                                                        ~x
    <<	            Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                            x << 2
    >>	            Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	        x >> 2

8. Operator Precedence => menjelaskan urutan operasi yang dilakukan.
    Berikut Urutan Prioritas:
    Operator	                                    Description
    ()	                                            Parentheses
    **	                                            Exponentiation
    +x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT
    *  /  //  %	                                    Multiplication, division, floor division, and modulus
    +  -	                                        Addition and subtraction
    <<  >>	                                        Bitwise left and right shifts
    &	                                            Bitwise AND
    ^	                                            Bitwise XOR
    |	                                            Bitwise OR
    ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
    not	                                            Logical NOT
    and	                                            AND
    or	                                            OR
"""

## Contoh Identity Operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


## Contoh Membership Operator
x = ["apple", "banana"]

print("apple" in x)
# returns True because a sequence with the value "banana" is in the list


## Contoh Bitwise Operator
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)


## Contoh Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

"""
Penjelasan Operator Bitwise
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

a. And bitwise
    6 = 0000000000000110
    3 = 0000000000000011
    --------------------
    2 = 0000000000000010
    ====================

b. Or bitwise
    6 = 0000000000000110
    3 = 0000000000000011
    --------------------
    7 = 0000000000000111
    ====================

c. XOR bitwise
    6 = 0000000000000110
    3 = 0000000000000011
    --------------------
    5 = 0000000000000101
    ====================

d. Not Bitwise
    Inverted 3 becomes -4:
     3 = 0000000000000011
    -4 = 1111111111111100

e. Push 00 in from the left
    3 = 0000000000000011
    becomes
    12 = 0000000000001100
    
f.  move each bit 2 times to the right
    8 = 0000000000001000
    becomes
    2 = 0000000000000010

Decimal numbers and their binary values:
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
8 = 0000000000001000
9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""