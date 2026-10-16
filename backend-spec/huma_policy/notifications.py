QUOTA = 50
WARN = int(QUOTA * 0.8)


def event(kind, id, by, reason=""):
    assert kind in ("pending", "approve", "reject")
    return {"event": kind, "id": id, "by": by, "reason": reason}


def check_quota(used):
    if used >= QUOTA:
        raise Exception("kota doldu")
    if used >= WARN:
        return f"UYARI: %{used / QUOTA * 100:.0f} doldu ({used}/{QUOTA})"
    return "ok"
