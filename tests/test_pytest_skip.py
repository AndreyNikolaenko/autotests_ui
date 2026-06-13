import pytest

SYSTEM_VERSION = "v1.2.0"

# SKIP
@pytest.mark.skip(reason="This test needs to be skipped")
def test_feature_in_development():
    ...

@pytest.mark.skip(reason="This test needs to be skipped")
class TestSuiteSkip:
    def test_feature_in_development1(self):
        ...

    def test_feature_in_development2(self):
        ...

# SKIPIF

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason="Тест не может быть запущен на версии v1.3.0"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="Тест не может быть запущен на версии v1.2.0"
)
def test_system_version_invalid():
    ...


# XFAIL

@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert False

@pytest.mark.xfail(reason="Баг уже исправлен, но на тесте всё еще висит маркировака xfail")
def test_without_bug():
    ...