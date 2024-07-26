from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf_file' not in request.files:
        return "Nenhum arquivo PDF enviado!"
    
    file = request.files['pdf_file']
    if file.filename == '':
        return "Nenhum arquivo selecionado!"
    
    if file and file.filename.endswith('.pdf'):
        # Salva o arquivo ou faz o processamento necessário
        return "Arquivo recebido com sucesso!"
    else:
        return "Apenas arquivos PDF são permitidos!"