from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate_field():
    data = request.get_json()
    field_name = data.get('field_name')
    value = data.get('value')
    
    # Simulación de validación para cada campo
    patrones_validados = {
        "telefono": r"^\d{10}$",
        "correo": r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,4}$",
        "curp": r"^[A-Z]{1}[AEIOU]{1}[A-Z]{2}\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])[HM]{1}[A-Z]{2}[BCDFGHJKLMNÑPQRSTVWXYZ]{3}[0-9A-Z]{2}$",
        "rfc": r"(^[A-Z]{4}\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])[A-Z0-9]{3}$)|(^[A-Z]{3}\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])[A-Z0-9]{3}$)",
        "ipv4": r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$",
        "fecha": r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{2}$",
    }

    import re
    valid = bool(re.match(patrones_validados.get(field_name, ""), value))

    return jsonify({"valid": valid})

if __name__ == '__main__':
    app.run(debug=True)
