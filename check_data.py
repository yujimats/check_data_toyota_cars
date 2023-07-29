import os

def check_data():
    path_input = os.path.join('dataset')
    list_dir = [f for f in os.listdir(path_input) if os.path.isdir(os.path.join(path_input, f))]

    path_save = os.path.join('output', 'dataset_toyota_cars.csv')
    with open(path_save, 'w') as logfile:
        logfile.write('dir_name,file_count\n')
    for dir in list_dir:
        path = os.path.join(path_input, dir)
        list_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        with open(path_save, 'a') as logfile:
            logfile.write('{},{}\n'.format(dir, len(list_files)))

if __name__=='__main__':
    check_data()