if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    j = 0
    float(j)
    for i in student_marks[query_name]:
        j += i
    j /= len(student_marks[query_name])
    print('%.2f' % j)
    

