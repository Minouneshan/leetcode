from reverse_integer import reverse_integer

def test_reverse_integer():
    nums = 123
    target = 321


    actual = reverse_integer.run(nums)

    assert(target == actual)
    return(actual)