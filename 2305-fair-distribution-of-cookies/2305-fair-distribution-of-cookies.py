class Solution:

    def distribute(self, cookies, k, buckets, i=0):

        if i == len(cookies):
             return max(buckets)

        answer = float('inf')
        for j in range(k):
            buckets[j]+=cookies[i]
            if buckets[j] < answer:
                answer = min(answer, self.distribute(cookies, k, buckets, i+1))
            buckets[j]-=cookies[i]

        return answer


    def distributeCookies(self, cookies: List[int], k: int, splits=[]) -> int:
        return self.distribute(cookies, k, [0]*k)
