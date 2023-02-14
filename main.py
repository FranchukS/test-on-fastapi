import uvicorn

from core.connection_db import connect_database


def main():
    connect_database()
    uvicorn.run("api.api:app", port=8000, log_level="info", reload=True)


if __name__ == "__main__":
    main()
