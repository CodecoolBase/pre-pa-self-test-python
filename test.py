import unittest
import tempfile
import os

import task1
import task2
import task3


class TestTask1(unittest.TestCase):

    def test_sum_of_even_nums_empty_list(self):
        self.assertEqual(task1.sum_of_even_nums([]), 0)

    def test_sum_of_even_nums_single_zero(self):
        self.assertEqual(task1.sum_of_even_nums([0]), 0)

    def test_sum_of_even_nums_single_odd_number(self):
        self.assertEqual(task1.sum_of_even_nums([41]), 0)

    def test_sum_of_even_nums_single_even_number(self):
        self.assertEqual(task1.sum_of_even_nums([42]), 42)

    def test_sum_of_even_nums_multiple_odd_number(self):
        self.assertEqual(task1.sum_of_even_nums([-7, 1, 41]), 0)

    def test_sum_of_even_nums_multiple_even_number(self):
        self.assertEqual(task1.sum_of_even_nums([-8, 2, 42]), 36)

    def test_sum_of_even_nums_multiple_mixed_numbers(self):
        self.assertEqual(task1.sum_of_even_nums(
            [-7, -2, 0, 1, 2, 8, 7, 41, 42]), 50)


class TestTask2(unittest.TestCase):

    def assert_find_oldest_person(self, given_text, expected_persons):
        # On Windows files that are already open for writing
        # cannot be opened for reading again, thus we need to
        # close the tempfile manually, then remove it after
        # the call.
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(given_text)
            f.close()
            try:
                res = task2.find_oldest_person(os.path.realpath(f.name))
                self.assertIn(res, expected_persons)
            finally:
                os.remove(f.name)

    def test_find_oldest_person_empty(self):
        self.assert_find_oldest_person(b'', [None])

    def test_find_oldest_person_single_line(self):
        self.assert_find_oldest_person(b'Max,33', ['Max'])

    def test_find_oldest_person_multiple_lines_different_age(self):
        self.assert_find_oldest_person(b'''Max,33
Mary,18
Joe,42'''.strip(), ['Joe'])

    def test_find_oldest_person_multiple_lines_same_age(self):
        self.assert_find_oldest_person(b'''Peter,33
Mary,18
Jane,12
Jack,33'''.strip(), ['Peter', 'Jack'])


class TestTask3(unittest.TestCase):

    LEAP_YEARS = [
        1804,
        1808,
        1812,
        1816,
        1820,
        1824,
        1828,
        1832,
        1836,
        1840,
        1844,
        1848,
        1852,
        1856,
        1860,
        1864,
        1868,
        1872,
        1876,
        1880,
        1884,
        1888,
        1892,
        1896,
        1904,
        1908,
        1912,
        1916,
        1920,
        1924,
        1928,
        1932,
        1936,
        1940,
        1944,
        1948,
        1952,
        1956,
        1960,
        1964,
        1968,
        1972,
        1976,
        1980,
        1984,
        1988,
        1992,
        1996,
        2000,
        2004,
        2008,
        2012,
        2016,
        2020,
        2024,
        2028,
        2032,
        2036,
        2040,
        2044,
        2048,
        2052,
        2056,
        2060,
        2064,
        2068,
        2072,
        2076,
        2080,
        2084,
        2088,
        2092,
        2096,
        2104,
        2108,
        2112,
        2116,
        2120,
        2124,
        2128,
        2132,
        2136,
        2140,
        2144,
        2148,
        2152,
        2156,
        2160,
        2164,
        2168,
        2172,
        2176,
        2180,
        2184,
        2188,
        2192,
        2196,
        2204,
        2208,
        2212,
        2216,
        2220,
        2224,
        2228,
        2232,
        2236,
        2240,
        2244,
        2248,
        2252,
        2256,
        2260,
        2264,
        2268,
        2272,
        2276,
        2280,
        2284,
        2288,
        2292,
        2296,
        2304,
        2308,
        2312,
        2316,
        2320,
        2324,
        2328,
        2332,
        2336,
        2340,
        2344,
        2348,
        2352,
        2356,
        2360,
        2364,
        2368,
        2372,
        2376,
        2380,
        2384,
        2388,
        2392,
        2396,
        2400,
    ]

    def test_leap_years(self):
        for leap_year in self.LEAP_YEARS:
            self.assertTrue(task3.is_leap_year(leap_year))

    def test_non_leap_years(self):
        first_leap_year = min(self.LEAP_YEARS)
        last_leap_year = max(self.LEAP_YEARS)
        non_leap_years = []
        for year in range(first_leap_year, last_leap_year):
            if year not in self.LEAP_YEARS:
                non_leap_years.append(year)
        for non_leap_year in non_leap_years:
            self.assertFalse(task3.is_leap_year(non_leap_year))


if __name__ == '__main__':
    unittest.main()
