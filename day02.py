limits = 20
tweets = "pass\n" * 6

diff = limits - len(tweets)

if diff >= 0:
    print(tweets)

else:
    print(f'제한 글자 수 {abs(diff)} 초과') # 절대값으로 변환

############################


vowels = 'aeiou'

letter = 'x'

if letter in vowels:
    print("fail")

else:
    print("success")


########################

letter = 'u'

if letter not in vowels:
    print("success")

else:
    print("fail")


