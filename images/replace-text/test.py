import unittest
import os
from rt import main as prog

class TestRt(unittest.TestCase):

    INPUTS = [
        """
hello A hello B
hello C
HeLlO W
        """,
        """
🐞
goodbye 👽
        """,
        ""
    ]
    OUTPUTS = [
        """
goodbye A goodbye B
goodbye C
HeLlO W
        """,
        """
🐞
replaced 👽
        """,
        ""
    ]
    def setUp(self):
        for i, txt in enumerate(self.INPUTS, start=1):
            with open(f'/tmp/in{i}.txt','w') as f:
                f.write(txt)
    
    def test_defaults(self):
        p = prog("--input-file /tmp/in1.txt --output-file /tmp/out1.txt".split())
        with open('/tmp/out1.txt') as f:
            self.assertEqual(f.read(), self.OUTPUTS[0])
        os.remove('/tmp/out1.txt')

    def test_custom(self):
        p = prog("--input-file /tmp/in2.txt --output-file /tmp/out2.txt --search goodbye --replace replaced".split())
        with open('/tmp/out2.txt') as f:
            self.assertEqual(f.read(), self.OUTPUTS[1])
        os.remove('/tmp/out2.txt')

    def test_empy(self):
        p = prog("--input-file /tmp/in3.txt --output-file /tmp/out3.txt".split())
        with open('/tmp/out3.txt') as f:
            self.assertEqual(f.read(), self.OUTPUTS[2])
        os.remove('/tmp/out3.txt')

    def test_delete(self):
        with open(f'/tmp/in0.txt','w') as f:
            f.write(self.INPUTS[0])
        p = prog("--input-file /tmp/in0.txt --output-file /tmp/out0.txt --delete".split())
        self.assertFalse(os.path.exists('/tmp/in0.txt'))
        os.remove('/tmp/out0.txt')

    def tearDown(self):
        for i in range(1,len(self.INPUTS)+1):
            os.remove(f'/tmp/in{i}.txt')

if __name__ == "__main__":
    unittest.main()
