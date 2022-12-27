# Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

list_mixed = ['1', 'a', 'b', '2', '3', 'c']
a = list(filter(lambda x: x.isdigit(), list_mixed))
c = list(filter(lambda x: x.isalpha(), list_mixed))
print(a)
print(c)