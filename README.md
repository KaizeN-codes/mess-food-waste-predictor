# 🍽️ AI Mess Food Waste Predictor

A small Python project that uses the **Hill Climbing search algorithm** to recommend how many servings a college/hostel mess should prepare, so that food wastage and food shortage are both reduced.

> Course: Artificial Intelligence & Soft Computing
> Author: *Aryan Raj* | Roll No: *2427030590* | Institute: *Manipal University Jaipur*

---

## 📌 Problem Statement

College and hostel messes usually prepare food based on rough estimates. As a result:

- **Some days** a lot of food is left over and thrown away (wastage).
- **Other days** food runs short and students go hungry (shortage).

This project treats the decision "how many servings should we cook?" as a **search/optimization problem** and solves it with Hill Climbing.

---

## 💡 Approach

Hill Climbing is a local search algorithm: start with a guess, look at nearby options, move to a better one, and stop when nothing nearby is better.

| Hill Climbing element | In this project |
|---|---|
| **State** | Number of servings to prepare (`current_servings`) |
| **Initial state** | One serving per expected student |
| **Neighbors** | `current_servings ± step` (a bit less / a bit more food) |
| **Objective function** | `score(servings) = -abs(prepared_food - target_food)` |
| **Target** | Expected demand + 3% safety buffer |
| **Move rule** | Move only if the neighbor has a strictly higher score |
| **Termination** | Step size shrinks to 0 with no further improvement |

### Score function

```python
def score(servings):
    prepared_food = servings * serving_size
    target_food = students * serving_size * 1.03   # 3% safety buffer
    return -abs(prepared_food - target_food)
```

The score is the **negative gap** between prepared and target food. A smaller gap gives a higher score, and the best possible score is `0` (exact match). The negative sign is used because hill climbing *maximizes*.

### Adaptive step size

The search starts with a step of about 5% of the student count (`students // 20`, minimum 1). Whenever a round brings no improvement, the step is halved (e.g. 5 → 2 → 1 → 0). Big steps get close quickly, and small steps fine-tune the answer.

---

## 🔄 Algorithm (Pseudocode)

```
read students, serving_size
current = max(1, students)
step    = max(1, students // 20)

while step >= 1:
    improved = False
    for change in (-step, +step):
        candidate = current + change
        if candidate < 1: skip
        if score(candidate) > score(current):
            current  = candidate
            improved = True
    if not improved:
        step = step // 2

output current as the recommended servings
```

---

## 🚀 How to Run

**Requirements:** Python 3.6+ (no external libraries needed)

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python mess_food_waste_predictor.py
```

### Sample run

```
=============================================
       AI MESS FOOD WASTE PREDICTOR
=============================================
How many students are expected? 100
Food per student in grams (example: 300): 300

--- AI Recommendation ---
Expected students: 100
Food per serving: 300 grams
Recommended servings to prepare: 103
Approximate total food: 30900 grams
Safety buffer: 3 servings
```

### How the search reached 103 (100 students, 300 g)

| Round | Step | Tried | Result |
|---|---|---|---|
| 1 | 5 | 95, 105 | moved to 105 |
| 2 | 5 | 100, 110 | no improvement → step 2 |
| 3 | 2 | 103, 105 | moved to 103 (score 0) |
| 4 | 2 | 101, 105 | no improvement → step 1 |
| 5 | 1 | 102, 104 | no improvement → step 0, **stop** |

---

## 📂 Project Structure

```
.
├── mess_food_waste_predictor.py   # Complete program
└── README.md                      # Project documentation
```

---

## ⚠️ Limitations

- The score function is unimodal (single peak), so hill climbing always finds the global optimum here. The same answer could also be computed directly as `round(students × 1.03)`. The project demonstrates the search technique rather than a necessity for search.
- The 3% buffer is a fixed assumption, not learned from data.
- It is **not** a machine-learning predictor: it does not forecast attendance and uses no historical data.
- Wastage and shortage are penalized equally, whereas in reality shortage is often worse.
- No input validation (non-numeric or negative input is not handled).
- Plans a single meal and a single dish only.

---

## 🔮 Future Scope

- Learn demand from historical attendance, weather, menu, and day of week.
- Use an asymmetric cost where shortage is penalized more than leftovers.
- Add input validation and a simple GUI/web interface.
- Optimize multiple dishes and meals together.
- Use fuzzy logic to estimate uncertain attendance (a soft-computing extension).
- Use Simulated Annealing or Genetic Algorithms for multi-dimensional problems where hill climbing could get stuck in local maxima.

---

## 🧠 Key Concepts

`Hill Climbing` · `Local Search` · `Objective Function` · `Adaptive Step Size` · `Optimization` · `Food Waste Reduction`

---

## 📜 License

This project is for academic purposes. Add a license of your choice (e.g. MIT) if you wish to share it publicly.
