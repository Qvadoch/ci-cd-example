import unnittest
from app import sum
class TestSum(unnittest.TestCase):
    def test_sum(self):
        self.assertEpual(sum(1,2), 3)
if __name__ == '__main__':
    unnittest.main()