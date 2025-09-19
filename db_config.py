import os


def get_db_uri(project="daredevls"):
    if project == "genai":
        return os.getenv("DATABASE_URL_GENAI")
    return os.getenv("DATABASE_URL_DAREDEVLS")
