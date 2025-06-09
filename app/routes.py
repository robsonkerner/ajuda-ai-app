from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@main.route("/painel-empresa")
def painel_empresa():
    return render_template("painel_empresa.html")

@main.route("/painel-faculdade")
def painel_faculdade():
    return render_template("painel_faculdade.html")

@main.route("/painel-publico")
def painel_publico():
    return render_template("painel_publico.html")

@main.route("/diagnostico")
def diagnostico():
    return render_template("diagnostico.html")

@main.route("/vagas")
def vagas():
    return render_template("vagas.html")

@main.route("/projetos")
def projetos():
    return render_template("projetos.html")

@main.route("/pesquisas")
def pesquisas():
    return render_template("pesquisas.html")

@main.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")

@main.route("/notificacoes")
def notificacoes():
    return render_template("notificacoes.html")

@main.route("/mensagens")
def mensagens():
    return render_template("mensagens.html")

@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@main.route("/relatorios")
def relatorios():
    return render_template("relatorios.html")

@main.route("/ajuda")
def ajuda():
    return render_template("ajuda.html")

@main.route("/sobre")
def sobre():
    return render_template("sobre.html")
