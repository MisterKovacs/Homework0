calls = 0
def count_calls():
    global calls
    print(calls)
def string_info(str_1):
    global calls
    tuple_1 = (len(str_1), str_1.upper(), str_1.lower())
    print(tuple_1)
    calls += 1
def is_contains(str_2, list_1):
    global calls
    print(str_2 in list_1)
    calls +=1

string_info('Ural Ramilevich Utyabaev')
is_contains('URAL', ['URAL', 'UTYABAEV', 'RAMILEVICH'])
string_info('Ural Utyabaev')
is_contains('JACK', ['CAPTAIN', 'SPARROW', 'JACK'])
string_info('Belaya beryoza pod moim oknom')
is_contains('RAMILEVICH', ['APPLE', 'BANANA', 'COCONUT'])
count_calls()