# ProjectNetwork: SECRET=0, PUBLIC=2 — yeni projeler varsayılan SECRET
DEFAULT_NETWORK = "SECRET"


def coerce_network(value: str | None) -> str:
    if not value:
        return DEFAULT_NETWORK
    v = value.strip().upper()
    return v if v in ("SECRET", "PUBLIC") else DEFAULT_NETWORK
