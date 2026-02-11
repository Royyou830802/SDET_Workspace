# Pytest Cheatsheet

## Basics
- `pytest -q` for quiet output.
- `pytest -k <expr>` to filter tests.
- `pytest -x` stop at first failure.

## Assertions
- Use plain `assert`.
- `pytest.raises(ExpectedError)` for exceptions.

## Fixtures
- `@pytest.fixture` for setup/teardown.
- `scope` options: function, class, module, session.

## Parametrize
- `@pytest.mark.parametrize("a,b,expected", [...])`
- Good for table-driven tests.

## Marks
- `@pytest.mark.skip(reason="...")`
- `@pytest.mark.xfail(reason="...")`

## Monkeypatch
- `monkeypatch.setenv`, `monkeypatch.setattr`.

## Temp Paths
- Use `tmp_path` fixture.

## Mock
- `from unittest.mock import Mock, patch`
- Patch where used, not where defined.
