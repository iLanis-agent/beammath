# Beam math

The candela names the throw, the cell names the hours, and the charger names the wait.

A flashlight box leads with lumens because lumens are the big number, but lumens say nothing about reach. Beam math works the three numbers that decide the purchase: throw from candela, runtime from the cell's watt-hours, and the honest wait at the charger.

## The three tools

- **Throw plan** - candela becomes meters by the ANSI throw rule (twice the square root), banded from a hallway light to a searchlight.
- **Runtime plan** - lumens against cell watt-hours at a labeled 80 system lumens per watt becomes real hours, banded from a sprint, not a hike to a week of evenings.
- **Charge plan** - cell mAh against charger mA at a labeled 85% efficiency becomes the wait, banded from a quick top-up to a day at the outlet.

Every band judges the unrounded figure; only the display rounds.

## Honesty notes

Illustrative planning arithmetic only. Every figure is a labeled default you replace by reading your own spec sheet. Real lights step down as they heat: the box number is the first minute, not the last. Never shine a powerful light at people, drivers or aircraft, and match the cell to what the light's manual allows.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
