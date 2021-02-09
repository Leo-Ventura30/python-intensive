def enviar_email(nome_loja, tabela):
    server = smtplib.SMTP('smtp.gmail.com:587')
    corpo_email = f"""
      <p>Prezados, </p>
      <p>Segue relatorio de vendas</p>
      <a href={nome_loja}>{tabela.to_html()}</a>
    """

    msg = email.message.Message()
    msg['Subject'] = f"Relatorio de vendas {nome_loja}"

    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = 'leohabbo1998@gmail.com'
    msg['To'] = 'leonardofventura98@gmail.com'
    password = "2585963741l"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# enviar_email("Diretoria", table_billings)
