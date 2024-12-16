from dynaconf import Dynaconf

AUTH_JWT_SECRET_KEY = "test"

settings = Dynaconf(
    load_dotenv=True,
    environments=True,
    settings_files=['../settings.toml'],
)
