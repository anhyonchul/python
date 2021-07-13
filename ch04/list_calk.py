#리스트의 연산

score = [72, 81, 53, 61, 98, 45]
avg = 0.0
sum = 0
count = len(score)

# 합계


for i in score:
    sum = sum + i #sum += i 과 같음
    print("i = %d, sum=%d" % (i, sum))

#평균


avg = sum / count

#print("개수 : %d개" % count)
print("개수 : {0}개".format(count))
#print("합계 : %d점" % sum)
print("합계 : {0}점".format(sum))
print("평균 : %.1f점" % avg)
