#tuple values
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

#Access the value at index -3
valueminus3 = year[-3]
print(f"Value at index -3: {valueminus3}")

#Reverse the tuple and print the original tuple and reversed tuple
reversedyear = tuple(reversed(year))
print(f"\nOriginal Tuple: {year}")
print(f"Reversed Tuple: {reversedyear}")

#Count number of times 2009 is in the tuple (use count() method)
count2009 = year.count(2009)
print(f"\nNumber of times 2009 is in the tuple: {count2009}")

#Get the index value of 2018(Use index method)
index2018 = year.index(2018)
print(f"\nIndex value of 2018: {index2018}")

#Find length of given tuple(Use len() method)
tuplelength = len(year)
print(f"\nLength of the tuple: {tuplelength}")