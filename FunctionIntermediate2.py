x = [ [5,2,3], [10,8,9] ] 
print("before :" ,x)
x[1][0]=15
print("After :" , x)
# # ------------------------------------------------------------------------------------

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print("Before :" ,students)
for i in range(0,len(students)):
    if students[i]['last_name'] == 'Jordan':
        students[i]['last_name']  = 'Bryan'

        
print("After : " , students)
# # ------------------------------------------------------------------------------------
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print("Before :" ,sports_directory)
for i in range(0, len(sports_directory['soccer'])):
        if sports_directory['soccer'][i] == 'Messi':
             sports_directory['soccer'][i] = 'Andres'

print("After : " ,sports_directory)
# # ------------------------------------------------------------------------------------

z = [ {'x': 10, 'y': 20} ]
print("Before :" ,z)
z[0]['y']=30
print("After : " ,z)

# ---------------------------------------------------------------------------------
# Create a function iterateDictionary(some_list) that, given a list of dictionaries,
#  the function loops through each dictionary in the list and prints each key and the 
# associated value. For example, given the following list:
# first_name - Michael, last_name - Jordan
studentsB = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print("--------------------------------------------------------------")
def iterateDictionary(arr):
    for i in range(len(arr)):
           print("first_name - ", arr[i]['first_name'],", last_name -",arr[i]['last_name'])

iterateDictionary(studentsB) 

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
#  the function prints the value stored in that key for each dictionary.
#  For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
print("--------------------------------------------------------------")
def iterateDictionary2(first_name , studentsB):
    for i in range(len(studentsB)):
          print(studentsB[i]['first_name'])
iterateDictionary2('first-name',studentsB)
print("--------------------------------------------------------------")
def iterateDictionary3(last_name , studentsB):
    for i in range(len(studentsB)):
        print(studentsB[i]['last_name'])
iterateDictionary3('last-name' , studentsB)
print("--------------------------------------------------------------")
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated 
# values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(arr):
    for key ,value in arr.items():
            print('\n',len(value),key ,'\n')
            for i in range(0,len(value)):
                print(value[i])

printInfo(dojo)





