from appy.pod.renderer import Renderer
import os.path

DIR = "tests/input"
INFILE = os.path.join(DIR, "simple.odt")
RESULT = os.path.join(DIR, "result.odt")


class TestsSimple:

    def setUp(self):
        pass

    def test_something(self):
        assert 1 + 1 == 2

    def tearDown(self):
        pass


class TestAppy:

    def test_appy(self):
        context = 'TestMessage'
        beingPaidForIt = True
        renderer = Renderer(
            INFILE, {"context": context, "beingPaidForIt": beingPaidForIt}, RESULT, overwriteExisting=True)
        renderer.run()
