from longest_substring_without_repeating_characters import longest_substring_without_repeating_characters

def test_lengthOfLongestSubstring():
   st = 'abcabcb'
   expected = 3


   actual = longest_substring_without_repeating_characters.run(st)

   assert(expected == actual)