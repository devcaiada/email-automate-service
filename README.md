# Envio Automático de Emails com Python

Este repositório contém um script Python para enviar emails automaticamente para clientes. O corpo do email contém texto e uma imagem anexada, e o código extrai os nomes e emails dos clientes de um banco de dados SQL.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `smtplib`
  - `email`
  - `pandas`
  - `mysql-connector-python` (ou qualquer outra biblioteca adequada para acessar seu banco de dados SQL)

Você pode instalar as bibliotecas necessárias usando o comando:
```bash
pip install pandas mysql-connector-python
```

## Configuração do Banco de Dados

Certifique-se de que o banco de dados SQL está configurado corretamente e que a tabela de clientes contém pelo menos duas colunas: ``nome`` e ``email``.

## Configuração do Script

Atualize o script com suas próprias informações:

### Conexão com o Banco de Dados:

~~~python
db_connection = mysql.connector.connect(
    host='seu_host',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
~~~

### Configuração do Servidor de Email:

~~~python
smtp_host = 'smtp.seudominio.com'
smtp_port = 587
smtp_user = 'seu_email@seudominio.com'
smtp_password = 'sua_senha'
~~~

### Caminho da Imagem:

~~~python
with open('caminho/para/sua/imagem.jpg', 'rb') as imagem:
~~~

## Código

Aqui está o script Python completo:

~~~python
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
~~~

## Como Usar

1. Atualize as configurações no script com suas próprias informações.

2. Execute o script para enviar emails automaticamente para os clientes listados no banco de dados.

## Contribuições <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" />

Contribuições são bem-vindas! Siga as instruções abaixo:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Faça o commit das alterações: `git commit -m 'Minha nova feature'`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um Pull Request.

---
