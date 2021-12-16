import unittest
from unittest.mock import MagicMock, patch

import main


class ReportTestCase(unittest.TestCase):
    def test_report_data(self):
        accounts = [
            {"id": "1"},
            {"id": "2"},
        ]

        accounts_detail = [
            {"Id": "1", "Name": "One"},
            {"Id": "2", "Name": "Two"},
        ]

        revenue = [
            {"AccountId": "1", "Amount": 1},
            {"AccountId": "2", "Amount": 2},
        ]

        main.salesforce = MagicMock()
        with patch(
            "main.salesforce.bulk.Account.query", return_value=[accounts_detail]
        ):
            with patch("main.salesforce.query_all_iter", return_value=revenue):
                self.assertDictEqual(
                    main.get_report_data(accounts),
                    {
                        "1": {"Name": "One", "Revenue": 1},
                        "2": {"Name": "Two", "Revenue": 2},
                    },
                )


if __name__ == "__main__":
    unittest.main()
