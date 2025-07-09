> 📘 Este README está disponível em: [🇧🇷 Português](README.md) | [🇺🇸 English](README.en.md)

# 📊 Shift Optimization with Gurobi

This project applies an **Integer Linear Programming** model using **Gurobi** to optimize employee scheduling over a 24-hour period, aiming to minimize salary costs while meeting multiple demand scenarios.

---

## 🎯 Objective

- Allocate employees in 6-hour shifts across 24 time periods efficiently.
- Minimize total labor cost based on hourly salary multipliers.
- Ensure each hour is covered by the minimum required number of employees.
- Test the model against multiple demand scenarios using external instances.

---

## 📁 File Structure

- `Trabalho Final.py` — main script containing model definition and data processing.
- `Tab_Func.txt` — configuration file with time slots, minimum staffing and salary multipliers.
- `inst_4a.txt` through `inst_6b.txt` — various demand instances to be tested.

---

## ⚙️ Resources Used

- `gurobipy` — mathematical model creation, variable declaration, constraint setting and solving.
- `.txt` file parsing for dynamic parameter and scenario input.
- Loop logic to reconfigure the model for each scenario.

---

## 🧠 Model Variables

- `x[i]` — number of workers starting their shift at hour `i`
- `Q[i]` — total number of workers present during hour `i`

---

## 📌 Constraints

- Each hour must be staffed by workers who started their shift in the previous 6 periods.
- The total presence `Q[i]` must meet the minimum required staff for that hour.
- Variables are integer and non-negative.

---

## 💰 Objective Function

Minimize:
```math
\sum_{i=0}^{23} Q[i] \times salary[i]
