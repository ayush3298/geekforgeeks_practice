#https://practice.geeksforgeeks.org/problems/most-frequent-word-in-an-array-of-strings/0
def most_freq_word_in_array(str_arr):
    str_arr.sort()
    s2 = []
    for i in str_arr:
        s2.append(str_arr.count(i))
    return str_arr[s2.index(max(s2))]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        str_arr = [i for i in input().split()][0:n]
        print(most_freq_word_in_array(str_arr))
