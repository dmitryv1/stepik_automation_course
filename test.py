from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
