from two_sum import two_sum

def test_two_sum():
   nums = [2, 7, 11, 15]
   target = 9
   expected = [0, 1]

   actual = two_sum.run(nums, target)

   assert(expected == actual)
   print(actual)
