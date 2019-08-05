from flask import Flask, request, render_template, url_for, redirect
from forms import SearchForm
from neural_net import model, scale_l, format_data
import tensorflow as tf

app = Flask(__name__)
app.secret_key = 'secret'

nn = model()
graph = tf.get_default_graph()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)


@app.route("/price-prediction", methods=["GET", "POST"])
def price():
    form = SearchForm()
    zip = request.form["zip"]
    city = request.form["city"]
    sqft = request.form["sqft"]
    beds = request.form["beds"]
    baths = request.form["baths"]
    levels = request.form["levels"]
    lotsize = request.form["lotsize"]
    age = request.form["age"]
    remarks = request.form["remarks"]
    proptype = request.form["proptype"]
    data = format_data(zip, age, sqft, city,
                       beds, baths, levels, lotsize,
                       remarks, proptype)
    global graph
    with graph.as_default():
        pred = str(scale_l.inverse_transform(nn.predict(data))[0][0])
        return render_template('price.html', predicted_price = pred)


if __name__ == "__main__":
    app.run(debut=True)