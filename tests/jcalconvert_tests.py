# tests/jcalconvert_tests.py

from typer.testing import CliRunner
from jcc import __app_name__, __version__, cli

runner = CliRunner()

def testVersion():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{_-__version__}" in result.stdout