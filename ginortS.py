
s = input()
def custom_sort_key(x):
    return (
        x.isdigit(),                      
        x.isdigit() and int(x) % 2 == 0,  
        x.isupper(),                      
        x.islower(),                     
        x                                 
    )
sorted_string = "".join(sorted(s, key=custom_sort_key))

print(sorted_string)
