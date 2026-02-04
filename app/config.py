from __future__ import annotations

import os
from dotenv import load_dotenv


def load_config() -> dict:
    """
    Read settings for connect to databse from .env file and return a dict
    """
    load_dotenv()  # pulls .env from the project

    def need(name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise ValueError(f"Missing env var: {name}")
        return value

    return {
        "host": need("DB_HOST"),
        "port": int(need("DB_PORT")),
        "dbname": need("DB_NAME"),
        "user": need("DB_USER"),
        "password": need("DB_PASSWORD"),
    }
