### Advanced Encryption Standard (AES)
AES or Advanced Encryption Standards (also known as Rijndael) is one of the most widely used methods for encrypting and decrypting sensitive information in 2017.
This encryption method uses what is known as a block cipher algorithm to ensure that data can be stored securely.

The features of AES are as follows:
* Symmetric key symmetric block cipher
* 128-bit data, 128/192/256-bit keys
* Stronger and faster than Triple-DES
* Provide full specification and design details
* Software implementable in C and Java

#### Encryption Process:
![alt text](https://www.tutorialspoint.com/cryptography/images/first_round_process.jpg)

#### ShiftRows: 
Each of the four rows of the matrix is shifted to the left. Any entries that ‘fall off’ are re-inserted on the right side of row. Shift is carried out as follows:
* First row is not shifted.
* Second row is shifted one (byte) position to the left.
* Third row is shifted two positions to the left.
* Fourth row is shifted three positions to the left.
* The result is a new matrix consisting of the same 16 bytes but shifted with respect to each other.

#### MixColumns:
* each column is processed separately
* each byte is replaced by a value dependent on all 4 bytes in the column
* effectively a matrix multiplication in GF(2^8) using prime poly m(x) =x^8+x^4+x^3+x+1
![alt text](https://lh6.googleusercontent.com/proxy/f_AI0fFJW5-318ylwKmCG0UeFkmbw615-H8UWE-P_hTMmZp709bHrmSJDnncATZCVQihCACgF02i7msXM5HFumowS5dPFTbQCD2qHHdz6JWn9rVqGBQw3duYMuVgZKKBshal3xvKVhe8u4mf9jKX-EqMNEnWbbUoE__7RQ=w1200-h630-p-k-no-nu)


