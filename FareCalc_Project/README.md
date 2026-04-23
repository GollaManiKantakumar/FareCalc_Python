# FareCalc_Python
# 🚖 FareCalc – CityCab Ride Estimator

FareCalc is a simple Python-based backend script that simulates fare calculation for a ride-sharing service called **CityCab**.
The fare is calculated dynamically based on distance, vehicle type, and peak-hour surge pricing.

---

## 📌 Features

* Distance-based fare calculation
* Vehicle-based pricing using a dictionary
* Peak hour surge pricing (5 PM – 8 PM)
* Case-insensitive user input handling
* Error handling for invalid vehicle types
* Clean and formatted receipt output

---

## 🧠 Pricing Logic

The fare is calculated using a predefined rate per kilometer:

| Vehicle Type | Rate (₹/km) |
| ------------ | ----------- |
| Economy      | 10          |
| Premium      | 18          |
| SUV          | 25          |

* The rates are stored in a **dictionary (mapping)**
* Keys are maintained in **uppercase format** as per requirement
* User input is normalized to match dictionary keys

---

## ⏰ Surge Pricing

* Surge is applied during **peak hours (17–20)**
* Multiplier: **1.5x of total fare**

---

## 📁 Project Structure

FareCalc_Project/
├── main.py          # Handles user input and execution
├── fare_logic.py    # Contains fare calculation logic
├── utils.py         # Handles formatted output
├── README.md

---

## ▶️ How to Run

1. Open terminal or command prompt
2. Navigate to the project folder
3. Run the script:

```bash
python main.py
```

---

## 💡 Example Input

```
Distance (km): 10
Vehicle (Economy/Premium/SUV): suv
Hour (0-23): 18
```

---

## 🧾 Sample Output

```
------------------------------
CityCab Ride Summary
------------------------------
Distance : 10 km
Vehicle  : Suv
Time     : 18:00
Surge    : Yes (Peak hours)
------------------------------
Final Fare : ₹ 375.0
------------------------------
```

---

## ⚠️ Error Handling

* Invalid vehicle type → "Service Not Available"
* Invalid inputs → handled using exception blocks

---

## 🧠 Key Concepts Used

* Dictionary mapping for pricing
* Conditional logic for surge pricing
* Function-based modular design
* Input validation and error handling

---

## 📌 Author

Golla Manikanta Kumar

---

## 🚀 Future Improvements (Optional)

* Add GUI interface
* Store ride history
* Convert into REST API

---
