import unittest
from battery import Battery
import typewise_alert
import test_data
from unittest.mock import patch
from io import StringIO
import constants as const

STD_OUT = 'sys.stdout'

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    for test in test_data.INFER_BREACH_INPUT_OUTPUT:
      self.assertTrue(typewise_alert.infer_breach(
          test.get(const.VALUE), 
          test.get(const.LOWER_LIMIT), 
          test.get(const.UPPER_LIMIT)) == test.get(const.RESULT))
          
  def test_classification_temperature_breach(self):
    for test in test_data.CLASSIFICATION_INPUT_OUTPUT:
      self.assertTrue(typewise_alert.classify_temperature_breach(
        test.get(const.COOLING_TYPE), 
        test.get(const.VALUE)) == test.get(const.RESULT))

  def test_set_cooling_limits(self):
    for test in test_data.COOLING_LIMIT_INPUT_OUTPUT:
      self.assertTrue(typewise_alert.set_cooling_limits(
        test.get(const.COOLING_TYPE)) == test.get(const.RESULT))

  def test_check_and_alert(self):
    for test in test_data.CHECK_ALERT_INPUT_OUTPUT:
      battery = Battery()
      battery.set_cooling_type(test.get(const.COOLING_TYPE))
      with patch(STD_OUT, new = StringIO()) as fake_out:
        typewise_alert.check_and_alert_breach(
          test.get(const.ALERT_TARGET), 
          battery.to_dictionary(), 
          test.get(const.VALUE))
        self.assertEqual(fake_out.getvalue(), test.get(const.RESULT))
  
  def test_alert(self):
    for test in test_data.ALERT_INPUT_OUTPUT:
      with patch(STD_OUT, new = StringIO()) as fake_out:
        typewise_alert.alert(
          test.get(const.ALERT_TARGET),
          test.get(const.BREACH_TYPE))
        self.assertEqual(fake_out.getvalue(), test.get(const.RESULT))


if __name__ == '__main__':
  unittest.main()
