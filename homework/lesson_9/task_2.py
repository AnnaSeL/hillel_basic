"""Function for partly hiding the email with '*' """
def replace(email):
    data = email.split('@')
    name = data[0]
    mail = data[1]
    parts = mail.split('.')
    parts[0] = '***'
    if len(name) < 3:
        hidden = name[0] + '**'
    else:
        hidden = name[:2] + '***'
    result = hidden + '@' + '.'.join(parts)
    return result


email = input("Enter your email: ")
res = replace(email)
print(res)

