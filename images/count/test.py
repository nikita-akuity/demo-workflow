import unittest
import os
from count import main as prog

class TestCount(unittest.TestCase):

    FILES = [
        """
hello A hello B
hello C
goodbye C
GoOdByE W
        """,
        """
🐞
goodbye 👽
        """,
        ""
    ]
    def setUp(self):
        for i, txt in enumerate(self.FILES, start=1):
            with open(f'/tmp/{i}.txt','w') as f:
                f.write(txt)
    
    def test_hello(self):
        self.assertEqual(prog("--input-file /tmp/1.txt --string hello".split()), 3)
        self.assertEqual(prog("--input-file /tmp/1.txt".split()), 3)

    def test_goodbye(self):
        self.assertEqual(prog("--input-file /tmp/1.txt --string goodbye".split()), 1)
        self.assertEqual(prog("--input-file /tmp/2.txt --string goodbye".split()), 1)

    def test_nonexistent(self):
        self.assertEqual(prog("--input-file /tmp/1.txt --string cowPower".split()), 0)
        self.assertEqual(prog("--input-file /tmp/2.txt".split()), 0)
        self.assertEqual(prog("--input-file /tmp/3.txt --string ''".split()), 0)

    def tearDown(self):
        for i in range(1,len(self.FILES)+1):
            os.remove(f'/tmp/{i}.txt')

if __name__ == "__main__":
    unittest.main()
