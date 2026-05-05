from serializer import serialize
import random

def simple(nums):
    return ",".join(str(n) for n in nums)

def test_case(name, nums):
    s1 = simple(nums)
    s2 = serialize(nums)
    ratio = len(s1) / len(s2)
    print(f"{name}:")
    print("  naive:", len(s1))
    print("  compact:", len(s2))
    print("  ratio:", round(ratio, 2))
    print("  compact string:", s2)
    print()

# Required tests

test_case("Short set", {1,3,5,7,9})

test_case("Random 50", set(random.sample(range(1,301), 50)))
test_case("Random 100", set(random.sample(range(1,301), 100)))
test_case("Random 500", set(random.sample(range(1,301), 300)))  # max unique

test_case("All 1-digit", set(range(1,10)))
test_case("All 2-digit", set(range(10,100)))
test_case("All 3-digit", set(range(100,301)))

# 3 copies of each number (900 total)
nums = []
for i in range(1,301):
    nums += [i,i,i]
test_case("900 numbers (3 copies each)", set(nums))
