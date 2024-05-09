from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

# Serve the HTML page
@app.route('/')
def index():
    return render_template('Questionnaire.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    # Process the data as needed
    print(data)
    return jsonify({'message': 'Data received successfully!'})


if __name__ == '__main__':
    app.run(debug=True)





