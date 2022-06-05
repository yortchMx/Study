# Study

Repo made to study leetcode problems.
I'll use python3 for now at least.
I'll create a requirements.txt file to try to follow good practices.
I'll use flake8 to practice PEP8 standards when feasible

CODE HIERARCHY:
=========================================
Each leetcode problem solution is located in its own file.
The files are named in such a way you can find the problem name and number in
the file name.
Each solution has it's own unittest file, this file has the same name
convention, but has the 'test' prefix

How to run tests:
python3 -m unittest test_<problem_name_#>

Example:
python3 -m unittest test_binary_search_704.py
