class Solution(object):
    def capitalizeTitle(self, title):
        s=title.title()
        # print(s)
        t=s.split(" ")
        # print(t) 
        for i in range(len(t)):
            if len(t[i])<=2:
                t[i]=t[i].lower()
        k=" ".join(t)
        return k
        