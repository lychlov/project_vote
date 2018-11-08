# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     score_factory
   Description :
   Author :       Lychlov
   date：          2018/11/6
-------------------------------------------------
   Change Activity:
                   2018/11/6:
-------------------------------------------------
"""
import random

grades = {'优': 90, '良': 80, '中': 70, '差': 60}


def generator(grade):
    score = grades[grade] + random.randint(0, 9)
    rest =  100 - score
    temp =[0,0,0,0]
    for i in range(3):
        temp[i] = random.randint(0,(rest-sum(temp))//(3-i))
    temp[3] = rest - sum(temp)+temp[3]
    return score,[25-x for x in temp]


# for i in range(10):
    # print(generator('差'))


def score_factory(index, grade):
    it_score,it_scores = generator(grade)
    b_score,b_scores = generator(grade)
