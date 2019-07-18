# Code your functions here!

# 1. Write a function that checks to see if a given year is a leap year, by replacing "pass" with your own code, and returns either the boolean value True or False.

def is_leap_year(year):
    if year % 4 == 0:
        return True 
    else: 
        return False

print (is_leap_year(2015))


# 2. Write a function that takes in the current year and returns a string telling when the next leap year will be.
 
def current_year(year):
    if is_leap_year(year):
        return year + 4
    
# print is_leap_year(2000))

# 3. Write a function that takes in two years as arguments (a start_year and a last_year), and then prints out every single year between them that is a leap year. 

def in_between_years(start,end):
   for i in range(start,end):
    if i % 4 == 0: 
        print (i)
in_between_years(2000,2016)

# git status == check what needs to be updated 
# git add == add files to sync/upload to github

