# Caesar Cipher

## Description

The  _Caesar Cipher_ is one of the earliest and easiest methods of encryption technique. It is a type of substitution cipher in which each letter of a message is replaced by another one some fixed number of positions down the alphabet.

## Logic Example

Assume you want to encrypt the word _hello_.

In order to encrypt a given text, a _shift_ should be indicated. The shift represents the number of positions each letter of the text has to be moved down. Assume a _shift_ value of 3.

In a Caesar Cipher with a shift of 3, A becomes D, B becomes E, etc. At the end of the alphabet, X becomes A, Y becomes B, and Z becomes C.

![](https://www.boxentriq.com/img/caesar-cipher-img1.png)

The encryption logic for the word _hello_ works in the following way:
> h &#8594; k  
> e &#8594; j  
> l &#8594; o  
> l &#8594; o  
> o &#8594; r  

In the end, the encrypted version of the word _hello_ would be _kjoor_.

Any numbers or special symbols like space, *, etc. will not be encrypted.

## Code structure

**art.py** file contains the ASCII logo of the Caesar Cipher.

**main.py** file contains the code for the Caesar Cipher. The code allows to encode any plain text, as well as decode any encrypted text by providing the shift number.

! Please make sure to keep all files in one folder when running the code.
