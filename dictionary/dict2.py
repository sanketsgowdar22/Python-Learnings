# ls = [("name","Sanket"),("age",34),("marks",64),(54,"marks2")]

# for k,v in ls:
#     print(k,"---",v)

# dic = {"name":{"S1","S2"}}
# print(dic.values())

students = {"Student1":{"name":"Sanket","Age":22},"Student2":{"name":"Rakshi","Age":23}}

for key,value in students.items():
    print(key,"-->",value)
    for k , v in value.items():
        print(k,"-->",v)
