# KALKULATOR SEDERHANA

print('-'*50)
print('Silahkan input angka terlebih dahulu')
a1 = int(input('Masukkan angka pertama: '))
a2 = int(input('Masukkan angka kedua: '))

print('-'*50)
print('''Silahkan pilih opsi operasi kalkulator :
+ (Penjumlahan)
- (Pengurangan)
x (Perkalian)
/ (Pembagian)
^ (Pemangkatan)''')
print('-'*50)

opsi = input('Masukkan opsi: ')

if opsi == '+':
    hasil = a1 + a2
elif opsi == '-':
    hasil = a1 - a2
elif opsi == 'x':
    hasil = a1 * a2
elif opsi == '/':
    hasil = a1 / a2
elif opsi == '^':
    hasil = a1 ** a2
else:
    print('Opsi salah. Silahkan input ulang opsi')
    exit()

print('-'*50)
print(f'Hasil = {hasil}')