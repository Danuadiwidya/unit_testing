from unitsistem import thisKalkulator

import unittest

class testOperasi(unittest.TestCase):
    def __init__(self, methodName: str = "MenjalankanTest") -> None:
        super().__init__(methodName)
        self.operasi = thisKalkulator(19,22)

    def test_penjumlahan(self):
        hasil = self.operasi.penjumlahan()
        self.assertEqual(hasil, 19+22)

    def test_pengurangan(self):
        hasil = self.operasi.pengurangan()
        self.assertEqual(hasil, 19-22)

    def test_perkalian(self):
        hasil = self.operasi.perkalian()
        self.assertEqual(hasil, 19*22)

    def test_pembagian(self):
        hasil = self.operasi.pembagian()
        self.assertEqual(hasil, 19/22)

    def test_pembagian_by_zero(self):
        # Uji kasus ketika b adalah nol
        with self.assertRaises(ValueError):
            hasil = thisKalkulator(19,0)
            hasil.pembagian()

if __name__ == '__main__':
    unittest.main()
