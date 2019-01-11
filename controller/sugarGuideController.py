from dao.sessionDao import redisCon
from dao import dietPlanDao
from dao import sportPlanDao
from dao import controlPlanDao
from dao import fangan


# 保存糖导的结果
def createHealthWeekly(session_id, gender, age, height, weight, sugarType, diseaseAge, akin, fm, manyDrinkWc, posion, thirsty, visionDown, diseaseSpeed, verifyYear, cureWay, dsPlan, complication):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if gender == '':
        data = {'code': 1, 'msg': '性别不能为空'}
        return data
    if age == '':
        data = {'code': 1, 'msg': '年龄不能为空'}
        return data
    if height == '':
        data = {'code': 1, 'msg': '身高不能为空'}
        return data
    if weight == '':
        data = {'code': 1, 'msg': '体重不能为空'}
        return data
    if sugarType == '':
        data = {'code': 1, 'msg': '血糖类型不能为空'}
        return data
    if verifyYear == '':
        data = {'code': 1, 'msg': '确证年份不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    if gender != '男' and gender != '女':
        data = {'code': 1, 'msg': '性别有误'}
        return data
    genderList ={'男': 1, '女': 2}
    gendercode = genderList[gender]
    age = int(age)
    height = float(height)
    weight = float(weight)
    sugarTypeList = {'1型糖尿病': 1, '2型糖尿病': 2, '妊娠期糖尿病': 3, '特殊糖尿病': 4}
    type = sugarTypeList[sugarType]
    if cureWay == '胰岛素':
        fuyong = 1
    else:
        fuyong = 0
    if complication == '':
        bing = 0
    else:
        bing = 1
    xueList = {'稳定不变': 0, '空腹高': 1, '餐后高': 2, '经常低血糖': 3}
    dietData = fangan.yinshi(gendercode, age, height, weight, 1)
    sportData = fangan.yundong(gendercode, age, type, bing)
    controlData = fangan.kongtang(gendercode, age, type, fuyong, bing, 1)
    result_diet = dietPlanDao.updateDietPlan(userId, dietData['change'], dietData['cereals'], dietData['fruit'],
                                             dietData['meat'], dietData['milk'], dietData['fat'],
                                             dietData['vegetables'])
    result_sport = sportPlanDao.updateSportPlan(userId, sportData['sport1'], sportData['sport2'],
                                                sportData['sport3'], sportData['sport4'],
                                                sportData['time1'], sportData['time2'],
                                                sportData['time3'], sportData['time4'],
                                                sportData['week1'], sportData['week2'],
                                                sportData['week3'], sportData['week4'])

    result_control = controlPlanDao.updateControlPlan(userId, controlData['min1'], controlData['max1'],
                                                      controlData['min2'], controlData['max2'],
                                                      controlData['sleep1'], controlData['sleep2'])
    if result_diet == 1 and result_sport == 1 and result_control == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '暂时无法保存'}
    return data



# 获取周报
def retireveHealthWeekly(session_id):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    dietData = dietPlanDao.selectDietPlan(userId)
    sportData = sportPlanDao.selectSportPlan(userId)
    controlData = controlPlanDao.selectConteolPlan(userId)
    cerealsValue = int(dietData.cereals)
    fruitValue = int(dietData.fruit)
    meatValue = int(dietData.meat)
    milkValue = int(dietData.milk)
    fatValue = int(dietData.fat)
    vegetablesValue = int(dietData.vegetables)

    diet = {'cereals': str(25 * cerealsValue) + '克大米, 麦片，面食， 面包, '+str(50 * cerealsValue)+'克马铃薯',
            'fruit': str(500*fruitValue) + '克西瓜, +' + str(300*fruitValue) + '克草莓，'+str(200*fruitValue)+'克葡萄，橙子，橘子 '+str(150*fruitValue)+'克香蕉,荔枝',
            'meat': str(25*meatValue) + '克大豆，' + str(20*meatValue) + '克腐竹，' + str(60*meatValue) + '克鸡蛋，' + str(50*meatValue) + '克鸭肉,猪肉，' + str(80*meatValue) + '克草鱼，' + str(100*meatValue) +'克鲫鱼',
            'milk': str(20*milkValue) + '克奶粉,' + str(160*milkValue) + '克牛奶，羊奶',
            'fat': '（一汤勺为准）' + str(10*fatValue) + '克花生油，豆油，黄油，菜籽油,'+ str(15*fatValue) + '克核桃,杏仁,花生',
            'vegetables': str(500*vegetablesValue) + '克白菜，韭菜，西红柿，冬瓜，茄子，丝瓜,' + str(200*vegetablesValue)+'克胡萝卜,' + str(150*vegetablesValue) + '克山药，' + str(70*vegetablesValue) +'克毛豆',
            'cerealsValue': cerealsValue,
            'fruitValue': fruitValue,
            'meatValue': meatValue,
            'milkValue': milkValue,
            'fatValue': fatValue,
            'vegetablesValue': vegetablesValue}

    sport = {
        'sport1': sportData.sport1,
        'sport2': sportData.sport2,
        'sport3': sportData.sport3,
        'sport4': sportData.sport4,
        'time1': sportData.time1,
        'time2': sportData.time2,
        'time3': sportData.time3,
        'time4': sportData.time4,
        'week1': sportData.week1,
        'week2': sportData.week1,
        'week3': sportData.week1,
        'week4': sportData.week1,
    }
    control = {
        'min1': controlData.min1,
        'max1': controlData.max1,
        'min2': controlData.min1,
        'max2': controlData.max2,
        'sleep1': controlData.sleep1,
        'sleep2': controlData.sleep2,

    }
    data = {'code': 0, 'diet': diet, 'sport': sport, 'control': control}
    return data
