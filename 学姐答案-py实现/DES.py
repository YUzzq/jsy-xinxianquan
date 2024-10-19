# 定义所有的表
import random

IP_Table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
# 初置换
IPR_Table = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
# 逆初始置换
E_Table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
# E表
P_Table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
           2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
# 置换选择
PC1_Table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
# 置换选择1
PC2_Table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
             23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
# 置换选择2
LOOP_Table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
# 密钥位移（左移次数）
S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
      0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
      4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
      15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
      3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
      0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
      13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
      13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
      13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
      1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
      13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
      10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
      3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
      14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
      4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
      11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
      10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
      9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
      4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
      13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
      1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
      6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
      1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
      7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
      2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
S = [S1, S2, S3, S4, S5, S6, S7, S8]


def displace(matrix, x):
    reslut_x = [0 for i in range(len(matrix))]
    for i in range(len(matrix)):
        reslut_x[i] = x[matrix[i] - 1]
    return reslut_x


def zuo(x):  # 循环左移
    reslut_x = [0 for i in range(len(x))]
    reslut_x[-1] = x[0]
    for i in range(len(x) - 1):
        reslut_x[i] = x[i + 1]
    return reslut_x


def Exclusive_or(a, b):
    reslut_a = [0 for i in range(len(a))]
    for i in range(len(a)):
        if a[i] == b[i]:
            reslut_a[i] = 0
        else:
            reslut_a[i] = 1
    return reslut_a


def bcd_to_binary(bcd_string):  # 10bcd - 2
    binary_list = []
    duiyin = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, }
    for digit in bcd_string:
        if digit in duiyin.keys():
            bcd_digit = duiyin[digit]
        else:
            bcd_digit = int(digit)
        binary_digit = format(bcd_digit, '04b')
        binary_list.extend(map(int, binary_digit))

    return binary_list


def bcd_to_16(num):
    string_16 = ''
    for i in range(int(len(num) / 4)):
        ten = num[i * 4] * 8 + num[(i * 4) + 1] * 4 + num[(i * 4) + 2] * 2 + num[(i * 4) + 3] * 1
        string_16 += hex(ten)[2:]
    return string_16


def get_k(matri1, matri2, x):
    # print("origin", x)
    x1 = displace(matri1, x)
    # print("newkey", x1)
    k = [[] for i in range(16)]
    c0 = x1[:28]
    d0 = x1[28:]
    for i in range(16):
        all = []
        for j in range(LOOP_Table[i]):
            ci = zuo(c0)
            di = zuo(d0)
            c0 = ci
            d0 = di
        # print("ci", i, ci)
        # print("di", i, di)
        all.extend(ci)
        all.extend(di)
        k[i] = displace(matri2, all)
        # print("K[i]", i, k[i])
    return k


def s_replace(matrix, x):
    row = x[0] * 2 + x[-1] * 1
    col = (x[1] * 8 + x[2] * 4 + x[3] * 2 + x[4] * 1)
    num = matrix[row * 16 + col]
    # print("num", num)
    if num > 9:
        return [int(i) for i in str(bin(num)[2:])]
    else:
        return bcd_to_binary(str(num))


def f_func(r, key):
    s_result = []
    r_e = displace(E_Table, r)
    reslut = Exclusive_or(r_e, key)
    for i in range(8):
        s_result.extend(s_replace(S[i], reslut[i * 6:(i + 1) * 6]))
    # print("s_result", s_result)
    # print(displace(P_Table, s_result))
    return displace(P_Table, s_result)


def eeeeee_coder(input_m, input_key, IP_Table, PC1_Table, PC2_Table, IPR_Table, model):
    m = input_m
    k = bcd_to_binary(input_key)
    if model != 'group':
        m = bcd_to_binary(input_m)
    after_ip_x = displace(IP_Table, m)
    L0 = after_ip_x[:32]
    R0 = after_ip_x[32:]
    key_16 = get_k(PC1_Table, PC2_Table, k)
    Ri = R0
    Li = L0
    # print("key_16", key_16)
    for i in range(16):
        Li_1 = Li
        Li = Ri
        RI_1 = Ri
        Ri = Exclusive_or(Li_1, f_func(RI_1, key_16[i]))
    m_ = []
    m_.extend(Ri)
    m_.extend(Li)
    c = displace(IPR_Table, m_)
    print("密文:", bcd_to_16(c).upper())
    return c, key_16, bcd_to_16(c).upper()
    # return Li, Ri, key_16, bcd_to_16(c).upper()


def dddddd_coder(c, key_16, model):
    c = displace(IP_Table, c)
    Li = c[32:]
    Ri = c[:32]
    for i in range(15, -1, -1):
        Ri_1 = Li  # 15 16
        Li_1 = Exclusive_or(Ri, f_func(Li, key_16[i]))
        Li = Li_1  # 16 15
        Ri = Ri_1
    m_ = []
    m_.extend(Li)
    m_.extend(Ri)
    c = displace(IPR_Table, m_)
    print("明文:", bcd_to_16(c).upper())
    if model == 'group':
        return c
    else:
        return bcd_to_16(c).upper()


def des():
    while 1:
        input_c = str(input("请输入明文:")).upper()
        input_key = str(input("请输入密钥:")).upper()
        if len(input_c) != 16 or len(input_key) != 16:
            print("明文/密钥必须是16位(16进制)")
        else:
            break
    c, key_16, m = eeeeee_coder(input_c, input_key, IP_Table, PC1_Table, PC2_Table, IPR_Table, 'des')
    c = dddddd_coder(c, key_16, 'des')
    return c


def three_des_eeeeee_coder(input_c, input_key_1, input_key_2, input_key_3, model):
    # k3加密
    m, key_1, m_1 = eeeeee_coder(input_c, input_key_3, IP_Table, PC1_Table, PC2_Table, IPR_Table, model)
    # k2解密
    key_2 = get_k(PC1_Table, PC2_Table, bcd_to_binary(input_key_2))
    c = dddddd_coder(m, key_2, model)
    # k1加密
    m, key_1, m_2 = eeeeee_coder(c, input_key_1, IP_Table, PC1_Table, PC2_Table, IPR_Table, model)
    print("3_des密文:", m_2)
    return m, m_2


def three_des_dddddd_coder(m, input_key_1, input_key_2, input_key_3, model):
    # k1解密
    key_1 = get_k(PC1_Table, PC2_Table, bcd_to_binary(input_key_1))
    c_1 = dddddd_coder(m, key_1, model)
    # k2加密
    m, key_1, m_1 = eeeeee_coder(c_1, input_key_2, IP_Table, PC1_Table, PC2_Table, IPR_Table, model)
    # k3解密
    key_3 = get_k(PC1_Table, PC2_Table, bcd_to_binary(input_key_3))
    c_2 = dddddd_coder(m, key_3, model)
    c = [bcd_to_16(i).upper() for i in [c_2]]
    print("解码3des密码明文:", c[0])
    return c_2


def three_des():
    # 加密 k3加密 k2解密 k1加密
    while 1:
        input_c = str(input("请输入明文:")).upper()
        input_key_1 = str(input("请输入密钥k1:")).upper()
        input_key_2 = str(input("请输入密钥k2:")).upper()
        input_key_3 = str(input("请输入密钥k3:")).upper()
        if len(input_c) != 16 or len(input_key_1) != 16 or len(input_key_2) != 16 or len(input_key_3) != 16:
            print("明文/密钥必须是16位(16进制)")
        else:
            break
    c, m = three_des_eeeeee_coder(input_c, input_key_1, input_key_2, input_key_3, 'three_des')
    c = three_des_dddddd_coder(c, input_key_1, input_key_2, input_key_3, 'three_des')
    return c


def group_eeeeee_coder(key, iv, c_group, model):
    ini_c = Exclusive_or(c_group, iv)
    c, ini_iv = three_des_eeeeee_coder(ini_c, key[0], key[1], key[2], model)
    print("分组密码密文:", ini_iv)
    return c


def group_dddddd_coder(group, key, iv, model):
    c_group = [Exclusive_or(three_des_dddddd_coder(group, key[0], key[1], key[2], model), iv)]
    c = [bcd_to_16(i).upper() for i in c_group]
    c_finaly = ''
    for i in c:
        c_finaly += i
    print("解码分组密码明文:", c_finaly)
    return c_finaly


def group():
    # 0000000000000000
    # 1111111111111111
    # 1234123412341234
    # 0100110001011001
    while 1:
        input_c = '12341234123412341234123412341234E68891E788B1796D'  # str(input("请输入明文:")).upper()
        input_key_1 = '0100110001011001'  # str(input("请输入密钥k1:")).upper()
        input_key_2 = '0000000000000000'  # str(input("请输入密钥k2:")).upper()
        input_key_3 = '0000000000000000'  # str(input("请输入密钥k3:")).upper()
        input_group = 1  # int(input("请输入分组数:"))
        # input_iv = '0100110001011001' # str(input("请输入初始随机向量:")).upper()
        if len(input_c) % 16 != 0 or len(input_key_1) != 16 or len(input_key_2) != 16 or len(input_key_3) != 16:
            print("初始随机向量/密钥必须是16位(16进制)||分组明文必须是16位(16进制)")
        else:
            break
    c_group = []
    dee_c = []
    for i in range(int(len(input_c) / 16)):
        c_group.append(bcd_to_binary(input_c[i * 16:(i + 1) * 16]))
    input_iv = random.choices(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'], k=16)
    input_iv = bcd_to_binary(input_iv)
    for i in range(len(c_group)):
        print("分组密码明文:", input_c[i * 16:(i + 1) * 16])
        c = group_eeeeee_coder([input_key_1, input_key_2, input_key_3], input_iv, c_group[i], 'group')
        dee_c.append(group_dddddd_coder(c, [input_key_1, input_key_2, input_key_3], input_iv, 'group'))

    return dee_c


def read_file(file_path):
    data = []
    with open(file_path, 'rb') as file:
        while True:
            binary_data = file.read(8)
            if not binary_data:
                break  # 读取结束
            hex_data = ''.join(format(byte, '02x') for byte in binary_data)
            hex_data = hex_data.upper()
            data.append(hex_data)
    if len(data[-1]) < 16:
        num = 16 - len(data[-1])
        for i in range(num - 1):
            data[-1] = data[-1] + '0'
        data[-1] = data[-1] + str(int(num / 2))
    elif len(data[-1]) == 16:
        data.append('0000000000000008')
    return data


def file_eeeeee_coder():
    file_path = 'test.png'  # str(input("请输入文件路径:"))
    while 1:
        input_key_1 = '0100110001011001'  # str(input("请输入密钥k1:")).upper()
        input_key_2 = '0000000000000000'  # str(input("请输入密钥k2:")).upper()
        input_key_3 = '0000000000000000'  # str(input("请输入密钥k3:")).upper()
        input_group = 1  # int(input("请输入分组数:"))
        if len(input_key_1) != 16 or len(input_key_2) != 16 or len(input_key_3) != 16:
            print("分组明文必须是16位(16进制)")
        else:
            break
    data = read_file(file_path)
    secret_data = []
    input_iv = random.choices(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
                              k=16)
    input_iv = bcd_to_binary(input_iv)
    for data_8 in data:
        c_input = (bcd_to_binary(data_8))
        print("分组密码输入明文:", data_8)
        c = group_eeeeee_coder([input_key_1, input_key_2, input_key_3], input_iv, c_input, 'group')
        c_16 = [bcd_to_16(i).upper() for i in [c]]
        secret_data.append(c_16)
    with open('密文.txt', 'w') as f:
        for i in secret_data:
            for j in i:
                f.write(str(j))
            f.write('\n')
    return '密文.txt', [input_key_1, input_key_2, input_key_3], input_iv


def file_dddddd_coder(file_path, key, input_iv):
    data = []
    with open(file_path, 'r') as f:
        for i in f.readlines():
            data.append(i.strip())
    no_secret_data = []
    for c in data:
        c = bcd_to_binary(c)
        c_group = group_dddddd_coder(c, key, input_iv, 'group')
        no_secret_data.append(c_group)
    no_secret_data[-1] = no_secret_data[-1][:len(no_secret_data[-1]) - (int(no_secret_data[-1][-1]) * 2)]
    output_file_path = '解码.png'
    with open(output_file_path, 'wb') as output_file:
        for hex_data in no_secret_data:
            binary_data = bytes.fromhex(hex_data)
            output_file.write(binary_data)


def file():
    path, [input_key_1, input_key_2, input_key_3], input_iv = file_eeeeee_coder()
    file_dddddd_coder(path, [input_key_1, input_key_2, input_key_3], input_iv)


if __name__ == "__main__":
    file() # 测试文件
    # group() # 测试分组
    # three_des() #测试3des
    # des() # 测试des
# 0000000000000000
# 1111111111111111
# 1234123412341234
# 0100110001011001
