if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_arr = set(arr)
    print(unique_arr)
    unique_arr_list = list(unique_arr)
    unique_arr_list.sort(reverse=True)
    print(unique_arr_list[1])
    

    #print(unique_arr_list)
    #print(unique_arr_list.sort(reverse=True)[1])
    #print (print(sorted(set(arr), reverse=True)[1]))