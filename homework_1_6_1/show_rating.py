def find_shows (shows_dic, show_genre):
    list_genre = []
    for key, value in shows_dic.items():
        if value == show_genre:
            list_genre.append(key)

    return list_genre


def calc_avg_rating (ratings_dic, list_genre):
    sum_rating = 0
    count = 0
    for i in list_genre:
        sum_rating += ratings_dic[i]
        count += 1

    avg_rating = sum_rating / count
    return avg_rating

