import unittest
from battery import Battery
import typewise_alert
import constants as const
from unittest.mock import patch
from io import StringIO

STD_OUT = 'sys.stdout'

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == const.TOO_LOW)
    self.assertTrue(typewise_alert.infer_breach(70, 50, 100) == const.NORMAL)
    self.assertTrue(typewise_alert.infer_breach(110, 50, 100) == const.TOO_HIGH)

  def test_classification_temperature_breach(self):
    self.assertTrue(typewise_alert.classify_temperature_breach(const.HI_ACTIVE_COOLING, -20) == const.TOO_LOW)
    self.assertTrue(typewise_alert.classify_temperature_breach(const.MED_ACTIVE_COOLING, 20) == const.NORMAL)
    self.assertTrue(typewise_alert.classify_temperature_breach(const.PASSIVE_COOLING, 40) == const.TOO_HIGH)

  def test_set_cooling_limits(self):
    self.assertTrue(typewise_alert.set_cooling_limits(const.PASSIVE_COOLING) == (35, 0))
    self.assertTrue(typewise_alert.set_cooling_limits(const.MED_ACTIVE_COOLING) == (40, 0))
    self.assertTrue(typewise_alert.set_cooling_limits(const.HI_ACTIVE_COOLING) == (45, 0))

  def test_set_cooling_limits(self):
    self.assertTrue(typewise_alert.set_cooling_limits(const.PASSIVE_COOLING) == (35, 0))
    self.assertTrue(typewise_alert.set_cooling_limits(const.MED_ACTIVE_COOLING) == (40, 0))
    self.assertTrue(typewise_alert.set_cooling_limits(const.HI_ACTIVE_COOLING) == (45, 0))

  def test_alert(self):
    battery = Battery()
    battery.set_cooling_type(const.HI_ACTIVE_COOLING)
    with patch(STD_OUT, new = StringIO()) as fake_out:
      typewise_alert.check_and_alert_breach(const.EMAIL_ALERT, battery.to_dictionary(), 30)
      self.assertEqual(fake_out.getvalue(), "No Breach\n")
    output = "{}\n{}\n".format(f'To: {const.RECEPIENT}', 'Hi, the temperature is too high')
    with patch(STD_OUT, new = StringIO()) as fake_out:
      typewise_alert.check_and_alert_breach(const.EMAIL_ALERT, battery.to_dictionary(), 70)
      self.assertEqual(fake_out.getvalue(), output)

    output = '65261, TOO_HIGH\n'
    with patch(STD_OUT, new = StringIO()) as fake_out:
      typewise_alert.check_and_alert_breach(const.CONTROLLER_ALERT, battery.to_dictionary(), 70)
      self.assertEqual(fake_out.getvalue(), output)
    

if __name__ == '__main__':
  unittest.main()
