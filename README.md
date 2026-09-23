# BMI Calculator

A simple, responsive BMI calculator that runs entirely in the browser. It supports both metric (kilograms and meters) and imperial (pounds and inches) units.

## Use it

Open [`index.html`](index.html) in any modern web browser. No build tools, dependencies, or server are required.

1. Choose **Metric** or **Imperial**.
2. Enter your weight and height.
3. Select **Calculate BMI** to see your BMI and the corresponding category.

## Formula

BMI is calculated as:

```text
BMI = weight (kg) / height (m)²
```

Imperial values are converted to kilograms and meters before the calculation. Categories follow these general adult ranges:

- Underweight: below 18.5
- Normal weight: 18.5–24.9
- Overweight: 25–29.9
- Obesity: 30 or higher

BMI is a general screening measure and is not a substitute for advice from a qualified healthcare professional.

## Project files

- `index.html` — the complete front page, styling, and calculator logic.
- `calculator.py` — the original command-line implementation.
