import unittest

from app import create_app
from app.services.incident_manager import detect_incidents


class CloudGuardAPITests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_metrics_endpoint(self):
        response = self.client.get("/api/metrics")

        self.assertEqual(response.status_code, 200)
        self.assertIn("cpu_usage", response.json["data"])
        self.assertIn("memory_usage", response.json["data"])
        self.assertIn("incidents", response.json)

    def test_high_cpu_detection(self):
        metrics = {
            "cpu_usage": 95,
            "memory_usage": 30
        }

        incidents = detect_incidents(metrics)

        self.assertEqual(len(incidents), 1)
        self.assertEqual(
            incidents[0]["type"],
            "HIGH_CPU_USAGE"
        )

    def test_application_failure_detection(self):
        metrics = {
            "cpu_usage": 20,
            "memory_usage": 30
        }

        incidents = detect_incidents(metrics, "FAILED")

        self.assertEqual(len(incidents), 1)
        self.assertEqual(
            incidents[0]["severity"],
            "CRITICAL"
        )


if __name__ == "__main__":
    unittest.main()
