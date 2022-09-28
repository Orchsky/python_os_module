import os 


#print(list(os.walk("/Users/bakhtiyarhuseynov/Documents/Orchsky-course-materials/python-for-devops/python_os_walk/")))

# for dir,path,fileid in list(os.walk("/Users/bakhtiyarhuseynov/Documents/Orchsky-course-materials/python-for-devops/python_os_walk/")):
#     # print(dir)
#     # print(path)
#     for file in fileid:
#         print(os.path.join(dir, file))


'''
[('/Users/bakhtiyarhuseynov/Documents/Orchsky-course-materials/python-for-devops/python_os_walk/', 
['python'], ['2.txt', '1.txt']), ('/Users/bakhtiyarhuseynov/Documents/Orchsky-course-materials/python-for-devops/python_os_walk/python', [],
 ['os.py'])]

1. Direpath 
2. dirname 
3. file within that path

'''


a = "4"
print(type(a))