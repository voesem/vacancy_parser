import requests
import json
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, vacancy_name):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для получения вакансий с сайта HeadHunter по заданному имени вакансии
    """

    def get_vacancies(self, vacancy_name, page=0):
        """
        Метод для работы с API HeadHunter

        :param vacancy_name: на вход поисковой запрос вакансии
        :param page: номер страницы поиска (по умолчанию первая страница)

        Метод записывает полученные данные в json-файл
        """

        params = {
            'text': f'NAME:{vacancy_name}',
            'area': 1,
            'page': page,
            'only_with_salary': True
        }

        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()

        vacancies = json.loads(data)

        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies['items'], f, ensure_ascii=False, indent=4)
