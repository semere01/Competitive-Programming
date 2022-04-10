class Solution:
  def fizzBuzz(self, n: int) -> list[str]:
    answer = []
    d = {15: 'FizzBuzz', 3: 'Fizz', 5: 'Buzz'};
    for i in range(1, n+1):
        added = False;
        for nums in d.keys():
            if not (i % nums):
                answer.append(d[nums])
                added = True
        if not added:
            answer.append(i)
    return answer;
s = Solution()
print(s.fizzBuzz(20))