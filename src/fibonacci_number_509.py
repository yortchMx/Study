#!/usr/bin/env python3

class Solution:
    def fib(self, n: int) -> int:

        def fib_h(n, memory):

          if len(memory) < n:
            memory.append(memory[-1] + memory[-2])
            return fib_h(n, memory)
          else:
            return memory[-1] + memory[-2]

        if n<=1:
          return n
        else:
          return fib_h(n, [0,1])
