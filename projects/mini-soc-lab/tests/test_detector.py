import unittest
from datetime import datetime

from detector import Event, detect


class DetectorTests(unittest.TestCase):
    def test_brute_force_detection(self) -> None:
        events = [
            Event(datetime(2026, 9, 8, 14, 0, i), "192.0.2.50", "admin", "FAILURE")
            for i in range(1, 6)
        ]
        alerts = detect(events)
        self.assertTrue(any(alert.rule == "AUTH-001" for alert in alerts))

    def test_success_after_failures(self) -> None:
        events = [
            Event(datetime(2026, 9, 8, 14, 0, i), "192.0.2.50", "user", "FAILURE")
            for i in range(1, 4)
        ]
        events.append(Event(datetime(2026, 9, 8, 14, 0, 10), "192.0.2.50", "user", "SUCCESS"))
        alerts = detect(events)
        self.assertTrue(any(alert.rule == "AUTH-002" for alert in alerts))

    def test_admin_targeting(self) -> None:
        events = [
            Event(datetime(2026, 9, 8, 14, 0, 1), "192.0.2.50", "admin", "FAILURE")
        ]
        alerts = detect(events)
        self.assertTrue(any(alert.rule == "AUTH-003" for alert in alerts))


if __name__ == "__main__":
    unittest.main()
