import numpy as np
import math as m
import pandas as pd

def bin_array_creation(end_length):
    #generates random arrays of different length binary strings to test
    c = 4
    while c <= end_length:
        c_x = 0
        c_y = 0
        bin_str_arr = np.random.default_rng(42).random((int(1.12 ** c), c))
        while c_x < int(1.12 ** c):
            while c_y < c:
                if bin_str_arr[c_x, c_y] >= .5:
                    bin_str_arr[c_x, c_y] = 1
                else:
                    bin_str_arr[c_x, c_y] = 0
                c_y = c_y + 1
            c_y = 0
            c_x = c_x + 1
        print(bin_str_arr.shape)

        name = "bin_str_" + str(c)
        outfile = open("%s.npy" % name, "wb")
        np.save(outfile, bin_str_arr)
        outfile.close()
        c = c + 1

def rule_110():
    c_file = 4
    c_line = 0
    c_calc = 0
    while c_file <= 125:
        name = "bin_str_" + str(c_file)
        bin_str = np.load("%s.npy" % name)
        x, y = bin_str.shape
        calc_bin_str = np.zeros((x, y))

        while c_line < x:
            bin_str_line = np.squeeze(bin_str[c_line:c_line+1])
            calc_bin_str_line = np.squeeze(calc_bin_str[c_line:c_line+1])

            while c_calc < y:
                if c_calc == 0:
                    if (bin_str_line[0] == 0 and bin_str_line[1] == 0):
                        calc_bin_str_line[c_calc] = 0
                    else:
                        calc_bin_str_line[c_calc] = 1

                elif c_calc == (y-1):
                    if bin_str_line[y-1] == 0:
                        calc_bin_str_line[c_calc] = 0
                    else:
                        calc_bin_str_line[c_calc] = 1

                else:
                    if (bin_str_line[c_calc-1] == bin_str_line[c_calc] == bin_str_line[c_calc+1]) or (bin_str_line[c_calc-1] == 1 and  bin_str_line[c_calc] == 0 and bin_str_line[c_calc+1] == 0):
                        calc_bin_str_line[c_calc] = 0
                    else:
                        calc_bin_str_line[c_calc] = 1



                c_calc = c_calc + 1
            c_calc = 0
            c_line = c_line + 1

        name1 = "calc_bin_str_" + str(c_file)
        outfile = open("%s.npy" % name1, "wb")
        np.save(outfile, calc_bin_str)
        outfile.close()
        print(c_file)
        c_file = c_file + 1
        c_line = 0
