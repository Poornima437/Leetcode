class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid = []  
        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            a = isActive[i]
            if not a:
                continue
            if b not in order:
                continue
            if not c:
                continue
            ok = True
            for ch in c:
                if not (ch.isalnum() or ch == "_"):
                    ok = False
                    break
            if not ok:
                continue
            valid.append((order[b], c))
        valid.sort()
        return [c for _, c in valid]

         