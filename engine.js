(function (root) {
  "use strict";
  var LUMENS_PER_W = 80;  // labeled system lumens per watt, not emitter claims
  var CHARGE_EFF = 0.85;  // labeled charge efficiency

  function round0(x) { return Math.round(x); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function throwPlan(candela) {
    if (!(candela > 0)) return { error: "the candela must be positive" };
    var raw = 2 * Math.sqrt(candela); // ANSI throw to 0.25 lux; bands judge the true figure
    var meters = round0(raw);
    var verdict;
    if (raw < 50) verdict = "a hallway light";
    else if (raw < 150) verdict = "a yard light";
    else if (raw < 400) verdict = "a trail light";
    else verdict = "a searchlight";
    return { meters: meters, verdict: verdict };
  }

  function runtimePlan(lumens, wh) {
    if (!(lumens > 0) || !(wh > 0)) return { error: "the lumens and the cell must be positive" };
    var raw = wh * LUMENS_PER_W / lumens; // bands judge the true figure
    var hours = round1(raw);
    var verdict;
    if (raw < 1) verdict = "a sprint, not a hike";
    else if (raw < 3) verdict = "an evening walk";
    else if (raw < 8) verdict = "a night shift";
    else verdict = "a week of evenings";
    return { hours: hours, verdict: verdict };
  }

  function chargePlan(mah, ma) {
    if (!(mah > 0) || !(ma > 0)) return { error: "the cell and the charger must be positive" };
    var raw = mah / ma / CHARGE_EFF; // bands judge the true figure
    var hours = round1(raw);
    var verdict;
    if (raw <= 2) verdict = "a quick top-up";
    else if (raw <= 5) verdict = "an overnight charge";
    else verdict = "a day at the outlet";
    return { hours: hours, verdict: verdict };
  }

  function renderThrow(r, candela) {
    return "A " + candela + " cd beam reaches about " + r.meters + " m - " + r.verdict + ".";
  }

  function renderRuntime(r, lumens, wh) {
    return "Your " + lumens + " lm on a labeled " + wh + " Wh cell runs about " + r.hours + " h - " + r.verdict + ".";
  }

  function renderCharge(r, mah, ma) {
    return "A " + mah + " mAh cell on a labeled " + ma + " mA charger fills in about " + r.hours + " h - " + r.verdict + ".";
  }

  var api = { throwPlan: throwPlan, runtimePlan: runtimePlan, chargePlan: chargePlan, renderThrow: renderThrow, renderRuntime: renderRuntime, renderCharge: renderCharge };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.BeamMath = api;
})(this);
