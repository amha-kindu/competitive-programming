class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        persons_vote = defaultdict(lambda: 0)
        self.times, self.leads = times, []
        current_lead = 0
        for i in range(len(persons)):
            persons_vote[persons[i]] += 1
            if persons_vote[persons[i]] >= persons_vote[current_lead]:
                current_lead = persons[i]
            self.leads.append(current_lead)


    def q(self, t: int) -> int:
        pos = bisect_right(self.times, t)
        return self.leads[pos-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)