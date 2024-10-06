from _datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    file = open(name,'r')
    while True:
        lines = file.readline()
        all_data.append(lines)
        if not lines :
            break
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# линейный вызов функции

# start_process = datetime.now()
# for name in filenames:
#     read_info(name)
# end_process = datetime.now()
# print(end_process - start_process)

# многопроцессорный вызов функции
if __name__ == '__main__':
    start_process = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_process = datetime.now()
    print(end_process - start_process)