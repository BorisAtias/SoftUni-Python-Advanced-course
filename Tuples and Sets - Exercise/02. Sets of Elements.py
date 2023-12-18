m_n = list(map(int, input().split()))
count = m_n[0] + m_n[1]
set_1 = set()
set_2 = set()

all_numbers = set()

for i in range(1, count + 1):
    nums = int(input())
    if i <= m_n[0]:
        set_1.add(nums)
    else:
        set_2.add(nums)

    all_numbers.add(nums)

for num in all_numbers:
    if num in set_1 and num in set_2:
        print(num)
