import subprocess

class CommandResult:

    def __init__(self, returncode: int, stdout: str, stderr: str):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
    
    @property
    def success(self) -> bool:
        return self.returncode == 0
    
def run_command(cmd: list[str], timeout: int = 30) -> CommandResult:
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout)
    
    cmdResult = CommandResult(result.returncode, result.stdout, result.stderr)

    return cmdResult

    
    