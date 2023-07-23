from utils import *


def main():
    print('Привет! Это программа для поиска вакансий на сайтах HeadHunter и SuperJob')
    search_name = input('Введите поисковый запрос: ')
    hh = HeadHunterAPI()
    sj = SuperJobAPI()
    json_saver = JSONSaver()
    hh.get_vacancies(search_name)
    sj.get_vacancies(search_name)
    Vacancy.instantiate_from_json()

    salary = int(input('Введите начальный порог зарплаты: '))

    num = 0
    filtered_vacancies = []
    for vacancy in Vacancy.all:
        if vacancy.salary_from >= salary:
            filtered_vacancies.append(vacancy.as_dict())
            num += 1
            print(
                f'{num}. Название вакансии: {vacancy.name}\n'
                f'Название компании: {vacancy.employer}\n'
                f'Зарплата: от {vacancy.salary_from} до {vacancy.salary_to} рублей.'
            )
            print()

    print('Вакансии сохранены в файл saved_vacancies.json')

    json_saver.add_vacancy(filtered_vacancies)


if __name__ == '__main__':
    main()
