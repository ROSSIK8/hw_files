with open('1.txt', encoding='utf') as file_1, open('2.txt', encoding='utf') as file_2, \
        open('3.txt', encoding='utf') as file_3, open('1-3.txt', 'a', encoding='utf') as file_1_3:
    dict_files = {'1.txt': file_1.readlines(), '2.txt': file_2.readlines(), '3.txt': file_3.readlines()}
    all_files = sorted(dict_files, key=dict_files.get, reverse=True)
    for file in all_files:
        file_1_3.write(f'{file}\n')
        file_1_3.writelines(f'{len(dict_files[file])}\n')
        file_1_3.writelines(dict_files[file])
        file_1_3.write('\n')
