
#Input
#Input
a = int(input())
b = int(input())
count_odd = 0
count_even = 0

for i in range(a, b + 1):
    # chú ý đến quy luật mình đã ghi nhé 
    # vì chỉ số tính từ 0 lên b+1 or theo cái mình vẽ ở trong sách nhé chú ý nhé
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)
