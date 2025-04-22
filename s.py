from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template with a form
html_form = '''
<!doctype html>
<title>Addition App</title>
<h2>Add Two Numbers</h2>
<form method="post">
  Number 1: <input type="number" name="num1"><br><br>
  Number 2: <input type="number" name="num2"><br><br>
  <input type="submit" value="Add">
</form>
{% if result is not none %}
  <h3>Result: {{ result }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def add():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except (ValueError, KeyError):
            result = "Invalid inputtt!"
    return render_template_string(html_form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
