penghasilan = int(input('Penghasilan perbulan: '));
pajak = int(0)
if penghasilan < 1000000:
    print('tidak kena pajak')
elif penghasilan < 2000000:
    pajak = int(penghasilan * 5 / 100)
    print('potongan pajak sebesar: ', pajak, '(5%)')
elif penghasilan < 5000000:
    pajak = int(penghasilan * 10 / 100)
    print('potongan pajak sebesar: ', pajak, '(10%)')
else:
    pajak = int(penghasilan * 20 / 100)
    print('potongan pajak sebesar: ', pajak, '(20%)')

print('Penghasilan Bersih: {}'.format(penghasilan - pajak))