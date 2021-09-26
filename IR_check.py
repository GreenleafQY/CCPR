import numpy as np
from PIL import Image
import csv
import copy


def Shu_data_extract(num):

    list_data = []
    j_index = 0
    a = []
    c = []
    d = []
    e = []

    index_a = 0
    index_b = 0
    index_c = 0

    #1.读取csv数据
    with open("./check/image_to_data/shu_{}.csv".format(num), "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            list_data.append(row)

    #2.提取a/b点(竖的最宽处左右）下标值
    for i in list_data:
        if i[-1] != "0 " and i[-1] != "0":
            a = copy.deepcopy(i)
            index_ab = list_data.index(a)
            break
        else:
            pass

    x_index = []
    for i in range(len(a)):
        if a[i] in a[:i]:
            x_index.append(x_index[-1] + 1)
        else:
            x_index.append(a.index(a[i]))

    index_b = x_index[-1]

    for i in a:
        if i != "0" and i != "0 ":
            index_a = a.index(i)
            break

    index_ab_mid = (index_b-index_a)/2

    #3.提取c点(竖的底部中点，倒数2、3、4行均值）下标值
    c = list_data[-2]
    d = list_data[-3]
    e = list_data[-4]
    index_c = list_data.index(c)

    index_c_1 = 0
    index_c_2 = 0
    index_d_1 = 0
    index_d_2 = 0
    index_e_1 = 0
    index_e_2 = 0

    for i in c:
        if i != "0" and i != "0 ":
            index_c_1 = c.index(i)
            break

    for i in c:
        if i != "0" and i != "0 ":
            index_c_2 = c.index(i)

    index_c_cal_1 = (index_c_1 + index_c_2)/2

    for i in d:
        if i != "0" and i != "0 ":
            index_d_1 = d.index(i)
            break

    for i in d:
        if i != "0" and i != "0 ":
            index_d_2 = d.index(i)

    index_c_cal_2 = (index_d_1 + index_d_2) / 2

    for i in e:
        if i != "0" and i != "0 ":
            index_e_1 = e.index(i)
            break

    for i in e:
        if i != "0" and i != "0 ":
            index_e_2 = e.index(i)

    index_c_cal_3 = (index_e_1 + index_e_2) / 2

    index_c_mid = (index_c_cal_1 + index_c_cal_2 + index_c_cal_3) / 3

    #计算最终比值（竖高/ab在水平线上的投影与c点的距离）
    height = index_c - index_ab
    shade_point = index_ab_mid - index_c_mid

    if shade_point != 0:
        mark_1_shu = height/shade_point
    elif shade_point == 0:
        mark_1_shu = 0

    # print("h", height)
    # print("p", shade_point)
    # print("m1", mark_1_shu)

    return height, shade_point, mark_1_shu

def Pool_shu_extract():
    height_list = []
    shade_point_list = []
    mark_1_shu_list = []

    mark_1_shu_sum = 0
    mark_1_shu_expect = 0

    for num in range(1,6):
        height, shade_point, mark_1_shu = Shu_data_extract(num)
        height_list.append(height)
        shade_point_list.append(shade_point)
        mark_1_shu_list.append(mark_1_shu)

    for i in mark_1_shu_list:
        mark_1_shu_sum += i

    mark_1_shu_expect = mark_1_shu_sum/20

    with open("./check/result/shu_result.csv", "w", newline='', encoding='UTF-8') as d:
        content = csv.writer(d)
        content.writerow(height_list)
        content.writerow(shade_point_list)
        content.writerow(mark_1_shu_list)
        content.writerow([mark_1_shu_expect])

def Kuan_data_extract():

    kuan_data = []
    xi_data = []
    count_j = 0
    count_data = []
    max_data = 0
    max_min_ratio = 0

    #1.读取最宽笔画数据
    with open("./check/image_to_data/kuan_1.csv", "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            kuan_data.append(row)

    # 2.读取最窄笔画数据
    with open("./check/image_to_data/kuan_2.csv", "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            xi_data.append(row)

    #print(kuan_data)
    #print(xi_data)

    #3.提取最宽值
    for i in kuan_data:
        if i[0] == "0" or i[0] == "0 ":
            for j in range(1, len(i)):
                if i[j] != "0" and i[j] != "0 ":
                    count_j += 1
            count_data.append(count_j)
            count_j = 0

    max_data = max(count_data)

    count_k = 0
    count_xi_data = []

    # 4.提取最窄值
    for i in xi_data:
        if i[0] == "0" or i[0] == "0 ":
            for j in range(1, len(i)):
                if i[j] != "0" and i[j] != "0 ":
                    count_k += 1
            count_xi_data.append(count_k)
            count_k = 0

    #print("count_xi_data", count_xi_data)

    min_data = min(count_xi_data)

    max_min_ratio = max_data/min_data

    # print("max_data", max_data)
    # print("min_data", min_data)
    # print("max_min_ratio", max_min_ratio)

    with open("./check/result/kuan_result.csv", "w", newline='', encoding='UTF-8') as d:
        content = csv.writer(d)
        #content.writerow(["kuan", "xi", "max_min_ratio"])
        content.writerow([max_data])
        content.writerow([min_data])
        content.writerow([max_min_ratio])

    return max_data, min_data, max_min_ratio

def Na_data_extract(num):
    na_list = []
    a = ""
    b = ""
    index_a = 0
    index_b = 0

    length = 0
    height = 0
    na_ratio = 0

    #1.读取csv数据
    with open("./check/image_to_data/na_{}.csv".format(num), "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            na_list.append(row)

    #print("na_list", na_list)
    index_i = 0
    lowest_point = 0

    #2.提取最低值
    for i in na_list[-1]:
        index_i = na_list[-1].index(i)
        if i != "0 " and i != "0" and i[-1] != "":
            a = copy.deepcopy(i)
            index_a = na_list[-1].index(i)
            break

    for i in na_list[-1]:
        index_i = na_list[-1].index(i)
        if i != "0 " and i != "0" and i[-1] != "":
            b = copy.deepcopy(i)
            if (na_list[-1][index_i + 1] and  na_list[-1][index_i + 1] == b) and (na_list[-1][index_i + 2] and na_list[-1][index_i + 2]== b):
                index_b = index_i + 2
            else:
                index_b = index_i

    # print("a",a)
    # print('b', b)
    # print("index_a", index_a)
    # print("index_b", index_b)
    lowest_point = int(round((index_b + index_a)/2, 0))

    #print("lowest_point", lowest_point)

    index_right_top = 0
    index_right_bottom = 0

    # 3.提取最右值
    for i in na_list:
        index_i = na_list.index(i)
        if i[-1] != "0 " and i[-1] != "0" and i[-1] != "":
            index_right_top = index_i
            break

    for i in na_list:
        index_i = na_list.index(i)
        if i[-1] != "0 " and i[-1] != "0" and i[-1] != "":
            index_right_bottom = index_i

    right_point = int(round((index_right_top + index_right_bottom)/2,0))

    #print("right_point", right_point)

    #4.计算宽度特征值
    length = len(na_list[-1]) - lowest_point
    height = len(na_list) - right_point

    na_ratio = round(height/length, 2)

    return na_ratio

def Pool_na_extract():

    low_ratio_list = []
    right_ratio_list = []
    sum_low_ratio = 0
    sum_right_ratio = 0
    na_ratio_list = []
    sum_na_ratio = 0
    expected_na_ratio = 0

    for num in range(1, 6):
        na_ratio = Na_data_extract(num)
        na_ratio_list.append(na_ratio)
        sum_na_ratio += na_ratio

    expected_na_ratio = round(sum_na_ratio/5, 2)

    with open("./check/result/na_result.csv", "w", newline='', encoding='UTF-8') as d:
        content = csv.writer(d)
        content.writerow(na_ratio_list)
        content.writerow([expected_na_ratio])

def Zhe_data_extract(num):

    zhe_list = []

    # 1.读取csv数据
    with open("./check/image_to_data/zhe_{}.csv".format(num), "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            zhe_list.append(row)

    #print("zhe_list", zhe_list)

    index_i = 0
    left_a = 0
    left_b = 0
    tan_left_ratio = 0

    right_a = 0
    right_b = 0
    tan_right_ratio = 0
    right_b_list = []

    # 2.提取左侧夹角Tan值
    for i in zhe_list[0]:
        index_i = zhe_list[0].index(i)
        if i != "0 " and i != "0" and i != "":
            a = copy.deepcopy(i)
            left_a = zhe_list[0].index(i)
            break

    #print("left_a", left_a)

    for i in zhe_list:
        index_i = zhe_list.index(i)
        if i[0] != "0 " and i[0] != "0" and i[0] != "":
            b = copy.deepcopy(i[0])
            left_b = zhe_list.index(i)
            break

    #print("left_b", left_b)

    tan_left_ratio = round(left_b/left_a, 2)

    #print("tan_left_ratio", tan_left_ratio)

    # 3.提取右侧夹角Tan值
    for i in zhe_list[0]:
        index_i = zhe_list[0].index(i)
        if i != "0 " and i != "0" and i != "":
            right_a = zhe_list[0].index(i)

    #print("right_a", right_a)

    right_value = 0

    for k in range(0, 10):
        for i in zhe_list[k]:
            index_i = zhe_list[k].index(i)
            if i != "0 " and i != "0" and i != "":
                right_value = zhe_list[k].index(i)
        right_b_list.append([right_value, k])

    #print("right_b_list", right_b_list)

    right_b_list_1 = copy.deepcopy(right_b_list)
    for i in right_b_list:
        for j in right_b_list_1:
            if i[0] > j[0]:
                right_b_list_1.remove(j)
            elif i[0] == j[0] and i[1] < j[1]:
                right_b_list_1.remove(j)

    right_b = right_b_list_1[0][1]

    #print("right_b", right_b)

    tan_right_ratio = round(right_b/right_a, 2)

    #print("tan_right_ratio", tan_right_ratio)

    return tan_left_ratio, tan_right_ratio

def Pool_zhe_extract():

    tan_left_list = []
    tan_right_list = []
    sum_left_ratio = 0
    sum_right_ratio = 0

    for num in range(1, 6):
        tan_left_ratio, tan_right_ratio = Zhe_data_extract(num)
        tan_left_list.append(tan_left_ratio)
        tan_right_list.append(tan_right_ratio)
        sum_left_ratio += tan_left_ratio
        sum_right_ratio += tan_right_ratio

    expected_tan_left_ratio = round(sum_left_ratio / 5, 2)
    expected_tan_right_ratio = round(sum_right_ratio / 5, 2)

    #print("expected_tan_left_ratio", expected_tan_left_ratio)
    #print("expected_tan_right_ratio", expected_tan_right_ratio)

    with open("./check/result/zhe_result.csv", "w", newline='', encoding='UTF-8') as d:
        content = csv.writer(d)
        # content.writerow(["tan_left_ratio_list", "expected_tan_left_ratio"])
        content.writerow(tan_left_list)
        content.writerow([expected_tan_left_ratio])
        # content.writerow(["tan_right_ratio_list", "expected_tan_right_ratio"])
        content.writerow(tan_right_list)
        content.writerow([expected_tan_right_ratio])

def Check_if_somebody(writer):

    shu_data = []
    shu_check = []
    na_data = []
    na_check = []
    zhe_data = []
    zhe_check = []
    kuan_data = []
    kuan_check = []

    shu_check_float = []
    shu_data_float = []
    probability_shu = 1
    probability_shu_cal = 0

    na_check_float = []
    na_left_check_float = []
    na_right_check_float = []
    na_data_float = []
    na_left_data_float = []
    na_right_data_float = []
    probability_na = 1
    probability_na_left = 0
    probability_na_right = 0
    probability_na_cal = 0

    zhe_check_float = []
    zhe_left_check_float = []
    zhe_right_check_float = []
    zhe_data_float = []
    zhe_left_data_float = []
    zhe_right_data_float = []
    probability_zhe = 1
    probability_zhe_left = 0
    probability_zhe_right = 0
    probability_zhe_left_right = 0

    kuan_check_float = []
    kuan_data_float = []
    probability_kuan = 1

    probability = 0

    #1. 导入数据库
    #(1)竖
    with open("./check/database/{}_shu_result.csv".format(writer), "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            shu_data.append(row)

    #print("shu_data", shu_data)

    with open("./check/result/shu_result.csv", "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            shu_check.append(row)

    #print("shu_check", shu_check)

    for i in shu_check[2]:
        i_f = float(i)
        shu_check_float.append(i_f)

    shu_check_max = max(shu_check_float)
    #print("max", shu_check_max)
    shu_check_min = min(shu_check_float)
    #print("min", shu_check_min)

    for i in shu_data[2]:
        i_f = float(i)
        shu_data_float.append(i_f)

    shu_data_max = max(shu_data_float)
    shu_data_min = min(shu_data_float)

    # if shu_check_max <= shu_data_max and shu_check_min >= shu_data_min:
    #     probability_shu = 1
    # else:
    #     probability_shu = 0.75

    if float(shu_check[3][0])/float(shu_data[3][0]) > 0:
        probability_shu_cal = 1-abs(float(shu_check[3][0])-float(shu_data[3][0]))/abs(float(shu_data[3][0]))

    probability_shu *= probability_shu_cal

    # print("probability_shu", probability_shu)
    # print("probability_shu_cal", probability_shu_cal)

    #2. 捺
    with open("./check/database/{}_na_result.csv".format(writer), "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            na_data.append(row)

    #print("na_data", na_data)

    with open("./check/result/na_result.csv", "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            na_check.append(row)

    #print("na_check", na_check)

    for i in na_check[0]:
        i_f = float(i)
        na_check_float.append(i_f)

    na_check_max = max(na_check_float)
    na_check_min = min(na_check_float)

    for i in na_data[0]:
        i_f = float(i)
        na_data_float.append(i_f)

    na_data_max = max(na_data_float)
    na_data_min = min(na_data_float)

    # if na_check_max <= na_data_max and na_check_min >= na_data_min:
    #     probability_na = 1
    # else:
    #     probability_na = 0.75

    probability_na_cal = 1 - abs(float(na_check[1][0]) - float(na_data[1][0])) / abs(float(na_data[1][0]))

    probability_na *= probability_na_cal

    # print("probability_na", probability_na)
    # print("probability_na_cal", probability_na_cal)

    #3.折
    with open("./check/database/{}_zhe_result.csv".format(writer), "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            zhe_data.append(row)

    #print("zhe_data", zhe_data)

    with open("./check/result/zhe_result.csv", "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            zhe_check.append(row)

    #print("zhe_check", zhe_check)

    for i in zhe_check[0]:
        i_f = float(i)
        zhe_left_check_float.append(i_f)

    zhe_left_check_max = max(zhe_left_check_float)
    zhe_left_check_min = min(zhe_left_check_float)

    for i in zhe_data[0]:
        i_f = float(i)
        zhe_left_data_float.append(i_f)

    zhe_left_data_max = max(zhe_left_data_float)
    zhe_left_data_min = min(zhe_left_data_float)

    for i in zhe_check[2]:
        i_f = float(i)
        zhe_right_check_float.append(i_f)

    zhe_right_check_max = max(zhe_right_check_float)
    zhe_right_check_min = min(zhe_right_check_float)

    for i in zhe_data[2]:
        i_f = float(i)
        zhe_right_data_float.append(i_f)

    zhe_right_data_max = max(zhe_right_data_float)
    zhe_right_data_min = min(zhe_right_data_float)

    # if zhe_left_check_max <= zhe_left_data_max and zhe_left_check_min >= zhe_left_data_min and zhe_right_check_max <= zhe_right_data_max and zhe_right_check_min >= zhe_right_data_min:
    #     probability_zhe = 1
    # else:
    #     probability_zhe = 0.75

    if float(zhe_check[1][0])/float(zhe_data[1][0]) > 0:
        probability_zhe_left = 1-abs(float(zhe_check[1][0])-float(zhe_data[1][0]))/abs(float(zhe_data[1][0]))
    if float(zhe_check[3][0]) / float(zhe_data[3][0]) > 0:
        probability_zhe_right = 1 - abs(float(zhe_check[3][0]) - float(zhe_data[3][0])) / abs(float(zhe_data[3][0]))

    probability_zhe_left_right =  (probability_zhe_left + probability_zhe_right)/2

    probability_zhe *= probability_zhe_left_right

    # print("probability_zhe", probability_zhe)
    # print("probability_zhe_left_right", probability_zhe_left_right)

    #4. 宽窄
    with open("./check/database/{}_kuan_result.csv".format(writer), "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            kuan_data.append(row)

    # print("kuan_data", kuan_data)

    with open("./check/result/kuan_result.csv", "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            kuan_check.append(row)

    # print("kuan_check", kuan_check)

    probability_kuan = 1 - abs(float(kuan_check[2][0]) - float(kuan_data[2][0])) / abs(float(kuan_data[2][0]))

    # print("probability_kuan", probability_kuan)

    #5. 汇总概率

    if probability_shu >0 and probability_na >0 and probability_zhe >0 and probability_kuan >0:
        probability = (probability_shu + probability_na + probability_zhe + probability_kuan)/4
    elif probability_shu <=0 or probability_na <=0 or probability_zhe <=0 or probability_kuan <=0:
        probability = 0

    # print("probability", probability)

    return probability

def Check_similarity():

    list_data = []
    shu_check = []

    #1. 提取竖的数据
    for name in ["zy", "wxz", "xianzhi", "yzq", "csl", "ysn", "lgq", "oyx", "ss", "mf", "htj", "zj", "zmf", "nz", "dqc",
                 "wzm", "dsr", "qg"]:
        with open("./check/database/{}_shu_result.csv".format(name), "r", newline='', encoding='GBK') as d:
            content = csv.reader(d)
            for i, rows in enumerate(content):
                if i == 3:
                    row = rows
                    list_data.append([name, row[0]])

    #print("list_data", list_data)

    famous = 0
    similarity_ratio = 0
    similarity_list = []

    #2. 对比竖的数据，找出最接近的三人
    with open("./check/result/shu_result.csv", "r", newline='', encoding='GBK') as d:
        content = csv.reader(d)
        for row in content:
            shu_check.append(row)

    # print("shu_check", shu_check)

    for i in list_data:
        famous = float(i[1])
        similarity_ratio = float(shu_check[3][0])/famous
        similarity_list.append(similarity_ratio)

    similarity_list_1 = copy.deepcopy(similarity_list)

    for i in similarity_list_1:
        if i > 1 or i <0:
            similarity_list.remove(i)

    # print("similarity_list", similarity_list)

    similarity_list = sorted(similarity_list, reverse=True)

    # print("similarity_list", similarity_list)

    first_ratio = similarity_list[0]
    second_ratio = similarity_list[1]
    third_ratio = similarity_list[2]

    # print("first_ratio", first_ratio)
    # print("s_ratio", second_ratio)
    # print("t_ratio", third_ratio)

    for i in list_data:
        if float(shu_check[3][0])/float(i[1]) == first_ratio:
            first_name = i[0]
        elif float(shu_check[3][0])/float(i[1]) == second_ratio:
            second_name = i[0]
        elif float(shu_check[3][0])/float(i[1]) == third_ratio:
            third_name = i[0]

    First_similarity_probability = Check_if_somebody(first_name)
    Second_similarity_probability = Check_if_somebody(second_name)
    Third_similarity_probability = Check_if_somebody(third_name)

    return first_name, First_similarity_probability, second_name, Second_similarity_probability, third_name, Third_similarity_probability

if __name__ == "__main__":

    #1. 提取数据
    Pool_shu_extract()
    Kuan_data_extract()
    Pool_na_extract()
    Pool_zhe_extract()

    #2. 检测是否某人作品
    probability = Check_if_somebody("ysn")
    print("probability_by_this_person", probability)

    #3. 检测与某人相似度
    first_name, First_similarity_probability, second_name, Second_similarity_probability, third_name, Third_similarity_probability = Check_similarity()
    print("Name:similarity", first_name, First_similarity_probability)
    print("Name:similarity", second_name, Second_similarity_probability)
    print("Name:similarity", third_name, Third_similarity_probability)








