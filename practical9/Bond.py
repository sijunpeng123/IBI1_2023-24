def favourite_bond(year_of_birth):
    aged_18 = year_of_birth + 18
    if 1973<aged_18<=1986:
        actor= 'Roger_Moore'
    elif 1986<aged_18<=1994:
        actor= 'Timothy	Dalton'
    elif 1994<aged_18<=2005:
        actor= 'Pierce	Brosnan'
    elif 2005<aged_18<=2021:
        actor= 'Daniel	Craig'
    else :
        actor = 'Unknown'
    print ('Favourite Bond actormight be', actor)
    return actor
birth_year = 1990
favorite = favourite_bond(birth_year)