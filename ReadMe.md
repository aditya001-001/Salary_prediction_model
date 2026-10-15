# Salary Prediction Model

A machine learning application that predicts salary based on years of experience using a trained regression model and Streamlit.

## Features

- Accepts years of experience as user input.
- Predicts salary using a trained machine learning model.
- Displays the prediction through a simple web interface.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

## Project Structure

```text
Salary_prediction_model/
├── app.py
├── salary_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## Run Locally

1. Clone or download this repository.
2. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Make sure `salary_model.pkl` is present in the project directory.
4. Start the application:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL displayed in your terminal.

## How It Works

The application loads a previously trained regression model, accepts years of experience, and uses the model to generate a salary prediction.

## Limitations

Predictions depend on the training dataset and model quality. They are estimates, not guaranteed salaries. The currency and applicability of the prediction depend on the original dataset.

