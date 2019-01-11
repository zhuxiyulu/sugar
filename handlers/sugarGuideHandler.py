from tornado.web import RequestHandler
from tornado.web import gen
from controller import sugarGuideController
import json


# 保存糖导的结果
class AddSugarGuideResult(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        gender = self.get_argument('gender')
        age = self.get_argument('age')
        height = self.get_argument('height')
        weight = self.get_argument('weight')
        sugarType = self.get_argument('sugarType')
        diseaseAge = self.get_argument('diseaseAge')
        akin = self.get_argument('akin')
        fm = self.get_argument('fm')
        manyDrinkWc = self.get_argument('manyDrinkWc')
        posion = self.get_argument('posion')
        thirsty = self.get_argument('thirsty')
        visionDown = self.get_argument('visionDown')
        diseaseSpeed = self.get_argument('diseaseSpeed')
        verifyYear = self.get_argument('verifyYear')
        cureWay =  self.get_argument('cureWay')
        dsPlan = self.get_argument('dsPlan')
        complication = self.get_argument('complication')

        data = sugarGuideController.createHealthWeekly(session_id, gender, age, height, weight,
                                                       sugarType, diseaseAge, akin, fm,
                                                       manyDrinkWc, posion, thirsty,
                                                       visionDown, diseaseSpeed, verifyYear,
                                                       cureWay, dsPlan, complication)
        self.write(json.dumps(data))

# 获取健康周报
class GetHealthWeekly(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        data = sugarGuideController.retireveHealthWeekly(session_id)
        self.render('healthWeekly.html', cerealsValue=data['diet']['cerealsValue'],
                    cereals=data['diet']['cereals'],fruitValue=data['diet']['fruitValue'],
                    fruit=data['diet']['fruit'],meatValue=data['diet']['meatValue'],
                    meat=data['diet']['meat'],milkValue=data['diet']['milkValue'],
                    milk=data['diet']['milk'],fatValue=data['diet']['fatValue'],
                    fat=data['diet']['fat'],vegetablesValue=data['diet']['vegetablesValue'],
                    vegetables=data['diet']['vegetables'],
                    sport1=data['sport']['sport1'],sport2=data['sport']['sport2'],
                    sport3=data['sport']['sport3'],sport4=data['sport']['sport4'],
                    time1=data['sport']['time1'], time2=data['sport']['time2'],
                    time3=data['sport']['time3'], time4=data['sport']['time4'],
                    week1=data['sport']['week1'], week2=data['sport']['week2'],
                    week3=data['sport']['week3'], week4=data['sport']['week4'],
                    min1=data['control']['min1'],max1=data['control']['max1'],
                    min2=data['control']['min2'],max2=data['control']['max2'],
                    sleep1=data['control']['sleep1'],sleep2=data['control']['sleep2'],)
