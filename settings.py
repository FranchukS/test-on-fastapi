import environs


env = environs.Env()
env.read_env(".env")

DB_CONFIG = {
    "connections": {
        "default": env("DB_CONNECTION_URL")
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        }
    }
}
