import unittest
import GithubAPI

class TestGithubAPI(unittest.TestCase):
    def testUserID(self):
        self.assertEqual(GithubAPI.getGithubReposAndCommits(
            "388r3rh8"), "Invalid UserID response!")
            
    def testBadInput(self):
        self.assertEqual(GithubAPI.getGithubReposAndCommits(24334), "UserID must be a string!")

    def testValidOutput(self):
        self.assertEqual(GithubAPI.getGithubReposAndCommits(
            "ogfemi"), [('BarrelMania', 7), ('CS-546', 30), ('iterative-prisoners-dilemma1', 2), ('Landing', 4), ('Resume', 2), ('RUHackathon', 2), ('SBUHackathon', 30)])



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
