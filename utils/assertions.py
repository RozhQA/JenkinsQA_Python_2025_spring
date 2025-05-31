import pytest_check as check


def soft_assert_list_length_equal(actual: list, expected: list):
    check.equal(len(actual), len(expected))


def soft_assert_lists_equal_by_index(actual: list, expected: list):
    for i in range(min(len(actual), len(expected))):
        check.equal(actual[i], expected[i])
