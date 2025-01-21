# Optimizing Power Allocation for Enhanced Energy Efficiency in NOMA Systems

## Requirements

- numpy==2.2.2
- packaging==24.2
- plotly==5.24.1
- tenacity==9.0.0

## Instructions

1. Run the following command

```bash
pip install -r requirements.txt
```

2. Run the following command in your terminal to run your local environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

3. Run this command to start running the script

```bash
python .\visualization\visualization.py
```

4. After finishing you can deactivate the local instance using this command

```bash
deactivate
```

## Steps to Optimize Power Allocation

1. Objectives

- Maximize System Throughput: Ensure higher data rates across users.
- Enhance Energy Efficiency: Reduce power consumption while maintaining performance.
- Ensure Fairness: Guarantee equitable resource distribution among users.
- Minimize Interference: Reduce cross-user interference in the superimposed signal.

2. Constraints

- Total Power Budget: The sum of allocated powers should not exceed the available power.
- User QoS Requirements: Each user must achieve a minimum required data rate.
- Channel Conditions: Take user channel gains into account (e.g., stronger users get less power in NOMA).

## 3. System Model

- **Superposition Coding**: Combining signals with different power levels based on priority.  
  \[
  s\_{\text{total}} = \sqrt{\alpha_1} s_1 + \sqrt{\alpha_2} s_2
  \]

- **Successive Interference Cancellation (SIC)**: To ensure proper decoding at the receiver.
  - User 2 decodes User 1’s signal first, subtracts it, then decodes its own.

---

## 4. Optimization Problem Formulation

- **Objective Function**: Maximizing the sum rate:  
  \[
  R*{\text{sum}} = \sum*{i=1}^N \log_2 \left( 1 + \frac{\text{Signal Power}\_i}{\text{Interference + Noise}} \right)
  \]

- **Constraints**:  
  \[
  \sum*{i=1}^N P_i \leq P*{\text{total}}
  \]  
  \[
  R*i \geq R*{\text{min}\_i} \quad \text{(for each user)}
  \]
