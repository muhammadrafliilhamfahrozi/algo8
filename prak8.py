print('@@@@      @     @@@@ @     @')
print('@  @     @ @    @    @     ')
print('@ @     @   @   @@@@ @     @  ')
print('@  @   @ @@@ @  @    @     @   ')
print('@   @ @       @ @    @@@@@ @      ')
def karakter_ganjil(input_string):
    karakter = ''
    for i in range(len(input_string)):
        if i % 2 == 1:
            karakter += input_string[i]
    return karakter

input_user = input("Masukkan sebuah kata: ")
hasil = karakter_ganjil(input_user)
print("Karakter indeks ganjil:", hasil)
