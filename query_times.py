import os
import csv
import re
import subprocess
import statistics
from pathlib import Path

BASE_DIR = Path(__file__).parent

DATABASE = BASE_DIR / "databases" / "tpch.db"
QUERY_DIR = BASE_DIR / "queries"
RESULTS_DIR = BASE_DIR / "results"

VERSIONS = {
    "3.35.0": BASE_DIR / "sqlite_versions" / "sqlite-3.35.0" / "sqlite3.exe",
    "3.40.0": BASE_DIR / "sqlite_versions" / "sqlite-3.40.0" / "sqlite3.exe",
    "3.45.0": BASE_DIR / "sqlite_versions" / "sqlite-3.45.0" / "sqlite3.exe",
    "3.50.0": BASE_DIR / "sqlite_versions" / "sqlite-3.50.0" / "sqlite3.exe",
}

REPETITIONS = 10

RESULTS_DIR.mkdir(exist_ok=True)

def run_query(sqlite_exe, query_file):

    