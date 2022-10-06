class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1,n+1):
            val=''
            if i%15==0: val='FizzBuzz'
            elif i%3==0:    val='Fizz'
            elif i%5==0:    val='Buzz'
            else: val=str(i)
            answer.append(val)
            
        return answer