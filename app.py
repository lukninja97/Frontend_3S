from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'senai_terapia_sp'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/funcionarios')
def funcionarios():
    return render_template("funcionarios.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash("Preencha o campo para realizar a soma", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrai = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subt=subtrai)

    return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/geometria/triangulo/area', methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            area = ((n1 * n1) * (3 ** 0.5)) / 4
            return render_template("geometria.html", area=round(area, 2))
        else:
            flash("Preencha o campo", 'alert-danger')
            return render_template("geometria.html")
    return render_template("geometria.html")

@app.route('/geometria/triangulo/perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            perimetro = n1 * 3
            return render_template("geometria.html", perimetro=perimetro)
    return render_template("geometria.html")

@app.route('/funcionarios', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        if request.form['form-nome']:
            flash(f"nome {request.form['form-nome']}", 'alert-success')

        return render_template("funcionarios.html")
    return render_template("funcionarios.html")

#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)