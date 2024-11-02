from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/modify_text',methods=['POST'])
def modify_text():
    data = request.get_json()
    extracted_text = data.get('text')

    modified_text = extracted_text.upper()

    return jsonify({'text': modified_text})

if __name__ == '__main__':
    app.run(debug=True)
