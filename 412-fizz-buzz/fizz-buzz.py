class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
      
        # answer[i] == "FizzBuzz" wouldnt work becasue the index is out of bound... when start with answer[i] there is no ith index to be assigned new value


        for i in range(1,n+1): 
            if i%3==0 and i%5 ==0: 
                answer.append("FizzBuzz")
            elif i%3==0: 
                answer.append("Fizz")
            elif i%5 ==0:
                answer.append("Buzz")
            else :
                
                answer.append(str(i)) # i is integer
        
        return answer
        