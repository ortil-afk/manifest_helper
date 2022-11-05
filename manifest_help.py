import os

#find the files
direct = os.listdir()
files = []

#make a list of the files that are in the directory
for i, j in enumerate(direct):
    if j == 'manifest.txt' or j == 'manifest_help.py':
        continue
    else:
        files.append(j)

#header for the file
top = '''Filetype: Flipper Animation Manifest
Version: 1'''

#write to the file
with open("manifest.txt", "w+") as f:
    f.write(top + '\n')
    for i in files:
        manifest = f'''
Name: {i}
Min butthurt: 0
Max butthurt: 14
Min level: 1
Max level: 30
Weight: 7
'''
        f.write(manifest)
