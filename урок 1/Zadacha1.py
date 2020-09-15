a = [1,2,3,4,5,6]
min_a=min(a)
max_a=max(a)
link_max = a.index(max_a)
link_min = a.index(min_a)
a[link_max] = min_a
a[link_min] = max_a
print(a)