For this project I created a model that predicts if a D1 college basketball team would qualify for the postseason NCAA tournament.  Team statistics from https://www.sports-reference.com/ were used from the 1992-93 through the 2022-23 season.

Before building the model, data from the different seasons was aggregated.  The data from the distinct pages that had team statistics (such as number of games, number of wins, number of losses, etc), conference rankings, as well as whether or not the team qualified for the tournament were merged together for each team for each season from 1992-93 through 2022-23.  Web scrapers were built to capture the data and produce .csv files, and then another script was used to join the different files into one larger dataframe with all the information for each team for each season.  Please see the folder "data-collection".  After running all of the scrapers and merging all of the .csv files, "d1-basketball-data-93-23.csv" is created.

The data was split into training and test sets.  The initial training set was then split into new training and test sets.  These new sets were used to tweak parameters of the models (for example, the number of hidden layers in the neural network), while the original test set was used to validate (again) the model’s predictions.

Next, the data was prepared for machine learning.  Columns with a significant number of NaN/ null values were dropped.  Because the remaining rows with NaN/ null values only represented three percent of all rows, they were also removed.  The columns with the names of the teams were also removed, and the column with the conference of the team was turned into “dummy” features.  The remaining columns were standardized (rather than normalized because I did not want to assume the data was normally distributed).  The same standardizer that was used to transform the training set was used to transform both test sets.

Logistic, neural network and random forest classifiers were then created and evaluated.  Due to the significant imbalance between the proportion of qualifying and non-qualifying teams, F1 score was used to determine the best model because it takes into account the precision and recall of the model as well as the accuracy.  The random forest model was the most predictive, scoring an F1 score of 80%.

A SHAP tree explainer was then used to interpret the random forest model.  The feature that most impacted the model’s prediction was the Simple Rating System (SRS).  As defined by https://www.sports-reference.com/ , SRS is a “rating that takes into account average point differential and strength of schedule. The rating is denominated in points above/below average, where zero is average. Non-Division I games are excluded from the ratings''.  Please see the folder "model-development".  The scaler used for preparing the data, the code used to perform additional preprocessing, and the random forest model are labeled in this folder.

Finally, the random forest model can be deployed as a Docker image of a Flask application.  After running the Docker container, a user can upload a .csv file containing season data for one or more D1 NCAA basketball teams and then the tournament qualification predictions are listed.  An example of the required schema of the .csv is displayed on the application, as well as a glossary of the metrics used to train the model.  Please see the folder "ncaa-tourn-qual-flask-app".
