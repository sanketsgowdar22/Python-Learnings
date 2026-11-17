# Count the occurrence of each character. 

sen = input("Enter the word:")

for chr in sen:
    if chr not in sen[:sen.index(chr)]:
        print(chr,"=",sen.count(chr))
        

# for i in sen:
#     count = 0
#     for j in sen:
#         if i == j:
#             count += 1
#     print(i,count)
