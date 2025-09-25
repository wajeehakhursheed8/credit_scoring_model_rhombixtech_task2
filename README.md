Credit Scoring System
A Machine Learning-powered creditworthiness predictor with a Streamlit web app, developed during my internship at Rombex Technologies.

Overview
This project automates credit evaluation for financial institutions using Machine Learning. It predicts whether a customer is creditworthy and generates a credit score (0–1000) based on financial inputs like income, loan amount, and credit history. The interactive Streamlit web app allows users to input data and view predictions in real-time.

Features
Creditworthiness Prediction: Determines if a customer qualifies for credit.
Credit Score Generation: Outputs a score between 0 and 1000.
Interactive UI: Built with Streamlit for seamless user interaction.
Data Insights: Includes dataset analysis and visualization.
Modular Design: Clean, organized code structure for scalability.


Project Structure:
textcredit-scoring-ml/
├── data/                    # Dataset
│   └── credit_data.csv
├── models/                  # Trained ML model
│   └── credit_model.pkl
├── app/                     # Streamlit web app
│   └── app.py
├── notebooks/               # Jupyter notebooks for model training
│   └── training.ipynb
├── requirements.txt         # Dependencies
└── README.md

Installation & Setup:
Clone the repository:
bashgit clone https://github.com/wajeeha-khursheed/credit-scoring-ml.git
cd credit-scoring-ml

Install dependencies:
bashpip install -r requirements.txt

Run the Streamlit app:
bashstreamlit run app/app.py
Open the app in your browser (typically at http://localhost:8501).

Tech Stack:
Python: Core programming language
Pandas, NumPy: Data processing and analysis
Scikit-learn: Machine Learning model
Streamlit: Web app framework
Joblib: Model serialization

Future Enhancements:
Incorporate advanced features (e.g., debt-to-income ratio).
Optimize model with XGBoost or LightGBM.
Deploy to Streamlit Cloud, AWS, or Heroku.
Add real-time data integration for dynamic predictions.


Acknowledgments:
Developed during my internship at Rombex Technologies. 

👩‍💻 Author
Wajeeha Khursheed
