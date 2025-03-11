class Solution(object):
    def minTimeToType(self, word):
        circle="abcdefghijklmnopqrstuvwxyz"
        index={circle[j]: j for j in range(26)}
        current=0
        time=0
        for i in word:
            target=index[i]
            mini_dis=min(abs(current-target),26-abs(current-target))
            time += mini_dis+1
            current=target
        return time