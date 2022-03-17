# -*- coding: utf-8 -*-

# ����
# ũ�Ⱑ N�� ���� A = A1, A2, ..., AN�� �ִ�. ������ �� ���� Ai�� ���ؼ� ��ū�� NGE(i)�� ���Ϸ��� �Ѵ�. Ai�� ��ū���� �����ʿ� �����鼭 Ai���� ū �� �߿��� ���� ���ʿ� �ִ� ���� �ǹ��Ѵ�. �׷��� ���� ���� ��쿡 ��ū���� -1�̴�.

# ���� ���, A = [3, 5, 2, 7]�� ��� NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1�̴�. A = [9, 5, 4, 8]�� ��쿡�� NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1�̴�.

# �Է�
# ù° �ٿ� ���� A�� ũ�� N (1 �� N �� 1,000,000)�� �־�����. ��° �ٿ� ���� A�� ���� A1, A2, ..., AN (1 �� Ai �� 1,000,000)�� �־�����.

# ���
# �� N���� �� NGE(1), NGE(2), ..., NGE(N)�� �������� ������ ����Ѵ�.

import sys

l = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(" ")))
b = []
r = []
max_val = 0
max_idx = 0
for i in range(l):
    n = a.pop()
    b.append(n)
    if n > max_val:
        r.append(-1)
        max_val = n
        max_idx = 1
    else:
        for j in range(max_idx):
            b[-(j + 1)] > n
for i in range(l):
    print(r.pop(), end=' ')