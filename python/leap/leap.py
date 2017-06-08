#leap year question 2 exercism#

def is_leap_year(year):
    is_div_by = lambda x,y : x%y
    return (is_div_by(year,4) == 0 and not is_div_by(year,100) == 0) or is_div_by(year,400) == 0
                                                
    
