from automation.framework.utils.subprocess_helper import run_command
import pytest

class TestDependency:
    @pytest.mark.parametrize("cmd", [
        (["python", "--version"]),
        (["git", "--version"]),
        (["pytest", "--version"]),
    ], ids = [
        "Test if python exist.",
        "Test if git exist.",
        "Test if pytest exist."
    ])
    def test_dependency(self, cmd: list[str]):
        result = run_command(cmd)
        print(result.stdout)
        assert result.returncode == 0, f"Failed: {result.stderr}"
