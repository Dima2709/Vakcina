class vakcina:

    def __init__(self, slovar):
        self.slovar = slovar
        massiv = []
        self.name = []
        self.pol = []
        self.vozrast = []
        self.otnoshenie = []
        self.mesyc = []
        for i in self.slovar:
            for j in self.slovar[i]:
                massiv.append(j)
        for i in massiv[::5]:
            self.name.append(i)
        for i in massiv[1::5]:
            self.pol.append(i)
        for i in massiv[2::5]:
            self.vozrast.append(i)
        for i in massiv[3::5]:
            self.otnoshenie.append(i)
        for i in massiv[4::5]:
            self.mesyc.append(i)

    def women_vakcina(self):
        count1 = 0
        for i in self.pol:
                if i == 'ж':
                    count1 += 1
        print(count1, 'Женщины прошли вакцинацию')

    def men_vakcina(self):
        count2 = 0
        for i in self.pol:
                if i == 'м':
                    count2 += 1
        print(count2, 'Мужчин прошли вакцинацию')

    def sred(self):
        print('Средний возраст прошедших вакцинацию: ',sum(self.vozrast)/len(self.vozrast))

    def sred_mes(self):
        z = []
        p = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'iun':
                    z.append(i)
        for j in z:
               p.append(self.vozrast[j])
        if len(p) > 0:
              print('Средний возраст в июне: ', sum(p)/len(p))
        else:
            print('В июне не было вакцинации')
        z1 = []
        p1 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'avgust':
                    z1.append(i)
        for j in z1:
               p1.append(self.vozrast[j])
        if len(p1) > 0:
             print('Средний возраст в августе: ', sum(p1)/len(p1))
        else:
            print('В августе не было вакцинации')
        z2 = []
        p2 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'июль':
                z2.append(i)
        for j in z2:
            p2.append(self.vozrast[j])
        if len(p2) > 0:
            print('Средний возраст в июле: ', sum(p2) / len(p2))
        else:
            print('В июле не было вакцинации')
        z3 = []
        p3 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'сентябрь':
                z3.append(i)
        for j in z3:
            p3.append(self.vozrast[j])
        if len(p3) > 0:
            print('Средний возраст в сентябре: ', sum(p3) / len(p3))
        else:
            print('В сентябре не было вакцинации')
        z4 = []
        p4 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'октябрь':
                z4.append(i)
        for j in z4:
            p4.append(self.vozrast[j])
        if len(p4) > 0:
            print('Средний возраст в октябре: ', sum(p4) / len(p4))
        else:
            print('В октябре не было вакцинации')
        z5 = []
        p5 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'ноябрь':
                z5.append(i)
        for j in z5:
            p5.append(self.vozrast[j])
        if len(p5) > 0:
            print('Средний возраст в ноябре: ', sum(p5) / len(p5))
        else:
            print('В ноябре не было вакцинации')
        z6 = []
        p6 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'декабрь':
                z6.append(i)
        for j in z6:
            p6.append(self.vozrast[j])
        if len(p6) > 0:
            print('Средний возраст в декабре: ', sum(p6) / len(p6))
        else:
            print('В декабре не было вакцинации')
        z7 = []
        p7 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'январь':
                z7.append(i)
        for j in z7:
            p7.append(self.vozrast[j])
        if len(p7) > 0:
            print('Средний возраст в январе: ', sum(p7) / len(p7))
        else:
            print('В январе не было вакцинации')
        z8 = []
        p8 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'февраль':
                z8.append(i)
        for j in z8:
            p8.append(self.vozrast[j])
        if len(p8) > 0:
            print('Средний возраст в феврале: ', sum(p8) / len(p8))
        else:
            print('В феврале не было вакцинации')
        z9 = []
        p9 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'март':
                z9.append(i)
        for j in z9:
            p9.append(self.vozrast[j])
        if len(p9) > 0:
            print('Средний возраст в марте: ', sum(p9) / len(p9))
        else:
            print('В марте не было вакцинации')
        z10 = []
        p10 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'апрель':
                z10.append(i)
        for j in z10:
            p10.append(self.vozrast[j])
        if len(p10) > 0:
            print('Средний возраст в апреле: ', sum(p10) / len(p10))
        else:
            print('В апреле не было вакцинации')
        z11 = []
        p11 = []
        for i in range(len(self.mesyc)):
            if self.mesyc[i] == 'май':
                z11.append(i)
        for j in z11:
            p11.append(self.vozrast[j])
        if len(p11) > 0:
            print('Средний возраст в мае: ', sum(p11) / len(p11))
        else:
            print('В мае не было вакцинации')
    def sred_voz(self):
        m = []
        w = []
        m1 = []
        w1 = []
        for i in range(len(self.pol)):
            if self.pol[i] == 'м':
                m.append(i)
        for i in range(len(self.pol)):
            if self.pol[i] == 'ж':
                w.append(i)
        for j in m:
            m1.append(self.vozrast[j])
        for j in w:
            w1.append(self.vozrast[j])
        print('Средний возраст у мужчин: ', sum(m1)/len(m1))
        print('Средний возраст у женщин: ', sum(w1)/len(w1))
    def loyl(self):
        p = []
        y1 = []
        y2 = []
        y3 = []
        y4 = []
        for j in range(len(self.otnoshenie)):
            if self.otnoshenie[j] == 'pol':
                p.append(j)
        for i in p:
            if self.vozrast[i] >= 18 and self.vozrast[i] < 25:
                y1.append(self.vozrast[i])
            elif self.vozrast[i] >= 25 and self.vozrast[i] < 35:
                y2.append(self.vozrast[i])
            elif self.vozrast[i] >= 35 and self.vozrast[i] < 45:
                y3.append(self.vozrast[i])
            elif i >= 45:
                y4.append(self.vozrast[i])
        if len(y1) > len(y2) and len(y1) > len(y4) and len(y1) > len(y3):
            print('Самые лояльные люди в возрасте от 18 до 25 лет')
        elif len(y2) > len(y1) and len(y2) > len(3) and len(y2) > len(y4):
            print('Самые лояльные люди в возрасте от 25 до 35 лет')
        elif len(y3) > len(y1) and len(y3) > len(2) and len(y3) > len(y4):
            print('Самые лояльные люди в возрасте от 35 до 45 лет')
        elif len(y4) > len(y1) and len(y4) > len(2) and len(y4) > len(y3):
            print('Самые лояльные люди в возрасте от 45 лет')
        else:
            print('Данные разнятся')
    def mes (self):
            a = dict((i, self.mesyc.count(i)) for i in self.mesyc)
            print(a)

b = {1:['dima','м',19,'pol','iun'],2:['dasd','ж',45,'otr','avgust'],3:['jo','м',24,'pol','iun']}

c = vakcina(b)
c.women_vakcina()
c.men_vakcina()
c.sred()
c.sred_mes()
c.sred_voz()
c.loyl()
c.mes()