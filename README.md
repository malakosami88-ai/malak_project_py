# malak_project_py
# Companion – Nearest-Neighbor Reading Classifier

A lightweight Python project that classifies numeric sensor/health readings as **"Normal"** or **"Unusual"** using a simple nearest-neighbor approach against a small set of labeled example readings.

## How It Works

The `companion` class stores a dictionary of example readings mapped to labels (`Normal` / `Unusual`). When a new reading comes in, it finds the closest known example (by absolute difference) and returns that example's label.

```python
self.examples = {45: "Normal", 52: "Normal", 48: "Normal", 95: "Unusual", 88: "Unusual"}
```

Any new value is classified based on whichever example number it is numerically closest to.

## Features

- Simple 1-nearest-neighbor classification logic
- Tracks a history of readings flagged as "Unusual" (`self.readings`)
- Includes a small built-in test set to measure classification accuracy

## Usage

```python
my_companion = companion("Mr Bigo")

# Classify a single reading
result = my_companion.classify(80)
print(result)  # "Unusual" or "Normal"

# Unusual readings are automatically logged
print(my_companion.readings)
```

## Testing Accuracy

The script includes a small labeled test set to evaluate the classifier:

```python
test = [(55, "unusual"), (91, "Unusual"), (47, "Normal"), (100, "Unusual"), (55, "Normal")]
```

Running the script prints any mismatches between predicted and expected labels, followed by the overall accuracy percentage.

## Requirements

- Python 3.x (no external libraries required)

## Running the Project

```bash
python AI_project.py
```

## Example Output

```
The question: 55
The wrong answer: Normal
Right answer: Normal
Accuracy= 80.0 %
Unusual
[80]
```

*(Exact output will vary depending on the test cases and classification results.)*

## Notes

- The example dataset (`self.examples`) is very small; for more reliable classification, consider expanding it with more labeled readings.
- Labels in the `test` set should be consistent in casing (e.g., `"unusual"` vs `"Unusual"`) to avoid accuracy mismatches from formatting rather than actual misclassification.

## License

Add a license of your choice (e.g., MIT) here.
