import unittest
import resolve


class TestResolve(unittest.TestCase):
    def test_github_url(self):
        url = "https://github.com/aptos-labs/aptos-core"
        self.assertEqual(resolve.Resolve(url).get_api_url(), ('github', "https://api.github.com/repos/aptos-labs"
                                                                        "/aptos-core"))


if __name__ == '__main__':
    unittest.main()
