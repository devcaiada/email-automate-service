import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
import mysql.connector

# Conecte-se ao banco de dados
db_connection = mysql.connector.connect(
    host='seu_host',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)

# Execute a consulta SQL para obter os dados dos clientes
query = "SELECT nome, email FROM clientes"
df = pd.read_sql(query, db_connection)

# Função para enviar o email
def enviar_email(nome, email_destino):
    # Configuração do servidor de email
    smtp_host = 'smtp.seudominio.com'
    smtp_port = 587
    smtp_user = 'seu_email@seudominio.com'
    smtp_password = 'sua_senha'

    # Criação do corpo do email
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = email_destino
    msg['Subject'] = 'Assunto do Email'

    # Corpo do texto
    corpo = f'Olá {nome},\n\nEste é um email automático com uma imagem da nossa empresa.\n\nAtenciosamente,\nSua Empresa'
    msg.attach(MIMEText(corpo, 'plain'))

    # Anexar imagem
    with open('caminho/para/sua/imagem.jpg', 'rb') as imagem:
        img = MIMEImage(imagem.read())
        img.add_header('Content-Disposition', 'attachment', filename='imagem.jpg')
        msg.attach(img)

    # Enviar email
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, email_destino, msg.as_string())
            print(f'Email enviado para {email_destino}')
    except Exception as e:
        print(f'Erro ao enviar email para {email_destino}: {e}')

# Enviar email para cada cliente no banco de dados
for index, row in df.iterrows():
    enviar_email(row['nome'], row['email'])
