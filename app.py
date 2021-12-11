from flask import Flask, request, render_template
import pickle

model = pickle.load(open("RandomForestRegressor.pkl","rb"))
app = Flask(__name__,template_folder="template") # Creation of Flask Application

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    '''
    For Rendering Results from on HTML GUI
    '''
    if request.method == "POST":
         mass_npea = float (request.form.get('mass_npea'))
         size_npear = float (request.form.get('size_npear'))
         malign_ratio = float (request.form.get('malign_ratio'))
         damage_size = float (request.form.get('damage_size'))
         exposed_area = float (request.form.get('exposed_area'))
         std_dev_malign = float (request.form.get('stddevmalign'))
         err_malign = float (request.form.get('err_malign'))
         malign_penalty = float (request.form.get('malign_penalty'))
         damage_ratio = float (request.form.get('damage_ratio'))
         # Input Features
         input_features = [[mass_npea,size_npear,malign_ratio,damage_size,
                            exposed_area,std_dev_malign,err_malign,
                            malign_penalty,damage_ratio]]
         # Making Predicition
         prediction = model.predict(input_features)
         result = prediction[0]
         result_format = "{:.2f}".format(result)
    
    return render_template('index.html',prediction_result=result_format)

if __name__ == "__main__":
    app.run(debug=True)