from appy.pod.renderer import Renderer
import os.path

INDIR = "tests/input"
OUTDIR = "tests/output"
INFILE = os.path.join(INDIR, "simple.odt")
RESULT = os.path.join(OUTDIR, "result.odt")


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
