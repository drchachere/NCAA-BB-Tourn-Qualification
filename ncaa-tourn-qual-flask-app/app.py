from flask import Flask, render_template, flash, request, redirect, url_for
import numpy
import pandas as pd
import joblib
import sklearn
import os

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "csv"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'ufile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['ufile']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file_name = "_"+file.filename
        if allowed_file(file.filename):
            file.save(file_name)
        # print(file_name)
        if file and allowed_file(file.filename):
            user_df = pd.read_csv(file_name)
            model = joblib.load("ncaa_tourn_qual_model_rfc.pkl")
            scaler = joblib.load("ncaa_tourn_qual_scaler.pkl")
            user_df.columns = list(map(lambda x: x.strip(), user_df.columns))
            try:
                df_scaled = scaler.transform(user_df.iloc[:, 0:23])
                data_scaled = pd.DataFrame(df_scaled, columns=['G', 'W', 'L', 'W-L%', 'SRS', 'SOS', 'W.1', 'L.1', 'W.2', 'L.2', 'W.3', 'L.3', 'Tm.', 'Opp.', 'FTr', '3PAr', 'TS%', 'TRB%', 'AST%', 'BLK%', 'eFG%', 'TOV%', 'FT/FGA'])
                data_ord = pd.get_dummies(user_df.iloc[:,23])
                data_ord = pd.DataFrame(data_ord, columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
                data_ord.columns = data_ord.columns.astype(str)
                data_ord = data_ord.fillna(0)
                data_dum = pd.get_dummies(user_df.iloc[:,24])
                data_dum = pd.DataFrame(data_dum, columns=['WAC', 'MAC', 'SEC', 'SWAC', 'CAA', 'Southern', 'Pac-10', 'Sun Belt', 'Patriot', 'OVC', 'SWC', 'MEAC', 'Big Sky', 'Big East', 'NAC', 'MVC', 'Ivy', 'MW Coll', 'Big West', 'Big South', 'MAAC', 'TAAC', 'Metro', 'GMWC', 'ACC', 'Mid-Cont', 'Big 8', 'NEC', 'WCC', 'Big Ten', 'Southland', 'A-10', 'ECC', 'AWC', 'CUSA', 'Big 12','AEC', 'MWC', 'A-Sun', 'Horizon', 'Summit', 'GWC', 'Pac-12', 'AAC'])
                data_dum = data_dum.fillna(0)
                data_ml = pd.concat([data_scaled, data_ord, data_dum], axis=1)
                data_ml = numpy.array(data_ml)
                result = model.predict(data_ml)
            except:
                os.remove(file_name)
                return """<p><b>ERROR</b> - Please check that the schema of the .csv file you have uploaded matches the example and try again.</p><br>
                <form action="/">
                    <button>Go Back</button>
                </form>
                """
            else:
                os.remove(file_name)
                return redirect(url_for("predictions", res=result))
    else:
        return render_template('index.html')

@app.route('/predictions/<res>', methods=['GET', 'POST'])
def predictions(res):
    return render_template('index2.html', res=res)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5002)