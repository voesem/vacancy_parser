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

        :param vacancy_name: на вход подается поисковой запрос вакансии
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


class Vacancy:
    """
    Класс для работы с вакансиями, инициализирующийся по
    названию вакансии, ссылке, требованиям, ответственности, нижней и верхней границ зарплаты
    """
    all = []

    def __init__(self, name, url, requirement, responsibility, salary_from, salary_to):
        self.name = name
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary_from = salary_from
        self.salary_to = salary_to

        Vacancy.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.url}", ' \
               f'"{self.requirement}", "{self.responsibility}", "{self.salary_from}", "{self.salary_to}")'

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        return self.salary_to < other.salary_to

    @classmethod
    def instantiate_from_json(cls):
        """
        Класс-метод, инициализирующий экземпляры класса из созданного классом HeadHunterAPI json-файла
        :return:
        """
        with open('vacancies.json', encoding='utf-8') as f:
            text = json.load(f)
            for vacancy in text:
                cls(
                    name=vacancy['name'],
                    url=vacancy['alternate_url'],
                    requirement=vacancy['snippet']['requirement'],
                    responsibility=vacancy['snippet']['responsibility'],
                    salary_from=vacancy["salary"]["from"],
                    salary_to=vacancy["salary"]["to"]
                )
