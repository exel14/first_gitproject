my_dict = dict(Russia = 'Moscow',student = ['Danil','Erjan','Baistan','Alina'])
second_dict = {1:'lala',2:'3lalal'}
my_dict['coller'] = 'water'

search = 'Russia'

if search in my_dict:
    del my_dict[search]
print(my_dict,second_dict)