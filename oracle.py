import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)
def round0(x): return jsnum(math.floor(x + 0.5))

LUMENS_PER_W = 80
CHARGE_EFF = 0.85

def throw_plan(candela):
    if not (candela > 0):
        return {"error": "the candela must be positive"}
    raw = 2 * math.sqrt(candela)  # bands judge the true figure
    meters = round0(raw)
    if raw < 50: verdict = "a hallway light"
    elif raw < 150: verdict = "a yard light"
    elif raw < 400: verdict = "a trail light"
    else: verdict = "a searchlight"
    return {"meters": meters, "verdict": verdict}

def runtime_plan(lumens, wh):
    if not (lumens > 0) or not (wh > 0):
        return {"error": "the lumens and the cell must be positive"}
    raw = wh * LUMENS_PER_W / lumens  # bands judge the true figure
    hours = round1(raw)
    if raw < 1: verdict = "a sprint, not a hike"
    elif raw < 3: verdict = "an evening walk"
    elif raw < 8: verdict = "a night shift"
    else: verdict = "a week of evenings"
    return {"hours": hours, "verdict": verdict}

def charge_plan(mah, ma):
    if not (mah > 0) or not (ma > 0):
        return {"error": "the cell and the charger must be positive"}
    raw = mah / ma / CHARGE_EFF  # bands judge the true figure
    hours = round1(raw)
    if raw <= 2: verdict = "a quick top-up"
    elif raw <= 5: verdict = "an overnight charge"
    else: verdict = "a day at the outlet"
    return {"hours": hours, "verdict": verdict}

def render_throw(r, candela):
    return "A " + fmt(candela) + " cd beam reaches about " + fmt(r["meters"]) + " m - " + r["verdict"] + "."

def render_runtime(r, lumens, wh):
    return "Your " + fmt(lumens) + " lm on a labeled " + fmt(wh) + " Wh cell runs about " + fmt(r["hours"]) + " h - " + r["verdict"] + "."

def render_charge(r, mah, ma):
    return "A " + fmt(mah) + " mAh cell on a labeled " + fmt(ma) + " mA charger fills in about " + fmt(r["hours"]) + " h - " + r["verdict"] + "."

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[10000],[2500],[1000],[40000],[625],[15000],[20000],[500],[0],[100000]]:
    add("throwPlan", throw_plan, render_throw, a)
for a in [[1000,12],[400,12],[2000,12],[100,12],[1000,24],[600,10],[1500,12],[50,12],[0,12],[1000,0]]:
    add("runtimePlan", runtime_plan, render_runtime, a)
for a in [[3500,1000],[2000,2000],[5000,1000],[3500,500],[1800,1000],[4000,2000],[3000,1500],[5000,2000],[0,1000],[3500,0]]:
    add("chargePlan", charge_plan, render_charge, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
