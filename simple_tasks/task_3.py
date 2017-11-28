from operator import itemgetter


def handle_list_of_tuples(list):
    list.sort(key=itemgetter(3), reverse=True)
    list.sort(key=itemgetter(2), reverse=True)
    list.sort(key=itemgetter(1), reverse=True)
    list.sort(key=itemgetter(0))
    return list

