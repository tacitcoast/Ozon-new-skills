# Вользите алгоритм пузырьковой сортировки из лекции.
# Модифицируйте его так, чтобы сортировка производилась не по возрастанию, а по убыванию.
# Отсортируйте список [19,2,31,45,6,11,121,27]

new_list = [19,2,31,45,6,11,121,27]

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

bubble_sort(new_list)
print(new_list)
