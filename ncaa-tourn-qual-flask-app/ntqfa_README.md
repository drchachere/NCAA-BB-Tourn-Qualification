# NCAA Tournament Qualification Flask App

This folder contains the files need to locally deploy the model as a containerized Flask app.  To locally deploy, copy this folder, build the container from the folder, and then run it.

- **ncaa-tourn-qual-model-rfc.pkl**:  artifact file of the model (to be used in deployment)
- **ncaa-tourn-qual-scaler.pkl**:  artifact file of the scaler used to preprocess team data (to be used in deployment)
- **app.py**:  the Flask app that uses the scaler and model to predict if the team data sumbitted by the user would yeild a tournament seed of 16 or better
- **templates/**:  HTML templates used by Flask app
- **Dockerfile**:  the build file used to create a containerized version of the Flask app for local deployment