
Python Written Test	
 
Question1
Use python lists and make an list of numbers.
Write a function which returns sum of the list of numbers


solution -
 n = map(int,input().split()) 
lst = sum(n)
print (lst)



Question2 
Setup a dict structure like this in python
Dict1: (this is a key, value pair of user id and username)
{
   “1” : “name1”,
   “2” : “name2”,
   “3” : “name3”
} etc.. 
Dict2: (this is a key value pair of user id and exam score) 
{
   “1” : 50,
   “2” : 60
   “3” : 70
}
These are just sample data assume there are hundreds of users 

Write a function in python in python, which will return maximum i.e function should return dictionary like
{
  “3” : 70
}

sol :
1.dict1 = dict([input().split()])
print (dict1)


another type solution :
dict1 = {}
dict1 = {'1':['name1'],
         '2': ['name2'],
         '3': ['name3']}
for each_row in zip(*([i] + (j) 
                      for i, j in dict1.items())):
      print(*each_row, " ")dict1 = {}

solution 3 :
dict1 = {
   '1' : 50,
   '2' : 60,
   '3' : 70
}
print (max(dict1.items()))


Question 3
Assume we have list like this
[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
Basically a list of zero’s and one’s.
Write a python function to the number of maximum consecutive  one’s present in the array. 
E.g output for the above array would be 4

solution - 
lst = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
n = len(lst)
def getMaxLength(lst, n):
    count = 0 
    result = 0 
    for i in range(0, n):
        if (lst[i] == 0):
            count = 0
        else:
            count+= 1 
            result = max(result, count) 
    return result 
print(getMaxLength(lst, n))    

Question 4
Design a mysql database. Requirements are as follows 
We have two entities “candidate” and “test_score”
candidate has properties name, email address
Every candidate has to give 3 tests like “first_round”, “second_round” , “third_round” and scoring for every test is done out of 10. 
CREATE TABLE candidate(
          id INT ,
          name varchar(50),
          email varchar (50)
          );

CREATE TABLE test_score(
         id INT,
         name varchar(50),
         first_round INT(10),
         second_round INT(10)
         third_round INT(10)

         );






Now using flask/django, need to create rest api to do the following
Insert a candidate into database
Assign score for a candidate based on the test
Api to get highest scoring candidate and average scores per round for all candidates

Next,
Write a route in flask or django GET, POST route to save a user, login a user, add/update address for that user.

