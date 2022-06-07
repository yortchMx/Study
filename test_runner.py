#!/usr/bin/env python3


import unittest


def main():
    """
    Main
    """

    print("Running main function")

    test_directory = "test"

    # Use the unittets loader to discover all the test cases from
    # files that have the 'test' prefix
    test_loader = unittest.TestLoader()
    suite = test_loader.discover(test_directory)

    # Run th tests
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    main()
