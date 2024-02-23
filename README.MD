# Edona
Encrypt and Decrypt data and passwords using a secret key.


## Encoding process
take input string from user
</br>
encode the input string to base64
</br>
take a pin from the user
</br>
split the base64 string in the length number of pin. ex: if user input 32 then its length is 2 therefore base64 string is split into two parts.
</br>
replace the character with its pin digit from letters. ex: as  3 is first character of 32, therefore each character of the first part of string is excedded by that value. ('a' becomes 'd').


## decoding process
split the encoded string into two parts.
</br>
restore the character throuch pin value.
</br>
