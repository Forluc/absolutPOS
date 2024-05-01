import requests


def save_response(data, session):
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSeW9h5sClsw1B7Mkum_Q7P6R5ewcGs1K5oCU9cSuhykTC51MA'
    print(data)
    form_data = {'entry.459099284': session['email'],
                 'entry.792996563': session['company'],
                 'entry.1944353173': session['address'],
                 'entry.1130494315': session['direction'],
                 'entry.65172522': data.get('Нужна ли поддержка в дальнейшем?'),
                 'entry.181497368': data.get('Нужна ли фурнитура?'),
                 'entry.723949198': data.get('Нужны ли сотрудники?'),
                 'entry.2039261159': data.get('Нужна ли охрана?'),
                 }
    user_agent = {'Referer': f'{url}/viewform',
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    requests.post(f'{url}/formResponse', data=form_data, headers=user_agent)
