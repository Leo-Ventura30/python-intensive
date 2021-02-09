import smtplib
import email.message


def enviar_email(nome_loja, tabela):
    server = smtplib.SMTP('smtp.gmail.com:587')
    corpo_email = """
      body mail
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"

    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = 'remetente'
    msg['To'] = 'destinatario'
    password = "senha do email"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# enviar_email("Diretoria", table_billings)
