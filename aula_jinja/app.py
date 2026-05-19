from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    pagina = "Página incial"
    return render_template('index.html', inicial=pagina)

@app.route('/questao1')
def mensagem():
    nome = "Sofie"
    pag = "Questão 1"
    return render_template('questao1.html', nome=nome, pagina=pag)

@app.route('/questao2')
def dados():
    dados = [
        {"nome": "Sofie Cirino", "idade": 18},
        {"nome": "Luciene Almeida", "idade": 27},
        {"nome": "Pedro Soares", "idade": 12},
        {"nome": "Júlio Cesar", "idade": 80}
        ]
    return render_template('questao2.html', dados=dados)

@app.route('/questao3')
def usuario():
    usuario = [
        {"nome": "Ana", "email": "ana@email.com"}
        ]
    return render_template('questao3.html', usuario=usuario)

@app.route('/questao4')
def nomes():
    nomes = [ "Ana Clara", "Bernado", "Cauã", "Davi"]
    return render_template('questao4.html', alunos=nomes)

@app.route('/questao5')
def alunos():
    lista_alunos = [
        {"nome": "Ana Clara", "nota": 9},
        {"nome": "Bernado", "nota": 4},
        {"nome": "Cauã", "nota": 6},
        {"nome": "Davi", "nota": 7}
    ]
    return render_template('questao5.html', alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)