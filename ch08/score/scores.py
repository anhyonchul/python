with open('scorelist.txt', 'w') as f:
    key = ''
    while True:
        try:
            key = input("성적을 저장할까요? (y/n) : ")
            if key == 'n' or key =='Y':
                break
            elif key == 'y' or key =='N':
                name = input("이름 입력 : ")
                kor = int(input("국어 점수 : "))
                math = int(input("수학 점수 : "))
                #avg = (kor + math) / 2

                f.write(name + ' ')
                f.write(str(kor) + ' ')
                f.write(str(math) + '\n')
                #f.write(str(avg) + '\n')
            else:
                print("잘못된 입력입니다. 다시 입력해주세요")

        except ValueError:
            print("잘못된 입력입니다. 다시 입력해주세요")

    print("입력을 종료합니다.")