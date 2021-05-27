emails=("1515423623" "5613626" "36342626" "516236547" "6236734734" "1516236253" "15134626" "56547347" "34734784" "8548548")
events=('办公' '娱乐' '写信' '学习' '敲码')
for email in ${emails[*]}
do
for event in ${events[*]}
do
key=$email"@qq.com"$event
python3 GetFont.py ${key}
cp out.ttf "/mnt/d/font/"${key}".ttf"
done
done
