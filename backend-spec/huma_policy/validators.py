import os

ALLOWED = [d.strip().lower() for d in os.getenv("HUMA_ALLOWED_DOMAINS", "ogr.uni.edu.tr,uni.edu.tr").split(",") if d.strip()]


def is_allowed(email: str) -> bool:
    try:
        domain = email.strip().lower().split("@")[1]
    except IndexError:
        return False
    return domain in ALLOWED or any(domain.endswith("." + d) for d in ALLOWED)


def validate_email(email: str) -> None:
    if not is_allowed(email):
        raise ValueError("E-posta alan adına izin yok")
