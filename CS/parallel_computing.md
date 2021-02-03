# Parallel Computing (multiprocessing vs multithreading)

## Process
instance of a computer program being executed.
- each process has own memory space
- chrome and firefox use multiprocessing
- easier to implement
- overhead : memory and time

## Thread
components of a process
- can run parallely
- share memory space -> sharing object is easier
- lower overhead
- spawning is faster
- overhead : have to think more about design -> for synchronization

## Pitfalls
- race condition
  - when 2 threads try to change 1 var -> use mutual exclusion(mutex) lock -> only 1 thread can change var at a time
- starvation
  - when 1 thread has no work due to poor design-> slower overall
- deadlock
  - when 1 thread is waiting for deadlock -> other thread needs resource from first thread -> both halt
- livelock
  - keep running in loop

## Python
> GIL(Global Interpreter Lock) <br>
: a mutex that prevents multiple threads from executing python at once.
-> multiple CPU core can't be used

<br>

## Usage
### multithreading
> IO, user interaction
- web-scraping
- web servers
- tensorflow -> transform data in parallel

### multiprocessing
> anything CPU intensive, computation, no IO or user interaction
- pytorch -> load data to GPU

[reference](https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/)

<br>

## Example
> crawling Baekjoon problem tier information from solved.ac

### No multi-threading
10 crawls -> 3.2s <br>
50 crawls -> 19.9s
```python
import datetime
import requests
from bs4 import BeautifulSoup

class Solved():
    URL = 'https://solved.ac/search?query='
    selector = '#__next > div.contents > div:nth-child(3) > div:nth-child(2) > div > div.StickyTable__Wrapper-akg1ak-3.tcQcH.sticky-table > div > div:nth-child(2)'
    baek_URL = 'https://www.acmicpc.net/problem/'
    
    def __init__(self, prob_num):
        self.prob_num = str(prob_num)
    
    def get_tier(self):
        self.URL += self.prob_num
        self.baek_URL += self.prob_num
        res = requests.get(self.URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        soup = soup.select_one(self.selector)
        soup_a = soup.find('a', {'href':self.baek_URL})
        tier_info = soup_a.img
        return tier_info

prob_nums = list(map(int, "1000 1008 1012 1021 1107 1149 1158 1182 1212 1248 1260 1309 1330 1373 1406 1463 1476 1620 1662 1676 1697 1699 1707 1712 1748 1759 1764 1874 1912 1918 1926 1927 1929 1932 1934 1935 1978 2004 2089 2091 2133 2146 2156 2167 2178 2193 2206 2217 2225 2231 2293 2294 2309 2468 2504 2529 2557 2577 2583 2588 2606 2609 2644 2667 2739 2742 2743 2745 2753 2869 2884 2941 3078 3085 4179 4949 5014 5427 6064 6588 6593 6603 7562 7569 7576 7785 8393 9012 9093 9095 9205 9375 9465 9498 9613 10026 10162 10171 10172 10430 10718 10773 10799 10807 10808 10809 10817 10818 10819 10820 10824 10828 10844 10845 10866 10869 10872 10951 10952 10971 10972 10973 10974 11005 11047 11052 11053 11054 11055 11057 11279 11576 11653 11655 11656 11722 11723 11724 11726 11727 11729 12865 13398 14002 14391 14500 14501 14888 14889 15649 15650 15651 15652 15654 15655 15656 15657 15658 15661 15663 15664 15665 15666 15988 15990 16194 16208 16956 17087 17103 17298 17299 17404 17413".split()))
prob_tier_info_list = []
for prob_num in prob_nums[:10]:
    solved = Solved(prob_num)
    prob_tier_info_list.append(solved.get_tier().get('src'))
print(len(prob_tier_info_list))
```

### With multi-threading
10 crawls -> 0.861s <br>
50 crawls -> 2.4s

```python
import datetime
import requests
from bs4 import BeautifulSoup
import concurrent.futures

MAX_THREADS = 30

class Solved():
    URL = 'https://solved.ac/search?query='
    selector = '#__next > div.contents > div:nth-child(3) > div:nth-child(2) > div > div.StickyTable__Wrapper-akg1ak-3.tcQcH.sticky-table > div > div:nth-child(2)'
    baek_URL = 'https://www.acmicpc.net/problem/'
    
    def __init__(self, prob_nums):
        self.prob_nums = prob_nums
        self.tier_info = []
    
    def get_tier(self, prob_num):
        prob_URL = self.URL + prob_num
        baek_URL = self.baek_URL + prob_num
        res = requests.get(prob_URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        soup = soup.select_one(self.selector)
        soup_a = soup.find('a', {'href':baek_URL})
        tier_info = soup_a.img
        self.tier_info.append(tier_info)
    
    def multi_threading(self):
        threads = min(MAX_THREADS, len(self.prob_nums))
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            # this is where number of questions to crawl goes in
            executor.map(self.get_tier, self.prob_nums[:50])
    
    def get_result(self):
        return self.tier_info

prob_nums = list("1000 1008 1012 1021 1107 1149 1158 1182 1212 1248 1260 1309 1330 1373 1406 1463 1476 1620 1662 1676 1697 1699 1707 1712 1748 1759 1764 1874 1912 1918 1926 1927 1929 1932 1934 1935 1978 2004 2089 2091 2133 2146 2156 2167 2178 2193 2206 2217 2225 2231 2293 2294 2309 2468 2504 2529 2557 2577 2583 2588 2606 2609 2644 2667 2739 2742 2743 2745 2753 2869 2884 2941 3078 3085 4179 4949 5014 5427 6064 6588 6593 6603 7562 7569 7576 7785 8393 9012 9093 9095 9205 9375 9465 9498 9613 10026 10162 10171 10172 10430 10718 10773 10799 10807 10808 10809 10817 10818 10819 10820 10824 10828 10844 10845 10866 10869 10872 10951 10952 10971 10972 10973 10974 11005 11047 11052 11053 11054 11055 11057 11279 11576 11653 11655 11656 11722 11723 11724 11726 11727 11729 12865 13398 14002 14391 14500 14501 14888 14889 15649 15650 15651 15652 15654 15655 15656 15657 15658 15661 15663 15664 15665 15666 15988 15990 16194 16208 16956 17087 17103 17298 17299 17404 17413".split())
solved = Solved(prob_nums)
solved.multi_threading()
print(len(solved.get_result()))
```

### Results
> wow better results than expected.

|         |no threading   |threading   |
|---      |---|---|---|---|
|10 crawls|3.2s|0.86s|
|50 crawls|19.9s|2.4s|