# Model Development

This folder contains the exploratory data analysis notebook, the notebook used to preprocess data, and create & evaluate models, the dataset used for training the models, and the .pkl files for the model and scaler to be used for deployment.

- **d1-baskeball-data-93-23.csv**:  dataset of all data scraped for each team for each season
- **EDA.ipynb**:  notebook containing the exploratory data analysis of the dataset
- **NCAA-tourn-qual-model.ipynb**:  notebook containing the splitting & preprocessing of data, creation & evaluation of machine learning models, and SHAP interpretation of best model
- **ncaa-tourn-qual-model-rfc.pkl**:  artifact file of the model (to be used in deployment)
- **ncaa-tourn-qual-scaler.pkl**:  artifact file of the scaler used to preprocess team data (to be used in deployment)
