import os

a = os.getcwd()
print(a)
print(os.listdir())
os.rename('./test_folder', './new_folder')
print(os.listdir())
