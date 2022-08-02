#!/usr/bin/env python3

class Solution:
    def tribonacci(self, n: int) -> int:

        def tribo_help(n, memory):

          if n == len(memory):
            return memory[-1] + memory[-2] + memory[-3]
          else:
            memory.append(memory[-1] + memory[-2] + memory[-3])
            return tribo_help(n, memory)

        memory = [0,1,1]
        if n <= 2:
          return memory[n]
        else:
          return tribo_help(n, memory)
