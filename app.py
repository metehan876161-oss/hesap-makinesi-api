from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hesap Makinesi API Çalışıyor"

@app.route('/hesapla', methods=['POST'])
def hesapla():
    try:
        data = request.get_json()
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        choice = data['choice']

        if choice == '+':
            result = num1 + num2
        elif choice == '-':
            result = num1 - num2
        elif choice == '*':
            result = num1 * num2
        elif choice == '/':
            if num2 == 0:
                return jsonify({'error': 'Sıfıra bölünemez'})
            result = num1 / num2
        else:
            return jsonify({'error': 'Geçersiz işlem'})

        return jsonify({'sonuç': result})
    except Exception as e:
        return jsonify({'error': str(e)})
