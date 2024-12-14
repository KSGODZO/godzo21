from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Grade Calculator!"

@app.route('/calculate', methods=['POST'])
def calculate_grade():
    data = request.get_json()
    math_score = data.get('math_score')
    science_score = data.get('science_score')
    english_score = data.get('english_score')

    total_score = math_score + science_score + english_score
    average_score = total_score / 3

    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"

    return jsonify({
        'total_score': total_score,
        'average_score': average_score,
        'grade': grade
    })

if __name__ == '__main__':
    app.run(debug=True)
