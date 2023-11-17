from data.data import Color, Person, Date
import random

from faker import Faker

faker_en = Faker('En')


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(18, 99),
        salary=random.randint(10000, 20000),
        department=faker_en.job(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        mobile=faker_en.msisdn()
    )


def generated_file():
    path = rf'G:\\Python\\PycharmProjects\\selenium\\selenium_auto_qa_portfolio_project\\filetest{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0,999)}')
    file.close()
    return file.name, path


def generated_subject():
    subject_list = ['Maths', 'Chemistry', 'Computer Science', 'Commerce', 'Economics', 'Hindi',
                    'Biology', 'Physics', 'Accounting', 'Arts', 'Social Studies', 'History', 'Civics', 'English']
    return subject_list[random.randint(0, 13)]


def generated_color():
    yield Color(color_name=["Red", "Blue", "Green", "Yellow", "Purple",
                            "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"])

    # return color_name[random.randint(0, 10)]


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='12:00',

    )
