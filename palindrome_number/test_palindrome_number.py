from palindrome_number import palindrome_number

def test_ispalindrome():
   num = 121
   expected = True
   actual = palindrome_number.run(num)

   assert(expected == actual)