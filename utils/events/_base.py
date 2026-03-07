def _e(title, desc, choices, city=None):
    return {"title": title, "desc": desc, "choices": choices, "city": city}

def _c(label, next_event=None, condition=None, rewards=None, flavor=None):
    return {"label": label, "next": next_event, "condition": condition, "rewards": rewards or {}, "flavor": flavor or ""}

def _cond(stat, val):
    return {"stat": stat, "val": val}
