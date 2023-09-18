# встроенные функции
# map, filter, reduce
# lambda
# num_1 = lambda a, b: a ** b


# def my_num(str_1):
#     return lambda str_2: str_1 + " " + str_2
#
#
# # a = my_num("Tabyldieva")
# # print(a("Nazgul"))
# lists = [2, 3, 45, 5, 6]

# new_list = map(lambda a: a ** 2, lists)
# print(list(new_list))

# phone_numbers = ["+996555443322", "+996550473322", "+996551443922"]
#
#
# def replace_start_char(number: str) -> str:
#     new_number = number.replace("+996", "0")
#     return new_number
#
#
# new_numbers = list(map(replace_start_char, phone_numbers))
# # print(new_numbers)
#
# # filter
#
# nums = list(range(1, 16))
#
# print(nums)
#
#
# def chetnoe_chislo(num):
#     if num % 2 == 0:
#         return num
#
#
# new_nums = list(filter(chetnoe_chislo, nums))
# print(new_nums)

students = [
    {
        "name": "Test",
        "kpi": [77, 73, 55],
        "age": 20,
    },
    {
        "name": "Test1",
        "kpi": [77, 90, 100],
        "age": 17,
    },
    {
        "name": "Test2",
        "kpi": [10, 100, 5],
        "age": 43,
    },
]


def filter_student(student: dict) -> dict:
    average = sum(student["kpi"]) / len(student["kpi"])
    if 18 < student["age"] < 45 and average > 63:
        student['kpi'] = average
        return student


filtered_st = list(filter(filter_student, students))
print(filtered_st)
