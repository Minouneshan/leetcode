from median_of_two_sorted_arrays import median_of_two_sorted_arrays

def test_findMedianSortedArrays():
   nums1 = [1 ,2]
   nums2 = [3,4]
   expected = 2.5

   actual = median_of_two_sorted_arrays.run(nums1,nums2)

   assert(expected == actual)