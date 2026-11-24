import pytest
from pydantic import ValidationError

from jobscout.config import Settings


@pytest.fixture
def valid_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DB_HOST", "test-host")
    monkeypatch.setenv("DB_NAME", "test_db")
    monkeypatch.setenv("DB_USER", "test_user")
    monkeypatch.setenv("DB_PORT", "1234")
    monkeypatch.setenv("DB_PASSWORD", "test_password")
    monkeypatch.setenv("REDIS_URL", "redis://localhost:6379/0")
    monkeypatch.setenv("MISTRAL_API_KEY", "TEST_KEY")


def test_app_env_default(valid_env: None):
    settings = Settings(_env_file=None)
    assert settings.app_env == "dev"


def test_db_port(valid_env: None):
    settings = Settings(_env_file=None)
    assert settings.db_port == 1234


def test_no_required_field(valid_env: None, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("MISTRAL_API_KEY")
    with pytest.raises(ValidationError) as exc_info:
        Settings(_env_file=None)

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("mistral_api_key",)
    assert errors[0]["type"] == "missing"


def test_wrong_app_env(valid_env: None, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("APP_ENV", "aboba")

    with pytest.raises(ValidationError) as exc_info:
        Settings(_env_file=None)

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("app_env",)
    assert errors[0]["type"] == "literal_error"


def test_secretstr_key(valid_env: None):
    settings = Settings(_env_file=None)

    assert "TEST_KEY" not in str(settings)
    assert "TEST_KEY" not in repr(settings)
    assert "test_password" not in str(settings)
    assert "test_password" not in repr(settings)
    assert settings.mistral_api_key.get_secret_value() == "TEST_KEY"


def test_postgres_dsn(valid_env: None):
    settings = Settings(_env_file=None)

    assert settings.postgres_dsn == ("postgresql://test_user:test_password@test-host:1234/test_db")
