def cal_avg(_filename):
    total_sum = 0
    number_of_lines = 0
    file_ = open(_filename,'r')

    while True:
        line_ = file_.readline()
        if line_ != None and line_ != "":
            total_sum += float(line_)
            number_of_lines += 1
        else:
            break

    avg = round(total_sum/number_of_lines,2)
    file_.close()

    return float(avg)