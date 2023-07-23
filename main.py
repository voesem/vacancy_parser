from utils import *


def main():
    print('Привет! Это программа для поиска вакансий на сайтах HeadHunter и SuperJob')
    platform_name = input('Выберите платформу:\n1 - HeadHunter\n2 - SuperJob\n')
    search_name = input('Введите поисковый запрос: ')
    if platform_name == '1':
        hh = HeadHunterAPI()
        json_saver = JSONSaver()
        hh.get_vacancies(search_name)
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

        json_saver.add_vacancy(filtered_vacancies)
    elif platform_name == '2':
        pass
    else:
        print('Неизвестная команда')


if __name__ == '__main__':
    main()
