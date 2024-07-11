import numpy as np
import pickle
import pandas as pd
from flask import Flask,url_for,render_template
from forms import Inputform;
app = Flask(__name__)

app.config["SECRET_KEY"]="secret_key"
with open('pipe3.pkl', 'rb') as file:
  model = pickle.load(file)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title = "Home")

@app.route("/predict",methods=['GET','POST'])
def predict():
    form =Inputform()
    if form.validate_on_submit():
        x_new = pd.DataFrame({
            'Company': [form.Company.data],
            'TypeName': [form.TypeName.data],
            'Ram': [form.Ram.data],
            'Weight': [form.Weight.data],
            'Touchscreen': [form.Touchscreen.data],
            'IPS Panel': [form.IPS_Panel.data],
            'ppi': [form.ppi.data],
            'Brand': [form.Brand.data],
            'HDD': [form.HDD.data],
            'SSD': [form.SSD.data],
            'gpu brand': [form.gpu.data],
            'op s': [form.ops.data]
        })
        prediction = np.exp(model.predict(x_new)[0])
        message = f"The predicted price is {prediction:,.0f} INR"
    else:
        message = "Please provide valid input details"
    return render_template("predict.html",title="Predict",form=form,output = message)


if __name__ == "__main__":
    app.run(debug=True)
