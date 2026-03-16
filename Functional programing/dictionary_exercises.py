from collections import defaultdict

transactions = [
    ("2026-01", "income", 2000),
    ("2026-01", "expense", 500),
    ("2026-02", "income", 2200),
    ("2026-02", "expense", 700),
]

summary = {}

for month, type_, amount in transactions:

    if month not in summary:
        summary[month] = {"income":0, "expense":0}

    summary[month][type_] += amount





def dict_converter(data):
    d = {}

    for person, skill in data:
        d[person] = d.get(person, []) + [skill]

    return d


data = [
("John", "python"),
("Anna", "java"),
("John", "sql"),
("Anna", "python"),
]


def dict_with_default(data):
    new_dict = defaultdict(list)

    for name , skill in data:
        new_dict[name].append(skill)

    return dict(new_dict)



transactions = [
("2026-01", "income", 2000),
("2026-01", "expense", 500),
("2026-02", "income", 2200),
("2026-02", "expense", 700),
("2026-02", "expense", 100)
]

def dict_converter2(transactions):

    d = {}

    for month, t_type, amount in transactions:

        if month not in d:
            d[month] = {"income": 0, "expense": 0}

        d[month][t_type] += amount

    for month in d:
        d[month]["balance"] = d[month]["income"] - d[month]["expense"]

    return d

data2 = [
("2026-01", 2000),
("2026-01", 500),
("2026-02", 2200),
("2026-02", 700)
]


def def_dict_converter(data):
    result = defaultdict(int)

    for month, amount in data:
        result[month]+=amount
    return dict(result)



text = "apple banana apple orange apple banana"

counter = defaultdict(int)

for word in text.split():
    counter[word] += 1

transactions2 = [
("food", 20),
("food", 15),
("rent", 500),
("food", 10),
("rent", 500)
]


def grouping_aggregations(transactions):
    result = defaultdict(int)

    for expense , amount in transactions:
        result[expense] += amount
    return dict(result)

squares = {x: x*x for x in range(5)}

#EX1 LIST TO DICT
numbers_1 = [1,2,3,4]
numbers_01 = {x: x * 2 for x in numbers_1}

#EX2 FILTERING
numbers_2 = [1,2,3,4,5,6]
numbers_02 = {x: x * x for x in numbers_2 if x % 2 == 0}

#EX3 TRANSFORM EXISTING DICT
prices = {
"apple": 1,
"banana": 2,
"orange": 3
}

def transform_existing_dicts(prices):
    return {product: price * 2 for product, price in prices.items()}

#EX4 (I USED HELP FROM GPT FOR THIS ONE )
transactions1 = [
("food", 20),
("rent", 500),
("food", 15)
]

def indexing(transactions):
    result = {index: transaction for index, transaction in enumerate(transactions)}

    return dict(result)




#EX5
months = ["2026-01","2026-02","2026-03"]

def fin_track_ext_dict(months):
    return {month: {"income": 0, "expense": 0} for month in months}






