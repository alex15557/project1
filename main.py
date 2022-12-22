# This is a sample Python script.
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method =='POST':
        number1 = request.form['number1']
        number2 = request.form['number2']
        znak = request.form['znak']

    if znak=="+":
        result = int(number1)+int(number2)
    elif znak=="-":
        result = int(number1)-int(number2)
    elif znak == "*":
        result = int(number1) * int(number2)
    elif znak == "/":
        result = int(number1) / int(number2)
    return render_template('index.html', num1 = number1, num2 = number2, zn = znak, res = result)

@app.route("/create_new_contact/", methods=['GET','POST'])
def create_new_contact():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method =='POST':
        input_name = request.form['name']
        input_status = request.form['status']
        input_phone = request.form['phone']
        with open('main_base.csv', 'a+') as f:
            f.write(f'{input_name};{input_status};{input_phone};\n')
        return render_template('form.html')

@app.route("/contacts/")
def contacts():
    context = {"Имя":[], "Статус":[], "Номер":[]}
    with open('main_base.csv', 'r') as csvfile:
        text = csv.reader(csvfile, delimiter=';')
        for row in text:
            context["Имя"].append(row[0])
            context["Статус"].append(row[1])
            context["Номер"].append(row[2])
    return render_template('contacts.html', context_names = context["Имя"], context_status = context["Статус"], context_phone = context["Номер"], num = len(context["Имя"]))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5001)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
