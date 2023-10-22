def min_removals_to_anagram(str1, str2):
    same = []
    for i in set(str1) :
        cnt1 = str1.count(i)
        cnt2 = str2.count(i)
        if cnt2 > 0 :
            for j in range(min(cnt1,cnt2)) :
                same.append(i)
    min_num = len(str1) - len(same) + len(str2) - len(same)
    return min_num

str1 = input()
str2 = input()

print(min_removals_to_anagram(str1, str2))