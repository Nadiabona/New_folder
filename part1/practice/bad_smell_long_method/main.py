# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list():
    data = read_csv(csv)
    data = sort_data(data)
    return filter(data)

def read_csv(data):
    return [x.split(";") for x in data.split("\n")]

def sort_data(data):
    return sorted(data, key=lambda x: int(x[1]))

def filter(data):
    return [x for x in data if int(x[1]) > 10]

def get_user_list():
    pass


if __name__ == "__main__":
    print(get_users_list())

