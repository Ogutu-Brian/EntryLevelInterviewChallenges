import unittest
from add_list_numbers import check_sum


class Test_add_numbers(unittest.TestCase):
  """
  Tests addition of numbers problem
  """

  def test_samole_truthy(self) -> None:
    """
    Tests for truthy occurrence
    """
    sample_list = [10, 15, 3, 7]
    k = 17
    result = check_sum(sample_list, 17)
    self.assertEqual(True, result)

  def test_empty_list(self) -> None:
    """
    Tests for an empty list
    """
    sample_list = []
    k = 17
    result = check_sum(sample_list, k)
    self.assertEqual(False, result)

  def test_falsy(self) -> None:
    """
    tests for falsy
    """
    sample_list = [10, 15, 3, 5]
    k = 17
    result = check_sum(sample_list, k)
    self.assertEqual(False, result)
