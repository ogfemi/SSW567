import unittest
from unittest.mock import MagicMock, patch
import GithubAPI


class TestGithubAPI(unittest.TestCase):
    @patch('GithubAPI.requests')
    def testUserID(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {
            'Response': "Doesnt exist"
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(GithubAPI.getGithubReposAndCommits(
            "388r3rh8"), "Invalid UserID response!")

    @patch('GithubAPI.requests')
    def testBadInput(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {
            'Response': "Doesnt exist"
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(GithubAPI.getGithubReposAndCommits(
            24334), "UserID must be a string!")

    @patch('GithubAPI.requests',)
    def testValidOutput(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "BarrelMania", "commits": 7},
            {"name": "CS-546", "commits": 30},
            {"name": "iterative-prisoners-dilemma1", "commits": 2},
            {"name": "Landing", "commits": 4},
            {"name": "Resume", "commits": 2},
            {"name": "RUHackathon", "commits": 2},
            {"name": "SBUHackathon", "commits": 30}
        ]
        mock_requests.get.return_value = mock_response
        self.assertEqual(GithubAPI.getGithubReposAndCommits(
            "ogfemi"), [('BarrelMania', 7), ('CS-546', 30), ('iterative-prisoners-dilemma1', 2), ('Landing', 4), ('Resume', 2), ('RUHackathon', 2), ('SBUHackathon', 30)])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
