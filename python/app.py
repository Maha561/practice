
from flask import Flask, render_template, request, jsonify
app = Flask(__name__, template_folder='../')

# Step 1: Add some dummy soap data
soaps = [
    {"name": "Aloe Fresh", "skin_type": "Dry", "reviews": 15, "purchases": 50},
    {"name": "Charcoal Detox", "skin_type": "Oily", "reviews": 22, "purchases": 80},
    {"name": "Lavender Calm", "skin_type": "Sensitive", "reviews": 10, "purchases": 35},
    {"name": "Neem Clear", "skin_type": "Acne-prone", "reviews": 30, "purchases": 90}
]

# Step 2: Create a home route
@app.route('/')
def home():
    return render_template('product.html', soaps=soaps)

# Step 3: Route to sort soaps
@app.route('/sort', methods=['GET'])
def sort_soaps():
    sort_by = request.args.get('type')
    if sort_by == "reviews":
        sorted_list = sorted(soaps, key=lambda x: x["reviews"], reverse=True)
    elif sort_by == "purchases":
        sorted_list = sorted(soaps, key=lambda x: x["purchases"], reverse=True)
    else:
        sorted_list = soaps
    return jsonify(sorted_list)

if __name__ == '__main__':
    app.run(debug=True)
