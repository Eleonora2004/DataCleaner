# DataCleaner # DataCleaner
# DataCleaner

**DataCleaner** is a tool for data cleaning and preprocessing, designed to automate common tasks when working with tabular datasets.

---

## 📌 Features

- Remove missing values
- Fill NaNs with mean, median, or a custom value
- Remove duplicate rows
- Convert data types
- Normalize and scale numerical features
- Encode categorical features (One-Hot Encoding / Label Encoding)
- Save cleaned dataset to file

---

## 📁 Project Structure
DataCleaner/
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   └── sample_input.csv
├── src/
│   └── cleaner.py
├── examples/
│   └── usage_example.ipynb
---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/eleonora2004/DataCleaner.git
cd DataCleaner
pip install -r requirements.txt
from src.cleaner import DataCleaner

dc = DataCleaner("data/sample_input.csv")
df_cleaned = dc.clean(
    fill_missing='mean',
    drop_duplicates=True,
    encode_categorical=True
)

df_cleaned.to_csv("data/cleaned_output.csv", index=False)
jupyter notebook examples/usage_example.ipynb
name
age
income
gender
Alice
25
55000
Female
Bob
NaN
63000
Male
Alice
25
55000
Female
After cleaning:
name
age
income
gender_Female
gender_Male
Alice
25
55000.0
1
0
Bob
25
63000.0
0
1
This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
Contributions are welcome! Please review the CONTRIBUTING.md and CODE_OF_CONDUCT.md files before submitting a pull request.
