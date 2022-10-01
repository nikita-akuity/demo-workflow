import unittest
import os
from greet import main as prog


class TestGreet(unittest.TestCase):

    OUTPUTS = ["""hello A
hello B
hello 👽
""","""greetings A
greetings B
greetings 👽
""","""hello 
hello B
"""]
    
    def test_default(self):
        p = prog("--name A --name B --name 👽 --output-file /tmp/1.txt".split())
        with open('/tmp/1.txt') as f:
            self.assertEqual(f.read(), self.OUTPUTS[0])
        os.remove('/tmp/1.txt')

    def test_custom(self):
        p = prog("--greeting greetings --name A --name B --name 👽 --output-file /tmp/2.txt".split())
        with open('/tmp/2.txt') as f:
            self.assertEqual(f.read(), self.OUTPUTS[1])
        os.remove('/tmp/2.txt')

    def test_empty(self):
        p = prog(['--name', '', '--name', 'B', '--output-file', '/tmp/3.txt'])
        with open('/tmp/3.txt') as f:
            self.assertEqual(f.read(), self.OUTPUTS[2])
        os.remove('/tmp/3.txt')


if __name__ == "__main__":
    unittest.main()
