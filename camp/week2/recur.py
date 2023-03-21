import colorama
from colorama import Fore


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n == 1):
            return True
        elif (n < 1):
            return False
        else:
            return self.isPowerOfFour(n/4)

def a2svAssumption(b):
    if b:
        print(Fore.GREEN + "Test Success")
    else:
        print(Fore.RED + "Test Failed")

        # raise Exception("TEST FAILED")

        
# assert Solution().isPowerOfFour(16) == False
a2svAssumption(Solution().isPowerOfFour(12) == False)
a2svAssumption(Solution().isPowerOfFour(0) == False)
a2svAssumption(Solution().isPowerOfFour(1) == True)
a2svAssumption(Solution().isPowerOfFour(12) == False)