# 🏡 Nigerian Housing Predictor

A machine learning practice project designed for the **NSBE UNILAG Machine Learning Skills Lab Training Program** to teach beginner machine learning concepts.

## 📋 Project Overview

This project demonstrates end-to-end machine learning workflow by predicting housing prices in Lagos, Nigeria. It serves as a hands-on learning tool for trainees to understand data science concepts, model building, and web application deployment using Streamlit.

## 🎯 Learning Objectives

This practice project helps trainees learn:
- Data preprocessing and feature engineering
- Machine learning model training and evaluation
- Model serialization and deployment
- Building interactive web applications with Streamlit
- Python programming best practices
- Project structure and organization

## 🚀 Features

- **Interactive Web Interface**: User-friendly Streamlit application for price predictions
- **Real-time Predictions**: Get instant housing price estimates based on input parameters
- **Multiple Input Parameters**: 
  - Number of bedrooms, bathrooms, and toilets
  - Parking spaces
  - House type (Detached Duplex, Terraced Bungalow, etc.)
  - Location within Lagos
- **Pre-trained Model**: Uses a saved machine learning pipeline for predictions

## 📁 Project Structure

```
Lagos-Housing-Predictor/
├── data/
│   └── nigeria_houses_data.csv     # Training dataset
├── models/
│   └── my_prediction_pipeline.pkl  # Pre-trained ML model
├── notebooks/
│   └── Nigerian_Housing.ipynb      # Jupyter notebook for analysis
├── src/
│   ├── app.py                      # Streamlit web application
│   └── main.py                     # Launcher script
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone/Download the project**
   ```bash
   # Clone from GitHub (replace with actual repository URL)
   git clone https://github.com/HaywhyCoder/Lagos-Housing-Predictor.git
   cd lagos-housing-predictor
   ```

   Or if downloading manually:
   ```bash
   # Navigate to your downloaded project folder
   cd "path/to/your/project/folder"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python src/main.py
   ```
   
   Or directly with Streamlit:
   ```bash
   streamlit run src/app.py
   ```

## 🖥️ Usage

1. Open the web application in your browser (typically at `http://localhost:8501`)
2. Use the sliders to set house specifications:
   - Number of bedrooms (1-10)
   - Number of bathrooms (1-10)
   - Number of toilets (1-10)
   - Parking spaces (1-10)
3. Select the house type from the dropdown menu
4. Choose a location in Lagos from the dropdown
5. Click "Get price" to receive the predicted housing price in Nigerian Naira (₦)

## 📊 Model Information

The machine learning model uses various features to predict housing prices:
- **Target Variable**: Housing price (log-transformed)
- **Features**: Bedrooms, bathrooms, toilets, parking spaces, house type, location
- **Model Type**: Saved as a scikit-learn pipeline (preprocessing + model)
- **Output**: Price prediction with exponential transformation

## 🎓 Educational Value

This project is specifically designed for **NSBE UNILAG Skills Lab trainees** to:

### For Beginners:
- Understand basic ML concepts through a practical example
- Learn how data flows from input to prediction
- Explore web application development with Python
- Practice reading and understanding code structure

### For Intermediate Learners:
- Examine model training process in the Jupyter notebook
- Understand data preprocessing techniques
- Learn about model evaluation and validation
- Practice debugging and code modification

## 📚 Learning Extensions

Trainees can extend this project by:

1. **Data Analysis**: Explore the dataset in `notebooks/Nigerian_Housing.ipynb`
2. **Model Improvement**: Experiment with different algorithms or features
3. **UI Enhancement**: Add more visualizations or improve the interface
4. **Feature Engineering**: Create new features from existing data
5. **Model Validation**: Implement cross-validation and performance metrics

## 🔧 Technical Stack

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning library (via joblib)
- **Jupyter**: Interactive development environment

## 📝 Notes for Trainees

- The model is pre-trained to focus on application development
- Price predictions are estimates based on historical data
- This is a learning tool - real estate decisions should involve professional consultation
- Experiment with the code to better understand how it works

## 🤝 Contributing

This is an educational project for the NSBE UNILAG Skills Lab. Trainees are encouraged to:
- Ask questions about the code
- Suggest improvements
- Practice version control with git
- Share learnings with fellow trainees
