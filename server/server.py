from flask import Flask,jsonify,request
import util
app = Flask(__name__)

@app.route("/get_location_names")
def hello():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-control-allow-origin',"*")
    return response
@app.route("/predict_home_price",methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.predict_price(location,total_sqft,bhk,bath)

    })

    response.headers.add('Access-control-allow-origin',"*")
    return response

if __name__ == "__main__":
    util.load_art_data()
    app.run()