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
                filtered_vacancies.append(vacancy)
                num += 1
                print(
                    f'{num}. Название вакансии: {vacancy.name}\n'
                    f'Название компании: {vacancy.employer}\n'
                    f'Зарплата: от {vacancy.salary_from} до {vacancy.salary_to} рублей.'
                )
                print()

        chosen_num = int(input('Введите порядковый номер вакансии, о которой хотите узнать подробнее:\n'))
        chosen_vacancy = filtered_vacancies[chosen_num - 1]
        print(chosen_vacancy)

        saved_vacancy = input('Сохранить вакансию?\n1 - Да\n2 - Нет\n')

        if saved_vacancy == '1':
            json_saver.add_vacancy(chosen_vacancy.as_dict())

    elif platform_name == '2':
        pass
    else:
        print('Неизвестная команда')


if __name__ == '__main__':
    main()
