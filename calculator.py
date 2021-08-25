def get_length_of_data(_filename):
    lod = 0
    file_ = open(_filename, 'r')
    while True:
        line_ = file_.readline()
        if line_ != None and line_ != "":
            lod += 1
        else:
            break
    return lod


def calculate_avg(_filename):
    total_sum = 0
    number_of_lines = get_length_of_data(_filename)
    file_ = open(_filename, 'r')
    for i in range(number_of_lines):
        total_sum += float(file_.readline())
    avg = round(total_sum / number_of_lines, 2)
    file_.close()

    return float(avg)


def repack(_filename_to_repack, _repack_frame_size):
    sum_ = 0
    file_res_initialize = open("repacked_" + str(_filename_to_repack), 'w')
    file_res_initialize.close()
    file_to_repack_length = get_length_of_data(_filename_to_repack)
    max_iter = int(file_to_repack_length / _repack_frame_size)
    file_to_repack_ = open(_filename_to_repack, 'r')
    file_res_ = open("repacked_" + str(_filename_to_repack), 'a+')
    for i in range(max_iter):
        for j in range(_repack_frame_size):
            sum_ += float(file_to_repack_.readline())
        repacked_data = round(float(sum_ / _repack_frame_size), 2)
        file_res_.write(str(repacked_data) + "\n")
        sum_ = 0

    return None

