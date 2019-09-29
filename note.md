This is an attempt to re-familiarize myself with Python and learn something by the way.

### 1

A simple problem that can be solved with a simple for/while loop. Actuallly it can be calculated by hand with basic arithmatic knowledge, but that doesn't seem to be the oringinal intention.

### 2

Still solvable by hand considering that Fibonacci numbers are even for every 3 terms (odd, odd, even). Since Fibonacci numbers have a general formula, finding the sum is a trivial problem.

### 3

The idea is that we first find all prime numbers below the square root of n, and then try them one by one. If none of the numbers divides n, then n is itself a prime number. 

For finding prime numbers we can use Sieve of Eratosthenes, which is fast enough for most problems. Here I'm using a slightly optimized version, a better choice would be to check out [here](http://compoasso.free.fr/primelistweb/page/prime/eratosthene_en.php).

### 4

The first idea would be to just try out every multiple of 3-digit numbers. I haven't come up with a second idea yet, but the first is fast enough anyway.

### 5

My first idea was to find prime numbers below 20 and multiply them. After a second thought, it appears to be quite wrong.

A more careful approach is to first identify the prime composition of each number (for example, 20 = 2 x 2 x 5), which can be represented as an array of the count of prime factors. Then we max them elementwise, which forms the factors of our result. I did this in an iterative way.

## 6

Trivial at first sight, as so it is at second and every latter sight. It's just a one-liner.

---

Here magic occurred, and I jumped directly to problem #51 without explanation.

### 51

The idea would be to use hashmaps. With number that look like X555XXX, we would replace the 5s with As and use the result as a key, and insert the oringinal to the corresponding list. In this way, we can map numbers that belong to the same family to the same bucket, and after it is done, we iterate over the keys to find the family that satisfies the requirement.

Despite having given us properties of the prime, the question stopped there and told us nothing about the location of the prime family. So by my own judgement, looking between 1e5 and 1e7 would be a good starting point, for families that have 3 same digits.

There are some rather delicate points in my python code, and I've made use with some python's useful utilities. Anyway, the most significant part is managing the numbers as strings and use 'A' to replace the target positions.

### 52

The only problem is how to quickly determine if two numbers consist of the same digits. The best solution that I can think of is to use two arrays of size 10, each of which would store the count of occurrences of every digit in the number.

However, I used the other optimal approach (optimal in the sense that it requires few code), which is also clever. Just suit yourself.

### 53

Computing C(100,50) would be a bad idea since the number can be astrological. I'm not gonna try but I guess Python can't handle that.

The idea is that for every n, we would just compute C(n, i) with i starting from 0, and growing i until it exceeds one million. Suppose the value is now a, then every pair between (n, a) and (n, n - a) would satisfy the requirement. The implementation follows the idea.

### 54

This seems to be a rather engineering problem, so I guess notes aren't quite helpful.
