def vis_god(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        i = 'да'
    else:
        i = 'нет'
    return(i)
print(vis_god(1999))    
