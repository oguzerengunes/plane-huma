import base64
import hashlib
import hmac
import secrets

PREFIX = "HUMA"


def normalize(code: str) -> str:
    """Boşluk/çizgi temizle, büyük harfe çevir."""
    return code.strip().upper().replace(" ", "").replace("-", "")


def generate_code() -> str:
    """16 byte secrets -> base32 26 char -> HUMA formatında kod."""
    raw = base64.b32encode(secrets.token_bytes(16)).decode().rstrip("=")
    assert len(raw) == 26, f"beklenen 26 char, geldi: {len(raw)}"
    return f"{PREFIX}-{raw[:13]}-{raw[13:]}"


def hash_code(code: str) -> str:
    """Ham kodu normalize edip sha256 hex döndür."""
    return hashlib.sha256(normalize(code).encode()).hexdigest()


def verify(code: str, code_hash: str) -> bool:
    """Zamanlama saldırısına dayanıklı karşılaştırma."""
    return hmac.compare_digest(hash_code(code), code_hash)


def prefix_of(code: str, n: int = 8) -> str:
    """Listeleme için ham olmayan önek."""
    return normalize(code)[:n]
