# Info

- Solve each task in the given time
- Write your code in the corresponding files (`task1.py`, `task2.py` and
  `task3.py`)
- Check your results by running `python3 test.py`, the output should be
    ```
    .........
    ----------------------------------------------------------------------
    Ran 13 tests in 0.003s

    OK
    ```
    and nothing else.
- Commit your changes and push your work.

## `task1.py`

Write a function called `sum_of_even_nums` that

- takes a list of numbers as its parameters
- and returns the sum of even numbers in the list.

## `task2.py`

Write a function called `find_oldest_person` that

- takes a CSV filename as its parameter
- reads and processes the CSV file
- and returns the oldest person's name.

If there are multiple people with the same age in the file it doesn't matter
which one is returned by the function.

The CSV file is structured as follows

```
Joe,10
Mary,18
Max,28
```

Calling your function with the filename of such a file should result in `'Max'`
as he's the oldest.

## `task3.py`

Write a function called `is_leap_year` that

- takes a year as its parameter
- decides if that year is a leap year or not
- and returns `True` or `False` depending on the result.
