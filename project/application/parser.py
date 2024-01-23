import requests
import re


class Parser:
    @staticmethod
    def vacancies():
        params = {
            'text': 'ios',
            'period': '1',
            'search_field': 'name'
        }

        resp = requests.get('https://api.hh.ru/vacancies', params=params)
        return resp.json()

    @staticmethod
    def vacancy_info(vacancy_id: str):
        resp = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}')
        return resp.json()

    def parse(self):
        vacancies_list = []
        counter = 0
        for vacancy in self.vacancies()['items']:
            if counter == 10:
                break
            data = self.vacancy_info(vacancy['id'])

            name = data['name']

            skills = ''
            for skill in data['key_skills']:
                skills += f"{skill['name']}, "
            skills = skills[:-2]

            try:
                salary = data['salary']['from']
                currency = data['salary']['currency']
            except TypeError:
                salary = 'Не указано'
                currency = ''

            if salary is None:
                salary = 'Не указано'
                currency = ''

            if skills == '':
                skills = 'Не указано'

            region = data['area']['name']

            template = re.compile('<.*?>')
            description = re.sub(template, '', data['description'])
            template = re.compile('&.*?;')
            description = re.sub(template, '', description)

            company_name = data['employer']['name']

            date_published = data['published_at'].split('T')[0]

            vacancies_list.append(
                {
                    'name': name,
                    'desc': description,
                    'skills': skills,
                    'company': company_name,
                    'price': f"{salary} {currency}",
                    'region': region,
                    'date_published': date_published
                }
            )
            counter += 1
        return vacancies_list
