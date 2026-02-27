numbers = [1, 2, 3, 4, 5, 6]

result = list(map(lambda n: n * n, numbers ))

result_filter = list(filter(lambda n: n > 10, numbers))

result_map_filter = list(filter(lambda n: n % 2 == 0,  map(lambda n: n * n , numbers)))




names = ["Anna", "Ivan", "Mira"]
scores = [90, 85, 100]


result_zip = list(
    map(
        lambda pair: (lambda x, y: f"{x}: {y}")(*pair),
        zip(names, scores)
    )
)

#LIST COMPREHENSION
result_comp = [f"{name}: {score}" for name, score in zip(names, scores)]


nums = [1, 2, 3, 4]
nums_result_map = list(map(lambda n: n * 10, nums))
nums_result_comps = [num * 10 for num  in nums]

words = ["hi", "python", "ok"]
words_map = list(map(lambda c: len(c), words ))
words_comp = [len(word) for word in words]

prices = [19.99, 5, 3.5]
prices_map = list(map(lambda price: str(price) ,prices ))
prices_comp = [str(price) for price in prices]

nums_filter = [1, 2, 3, 4, 5, 6]
nums_filter_map = list(filter(lambda n: n % 2 ==0 , nums_filter))
nums_filter_camp = [n  for n in nums_filter if n % 2 == 0]

nums_f2 = [-3, -1, 0, 2, 5]
nums_filter_f2 = list(filter(lambda  n: n > 0 , nums_f2))
nums_filter_f2_comp = [n for n in nums_f2 if n > 0]


words_f3 = ["car", "", "  ", "house", "a"]
words_f3_filter = list(filter(lambda  word: word.strip(), words_f3))
words_f3_filter_comp = [ word for word in words_f3 if len(word.strip()) > 0]


values = [0, 1, "", "hello", None, False, True]
values_result = list(filter(None ,values))
print(values_result)

