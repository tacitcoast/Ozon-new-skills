# В приложении к уроку дан список имен животных animals.
# С помощью map трансформируйте его в список, в котором лежат длины строк имен животных.
# Например animals = ['питон', 'питон', ... ] трансформируется в [5, 5, ...].
# Проделайте эту же операцию с помощью list comprehension. Напечатайте результаты.

animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф', 'леопард', 'жираф', 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит',
'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф', 'собака', 'собака', 'кит', 'питон', 'леопард', 'кошка', 'жираф', 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит', 'леопард', 'леопард', 'горилла',
'горилла', 'кит']

# Трансформируем список с помощью map
result = list(map(lambda x: len(x), animals))
print(result)

# Трансформируем список с помощью list comprehension
print([len(x) for x in animals])