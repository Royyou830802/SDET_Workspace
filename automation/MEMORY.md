# Automation Framework - Memory Bank

## Goal

Build an automation framework targeting Embedded Linux devices (modeled after the Roku TV SDET role) as a portfolio project.
All tests use mock / fixtures — no real device required.

---

## Completed

### `framework/utils/subprocess_helper.py`
- `CommandResult` class: wraps `returncode`, `stdout`, `stderr`, exposes `success` property
- `run_command(cmd: list[str], timeout: int = 30) -> CommandResult`: wraps `subprocess.run()`

### `system_tests/test_smoke.py`
- `TestDependency`: uses `parametrize` to verify local tools are available (python / git / pytest)
- All tests passing

---

## Next Steps (in order)

### Step 1 — `framework/fixtures/`
Create sample log files:
- `app.log` — structured app log (`[timestamp] [LEVEL] [Component] message`)
- `dmesg.log` — kernel / boot log (`[timestamp] message`, contains ERROR / WARNING)

### Step 2 — `framework/parsers/app_log_parser.py`
Parse `app.log`:
- `LogEntry` class: `timestamp`, `level`, `component`, `message`
- `AppLogParser(raw_log: str)`:
  - `parse() -> list[LogEntry]`
  - `get_errors() -> list[LogEntry]`
  - `get_warnings() -> list[LogEntry]`
  - `get_by_component(component: str) -> list[LogEntry]`

### Step 3 — `framework/collectors/mock_collector.py`
Read fixture files to simulate log collection from a device:
- `MockCollector(fixture_path: Path)`
- `get_app_log() -> str`
- `get_dmesg() -> str`

### Step 4 — `system_tests/test_log_parser.py`
Validate parser logic with pytest:
- Verify error count is correct
- Verify component filtering works
- Verify clean log returns empty list

### Step 5 — `framework/parsers/dmesg_parser.py`
Parse `dmesg.log` (similar to app_log_parser, different format)

---

## Log Format Reference

### app.log
```
2026-03-05 10:00:01 [INFO]  [VideoPlayer] Playback started: resolution=4K fps=60
2026-03-05 10:00:05 [ERROR] [AudioService] HDMI ARC handshake timeout after 3000ms
2026-03-05 10:00:06 [WARN]  [NetworkManager] Signal strength low: rssi=-85dBm
```

### dmesg.log
```
[    0.000000] Booting Linux on physical CPU 0x0
[    0.512345] hdmi: HDMI cable connected
[    2.345678] ERROR: wifi: failed to load firmware wlan.bin
[    3.456789] WARNING: audio: underrun detected on HDMI output
```

---

## Current Structure

```
automation/
  framework/
    utils/
      subprocess_helper.py    ✅ done
    parsers/                  ⬜ pending
    collectors/               ⬜ pending
    fixtures/                 ⬜ pending
  system_tests/
    test_smoke.py             ✅ done
    test_log_parser.py        ⬜ pending
```