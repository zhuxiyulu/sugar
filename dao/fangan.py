 # 参数表
 # sex 1 女 2 男
 # age 年龄
 # height 身高
 # weight 体重
 # yundong 1-5 表示运动强度
 # type 糖尿病类型 1 1型 2 2型 3 妊娠 4 特殊
 # bing 有无并发症 0 没有 1 有
 # xue 血糖控制 0 稳定不变 1 空腹高 2 餐后高 3 经常低血糖
 # fuyong 服用胰岛素


# 饮食方案 性别，年龄，身高，体重，运动强度，
def yinshi(sex,age,height,weight,yundong):
    bmi=weight/(height*height)
    if sex == 1:
        bmr = 655+(9.6*weight)+(1.8*height)-(4.7*age)
    else:
        bmr = 66+(13.7*weight)+(5*height)-(6.8*age)
    if yundong == 1:
        bmr=bmr*1.2
    elif yundong == 2:
        bmr = bmr * 1.375
    elif yundong == 3:
        bmr = bmr * 1.55
    elif yundong == 4:
        bmr = bmr * 1.725
    elif yundong == 5:
        bmr = bmr * 1.9
    jiaohuan=int(bmr)/90
    jiaohuan=int(jiaohuan)
    guwu, shuiguo, yurou, nai, youzhi, shucai = 1,1,1,1,1,1
    if jiaohuan==11:
        guwu,shuiguo,yurou,nai,youzhi,shucai =6,1,1,1,1,1
    elif jiaohuan==12:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 6, 1, 1, 1, 1, 1
    elif jiaohuan == 13:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 7, 1, 2, 1, 1, 1
    elif jiaohuan == 14:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 7, 1, 2, 2, 1, 1
    elif jiaohuan == 15:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 8, 1, 2, 2, 1, 1
    elif jiaohuan == 16:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 8, 1, 2, 2, 2, 1
    elif jiaohuan == 17:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 9, 1, 2, 2, 2, 1
    elif jiaohuan == 18:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 9, 1, 3, 2, 2, 1
    elif jiaohuan == 19:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 10, 1, 3, 2, 2, 1
    elif jiaohuan == 20:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 11, 1, 3, 2, 2, 1
    elif jiaohuan == 21:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 12, 1, 3, 2, 2, 1
    elif jiaohuan == 22:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 12, 1, 4, 2, 2, 1
    elif jiaohuan == 23:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 13, 1, 4, 2, 2, 1
    elif jiaohuan == 24:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 14, 1, 4, 2, 2, 1
    elif jiaohuan == 25:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 14, 1, 4, 2, 3, 1
    elif jiaohuan == 26:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 14, 1, 5, 2, 3, 1
    elif jiaohuan == 27:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 15, 1, 5, 2, 3, 1
    elif jiaohuan == 28:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 15, 2, 5, 2, 3, 1
    elif jiaohuan == 29:
        guwu, shuiguo, yurou, nai, youzhi, shucai = 15, 2, 5, 2, 3, 2
    data = {'change': jiaohuan,
            'cereals': guwu,
            'fruit': shuiguo,
            'meat': yurou,
            'milk': nai,
            'fat': youzhi,
            'vegetables': shucai
            }
    return data

# 运动方案  运动方式， 时长，每周次数
def yundong(sex,age,type,bing):
    time1, time2, time3, time4,  = 0, 0, 0, 0
    week1, week2, week3, week4 = '', '', '', ''
    if type==3:  # 孕妇
        sp1 = "散步"
        sp2 = "做家务"
        sp3 = ''
        sp4 = ''
        time1 = 20
        time2 = 15
        week1 = '3-5'
        week2 = '2-4'

    elif age >= 60:  # 老人
        sp1 = "散步"
        sp2 = "上下楼梯"
        sp3 = "打太极"
        sp4 = ''
        time1 = 10
        time2 = 10
        time3 = 30
        time4 = 0
        week1 = '3-4'
        week2 = '1-2'
        week3 = '3-5'
    elif age <= 20:
        if bing == 0:
            sp1 = "跑步"
            sp2 = "游泳"
            sp3 = "打羽毛球"
            sp4 = "自行车"
            time1 = 10
            time2 = 20
            time3 = 30
            time4 = 20
            week1 = '3-5'
            week2 = '4-5'
            week3 = '3-4'
            week4 = '3-4'
        else:
            sp1 = "快走"
            sp2 = "散步"
            sp3 = "打羽毛球"
            sp4 = "自行车"
            time1 = 10
            time2 = 10
            time3 = 30
            time4 = 20
            week1 = '3-5'
            week2 = '4-5'
            week3 = '3-4'
            week4 = '3-4'
    else:
        if sex == 2:
            if type == 1 and bing == 0:
                sp1 = "快走"
                sp2 = "散步"
                sp3 = "打羽毛球"
                sp4 = "自行车"
                time1 = 10
                time2 = 10
                time3 = 30
                time4 = 20
                week1 = '3-5'
                week2 = '4-5'
                week3 = '3-4'
                week4 = '3-4'
            elif type == 1 and bing == 1:
                sp1 = "快走"
                sp2 = "散步"
                sp3 = "打羽毛球"
                sp4 = "自行车"
                time1 = 10
                time2 = 10
                time3 = 15
                time4 = 20
                week1 = '3-5'
                week2 = '4-5'
                week3 = '3-4'
                week4 = '3-4'
            elif type == 2 and bing == 0:
                sp1 = "快走"
                sp2 = "跑步"
                sp3 = "游泳"
                sp4 = "举重"
                time1 = 20
                time2 = 10
                time3 = 30
                time4 = 10
                week1 = '3-5'
                week2 = '3-4'
                week3 = '3-4'
                week4 = '3-4'
            elif type == 2 and bing == 1:
                sp1 = "散步"
                sp2 = "快走"
                sp3 = "跑步"
                sp4 = "游泳"
                time1 = 20
                time2 = 10
                time3 = 10
                time4 = 10
                week1 = '3-5'
                week2 = '3-4'
                week3 = '2-4'
                week4 = '2-4'
        if sex == 1:
            if type == 1 and bing == 0:
                sp1 = "散步"
                sp2 = "瑜伽"
                sp3 = "跳舞"
                sp4 = "打羽毛球"
                time1 = 20
                time2 = 15
                time3 = 20
                time4 = 20
                week1 = '3-4'
                week2 = '3-4'
                week3 = '2-3'
                week4 = '2-3'
            elif type == 1 and bing == 1:
                sp1 = "散步"
                sp2 = "瑜伽"
                sp3 = "快走"
                sp4 = "打乒乓球"
                time1 = 20
                time2 = 15
                time3 = 15
                time4 = 20
                week1 = '3-4'
                week2 = '2-4'
                week3 = '2-3'
                week4 = '2-3'
            elif type == 2 and bing == 0:
                sp1 = "快走"
                sp2 = "跑步"
                sp3 = "游泳"
                sp4 = "自行车"
                time1 = 20
                time2 = 15
                time3 = 15
                time4 = 20
                week1 = '3-4'
                week2 = '3-4'
                week3 = '2-3'
                week4 = '2-4'
            elif type == 2 and bing == 1:
                sp1 = "快走"
                sp2 = "跑步"
                sp3 = "游泳"
                sp4 = "瑜伽"
                time1 = 20
                time2 = 10
                time3 = 30
                time4 = 15
                week1 = '3-4'
                week2 = '3-4'
                week3 = '2-3'
                week4 = '3-4'
    data = {'sport1': sp1,
            'sport2': sp2,
            'sport3': sp3,
            'sport4': sp4,
            'time1': time1,
            'time2': time2,
            'time3': time3,
            'time4': time4,
            'week1': week1,
            'week2': week2,
            'week3': week3,
            'week4': week4,
            }
    return data

# 控糖方案 早中晚一样（前：min1-max1， 后：min2-mxa2）
def kongtang(sex,age,type,fuyong,bing,xue):
    if age<=20:
        min1,max1,min2,max2,sleep1,sleep2=5.0,8.0,5.0,10.0,6.7,10.0
        if xue==1:
            max1=max1+0.5
        elif xue==2:
            max2=max2+0.5
        elif xue==3:
            min1=min1-0.3
            min2=min2-0.3
            max1=max1-0.3
            max2=max2-0.3
    elif type==3:
        min1, max1, min2, max2, sleep1 ,sleep2= 3.9,7.2,5.0,8.0,6.7,8.0
        if xue == 1:
            max1 = max1 + 0.5
        elif xue == 2:
            max2 = max2 + 0.5
        elif xue == 3:
            min1 = min1 - 0.3
            min2 = min2 - 0.3
            max1 = max1 - 0.3
            max2 = max2 - 0.3
    elif age >= 60:
        min1, max1, min2, max2, sleep1 ,sleep2= 6.0,7.0,8.0,10.0,7.0,10.0
        if bing == 1:
            min1 = min1 + 1.0
            max1 = max1 + 2.0
            max2 = max2 + 1.0
            sleep1 = sleep1 + 1.0
            sleep2 = sleep2 + 1.0
        if xue == 1:
            max1 = max1 + 0.1
        elif xue == 2 :
            max2 = max2 + 0.2
        elif xue == 3:
            min1 = min1 - 0.3
            min2 = min2 - 0.3
            max1 = max1 - 0.3
            max2 = max2 - 0.3
    else:
        min1, max1, min2, max2, sleep1, sleep2 = 3.9,7.2,5.0,8.0,6.7,8.0
        if bing == 1:
            min1 = min1 + 1.5
            max1 = max1 + 0.6
            min2 = min2 + 1
            max2 = max2 + 2
            sleep1 = sleep1 + 2
        elif fuyong == 1:
            min1 = min1 + 0.5
            max1 = max1 + 0.6
            max2 = max2 + 2
            sleep1 = sleep1 +2
        if xue == 1:
            max1 = max1 + 0.1
        elif xue == 2 :
            max2 = max2 + 0.2
        elif xue == 3:
            min1 = min1 - 0.3
            min2 = min2 - 0.3
            max1 = max1 - 0.3
            max2 = max2 - 0.3
    data = {'min1': '%.1f'%min1,
            'max1': '%.1f'%max1,
            'min2': '%.1f'%min2,
            'max2': '%.1f'%max2,
            'sleep1': '%.1f'%sleep1,
            'sleep2': '%.1f'%sleep2}
    return data

# a=kongtang(1,21,1,1,1,1)
# print(a)