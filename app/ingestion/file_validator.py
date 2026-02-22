# app/ingestion/file_validator.py

from pathlib import Path

SUPPORTED_EXTENSIONS = {".py", ".ts", ".md", ".txt", ".json"}

MAX_FILE_SIZE_MB = 5


class FileValidationError(Exception):
    pass


def validate_file_path(file_path: str) -> Path:
    path = Path(file_path)

    # 1️⃣ Check existence
    if not path.exists():
        raise FileValidationError(f"File does not exist: {file_path}")

    # 2️⃣ Ensure it's a file (not directory)
    if not path.is_file():
        raise FileValidationError(f"Expected a file but got directory: {file_path}")

    # 3️⃣ Validate extension
    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise FileValidationError(
            f"Unsupported file type: {path.suffix}. "
            f"Supported: {SUPPORTED_EXTENSIONS}"
        )

    # 4️⃣ Validate file size
    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        raise FileValidationError(
            f"File too large ({size_mb:.2f} MB). Max allowed: {MAX_FILE_SIZE_MB} MB"
        )

    return path
