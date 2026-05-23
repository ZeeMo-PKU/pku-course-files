num=int(input())
print(num)
for i in range(0,num):
    Haab=input()
    day,month,year=Haab.split()
    day=int(day[:-1])
    Haab_year=list('pop、no、zip、zotz、tzec、xul、yoxkin、mol、chen、yax、zac、ceh、mac、kankin、muan、pax、koyab、cumhu、uayet'.split('、'))
    year=int(year)
    month=Haab_year.index(month)
    days=day+1+year*365+month*20
    if days%260==0:
        now_year=days//260-1
        left=260
    else:
        now_year=days//260
        left=days%260
    Tzolkin=list('ahau、imix、ik、akbal、kan、chicchan、cimi、manik、lamat、muluk、ok、chuen、eb、ben、ix、mem、cib、caban、eznab、canac'.split('、'))
    if days%13==0:
        day=13
    else:
        day=days%13
    month=Tzolkin[left%20]
    print(day,month,now_year)

