def rd(a):
    print("[", end='')
    for num in a:
        print(num, end =' ')
    print("]")

for _ in range (int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    st = []
    for i in range(n):
        while len(st) > 0 and a[i] >= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            print(i+1, end = ' ')
        else:
            print(i - st[-1], end = ' ')
        st.append(i)
    print()
