import shutil
import sys
from typing import Any, List, cast

from _pytest.config import Config
from _pytest.config.argparsing import Parser
from pytest import ExitCode, hookimpl

out_path = ".deeptest/junit.xml"


def is_enabled(config: Config) -> bool:
    return not cast(bool, config.option.no_cov) and bool(config.option.cov_source)


@hookimpl(hookwrapper=True)
def pytest_load_initial_conftests(
    early_config: Config, parser: Parser, args: List[str]
):
    if sys.gettrace():
        early_config.known_args_namespace.cov_source = None
        early_config.option.no_cov = True

    early_config.known_args_namespace.cov_context = "test"

    yield


def pytest_configure(config: Config):
    if is_enabled(config) and config.option.xmlpath is None:
        config.option.xmlpath = out_path


def pytest_terminal_summary(
    terminalreporter: Any, exitstatus: ExitCode, config: Config
):
    if is_enabled(config) and config.option.xmlpath != out_path:
        print(f"Copying {config.option.xmlpath} to {out_path}")
        shutil.copy(config.option.xmlpath, out_path)
