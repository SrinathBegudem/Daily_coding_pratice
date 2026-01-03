# google question 1
Yeah, this is a very common “logs lookup / time to value” style question.

From your notes, the rule sounds like this:

You have updates like 50 -> priceA, 100 -> priceB

For a query time t, return the price from the latest update strictly before t.

So t = 60 returns priceA (from 50)

t = 100 still returns priceA (because update at 100 starts from 101)

t = 101 returns priceB (from 100)

So the operation is basically: predecessor lookup using “< t” (strictly less).

Clean problem statement (what Google usually asks)

“Given a list of (time, price) updates and a list of query times, return the price active at each query time. A price update recorded at time x becomes active starting at time x+1 (so at time x itself, the old price still applies).”

from typing import Dict, List, Any, Optional

def answer_queries_bruteforce_max(update_map: Dict[int, Any],
                                  queries: List[int],
                                  default: Optional[Any] = None) -> List[Any]:
    update_times = list(update_map.keys())
    out = []

    for t in queries:
        best_time = -1  # means "no valid update found yet"
        for tm in update_times:
            if tm < t:                       # STRICT: only earlier updates
                best_time = max(best_time, tm)

        out.append(default if best_time == -1 else update_map[best_time])

    return out

sol 2
from typing import Dict, List, Any, Optional

def answer_queries_binary_search(update_map: Dict[int, Any],
                                 queries: List[int],
                                 default: Optional[Any] = None) -> List[Any]:
    times = sorted(update_map.keys())  # sort once

    def predecessor_index_strict(t: int) -> int:
        # rightmost index i with times[i] < t, or -1 if none
        left, right = 0, len(times) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if times[mid] < t:          # STRICT
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    out = []
    for t in queries:
        idx = predecessor_index_strict(t)
        out.append(default if idx == -1 else update_map[times[idx]])

    return out


