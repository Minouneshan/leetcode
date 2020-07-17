from zigzag_conversion import zigzag_conversion

def test_convert():

   st = 'PAYPALISHIRING'
   numRows = 3
   expected = "PAHNAPLSIIGYIR"

   actual = zigzag_conversion.run(st, numRows)

   assert(expected == actual)
                 