input_data = input().split(" ")
A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])

print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)