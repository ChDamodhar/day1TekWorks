cno,cname=map(str,input("Enter student number and name").split())
pmr,lmr=map(int,input("Enter present month and last month readings:").split())
tu=pmr-lmr
cbill=tu*3.80
print(f'customerno:{cno} cname:{cname} pmr:{pmr} lmr:{lmr} totalunits:{tu} currentbill{cbill}')