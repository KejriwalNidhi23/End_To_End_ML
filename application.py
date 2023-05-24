from flask import Flask, redirect, url_for, render_template, request
from src.exception import CustomException
from src.logger import logging
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
import sys

app = Flask(__name__)

## Route for home page
@app.route("/")
def index():
    return render_template('home.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        else:
            data = CustomData(
                gender = request.form.get('gender'),
                race_ethnicity = request.form.get('ethnicity'),
                parental_level_of_education = request.form.get('parental_level_of_education'),
                lunch = request.form.get('lunch'),
                test_preparation_course = request.form.get('test_preparation_course'),
                reading_score = request.form.get('reading_score'),
                writing_score = request.form.get('writing_score')
            )
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            logging.info('Input Data Read as DataFrame')

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            logging.info('Prediction completed')

            return render_template('home.html',results=results[0])
        
    except Exception as e:
        raise CustomException(e,sys)


if __name__=="__main__":
    app.run(debug=True)