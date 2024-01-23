from matplotlib import pyplot as pt


def create_demand_chart():
    dictt = {}
    lists = dictt.items()
    h, v = zip(*lists)

    pt.figure(figsize=(12, 6))
    pt.bar(h, v)
    pt.title("Динамика количества вакансий для выбранной профессии")
    pt.xlabel("Год")
    pt.xticks(h)
    pt.ylabel("Количество вакансий")
    pt.grid()
    pt.savefig('charts/demand_4.png')


def create_geography_salary_chart():
    dictt = {}
    pt.figure(figsize=(12, 6))
    pt.barh(list(dictt.keys()), list(dictt.values()), color='purple')
    pt.title("Уровень зарплат по городам")
    pt.xlabel("Уровень зарплат")
    pt.grid(True, axis='x')
    pt.gca().invert_yaxis()
    pt.savefig('charts/geography_3.png')


def create_geography_vacancy_chart():
    dictt = {}
    colors = ['purple', 'blue', 'springgreen', 'orange', 'tomato', 'darkgreen', 'yellow', 'lime', 'royalblue',
              'slateblue', 'darkred', 'gold', "khaki", "navy", "hotpink", "darkgoldenrod"]

    pt.figure(figsize=(10, 5))
    pt.pie(list(dictt.values()), colors=colors)
    pt.legend(dictt.keys(), bbox_to_anchor=(-0.1, 1.))
    pt.title("Доля вакансий по городам для выбранной профессии")
    pt.savefig('charts/geography_2.png')


def create_skills_chart():
    dictt = {}
    for year in dictt:
        h = dictt[year][0]
        v = dictt[year][1]
        pt.figure(figsize=(20, 6))
        pt.barh(h, v)
        pt.title(f"ТОП-20 навыков за {year}")
        pt.xlabel("Частотность")
        pt.grid(True, axis='x')
        pt.gca().invert_yaxis()
        pt.savefig(f'charts/skills_{year}.png')


if __name__ == '__main__':
    create_skills_chart()
