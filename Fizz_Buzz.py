class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dict = {}
        for i in range(1,n+1):
            dict[i] = i
        I = n/3
        K = n/5
        listI = []
        listK = []
        for i in range(1,I+1):
            if 3*i <= n:
                listI.append(i*3)
        for i in range(1,K+1):
            if 5*i <= n:
                listK.append(i*5)
        for i in listI:
            dict[i] ="Fizz"

        for i in listK:
            if dict[i]=="Fizz":
                dict[i]="FizzBuzz"
            else:
                dict[i] ="Buzz"
        listr = []
        for v in dict.values():
            listr.append(str(v))
        return listr
t = Solution()
n = 15
print t.fizzBuzz(n)