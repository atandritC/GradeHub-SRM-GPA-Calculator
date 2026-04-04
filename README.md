# GradeHub

**SRM University GPA Calculator**  
A Streamlit-powered web app that helps SRM University students instantly compute their Grade Point Average — featuring credit-based grade input, real-time GPA calculation, and a clean, intuitive interface designed specifically for SRM's grading system.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io)
[![SRM University](https://img.shields.io/badge/SRM-University-0066CC.svg?logo=googlechrome&logoColor=white)](https://www.srmist.edu.in)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🛠 Tech Stack

**Backend & Logic**
- Python 3.8+ — Clean, readable scripts for GPA computation and validation
- Streamlit — Reactive UI framework for instant form handling and result rendering

**Frontend & UX**
- Streamlit native components — Text inputs, number sliders, and dynamic result cards
- Responsive layout — Works seamlessly on desktop and mobile browsers
- Zero custom CSS — Leverages Streamlit's theming for a polished, accessible interface

**Data & Validation**
- SRM-specific grading scale — Hardcoded grade-to-point mapping (S=10, A=9, B=8, etc.)
- Input sanitization — Validates credit values (positive integers) and grade codes before calculation
- Formula: `GPA = Σ(GradePoint × Credits) / Σ(Credits)` implemented with floating-point precision

## ✨ Key Features

- **SRM-Optimized Grading** — Pre-configured with SRM University's official grade-to-point conversion table
- **Instant Calculation** — GPA updates in real-time as you add or modify courses
- **Dynamic Course Entries** — Add/remove courses on the fly with credit and grade fields
- **Clear Result Display** — Shows computed GPA with two-decimal precision and total credits summary
- **Zero Setup for Users** — Hosted live on Streamlit Cloud; no installation required
- **Local Development Ready** — Simple `pip install` and `streamlit run` workflow for contributors
- **Lightweight & Fast** — Pure Python logic; no external APIs or database dependencies

## 📸 Demo

![GradeHub Demo](https://github.com/atandritC/Project-Demos/blob/main/GradeHub.gif)

## 🏗 Architecture

- **Single-File Simplicity** — All logic and UI contained in `app.py` for easy maintenance and deployment
- **Reactive Computation** — Streamlit's auto-rerun triggers GPA recalculation on any input change
- **Grade Mapping Dictionary** — Centralized `GRADE_POINTS` dict ensures consistent SRM grading logic
- **Input Validation Layer** — Checks for empty fields, invalid grade codes, and non-positive credits before computing
- **Stateless Design** — No session persistence required; each calculation is independent and privacy-friendly

## ⚙️ How to Run Locally

No Docker, no database, no complex setup — just Python and Streamlit.

```bash
# Clone the repository
git clone https://github.com/atandritC/GradeHub-SRM-GPA-Calculator.git
cd GradeHub-SRM-GPA-Calculator

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

The app will open automatically in your browser. Start adding your courses, credits, and grades to see your GPA update instantly.

> 🌐 **Use Online**: No setup needed — visit the live app at [srm-gpa-calculator.streamlit.app](https://srm-gpa-calculator.streamlit.app/)

## 🧠 Challenges Faced & Solutions

| Challenge | Solution |
|---|---|
| SRM uses non-standard grade codes (S, A+, B-, etc.) not found in generic calculators | Created a hardcoded `GRADE_POINTS` dictionary matching SRM's official academic handbook |
| Users might enter invalid grades or negative credits | Added input validation with clear error messages using Streamlit's `st.error()` and conditional rendering |
| GPA formula must handle dynamic number of courses | Used Python list comprehensions and `zip()` to compute weighted sums regardless of course count |
| Streamlit reruns entire script on every input change | Leveraged this behavior intentionally — no manual "calculate" button needed; results update reactively |
| Floating-point precision could show long decimals | Applied `round(gpa, 2)` for clean two-decimal output matching university transcript format |

## 📈 What I Learned

- Building domain-specific tools by encoding institutional rules (like SRM's grading scale) into simple logic
- Designing reactive forms in Streamlit that feel instant and intuitive without manual submission
- Validating user input gracefully to prevent calculation errors while maintaining a friendly UX
- Deploying Python web apps to Streamlit Cloud with zero-config CI/CD
- Keeping projects minimal and focused — solving one problem well rather than over-engineering

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repo and create your feature branch:  
   `git checkout -b feature/AmazingFeature`
2. Commit your changes:  
   `git commit -am 'Add some AmazingFeature'`
3. Push to the branch:  
   `git push origin feature/AmazingFeature`
4. Open a Pull Request with a clear description of your changes

**Guidelines**:
- Follow PEP 8 style and include docstrings for new functions
- Test GPA calculations with edge cases (0 credits, all S grades, mixed inputs)
- Preserve SRM-specific grading logic unless updating based on official policy changes
