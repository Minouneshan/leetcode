
from container_with_most_water import container_with_most_water

def test_maxArea():
   heights = [2, 7, 11, 15]
   expected = 14


   actual = container_with_most_water.run(heights)

   assert(expected == actual)

