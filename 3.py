with open('1.txt', encoding='utf') as file_1, open('2.txt', encoding='utf') as file_2, open('3.txt', encoding='utf') as file_3:
    dict_files = {'1.txt': file_1.readlines(), '2.txt': file_2.readlines(), '3.txt': file_3.readlines()}
    all_files = sorted(dict_files, key=dict_files.get, reverse=True)
    for index_file in range(len(all_files)):
        print(all_files[index_file])
        print(index_file + 1)
        print(*dict_files[all_files[index_file]])