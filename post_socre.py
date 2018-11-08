# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     post_socre
   Description :
   Author :       Lychlov
   date：          2018/11/6
-------------------------------------------------
   Change Activity:
                   2018/11/6:
-------------------------------------------------
"""
import score_factory as sf
import requests

source = [
    # (1, '差'),
    (2, '中'),
    (3, '优'),
    (4, '中'),
    (5, '中'),
    (6, '优'),
    (7, '良'),
    (8, '差'),
    (9, '差'),
    (10, '良'),
    (11, '优'),
    (12, '差'),
    (13, '中'),
    (14, '差'),
    (15, '中'),
    (16, '优'),
    (17, '差'),
    (18, '差'),
    (19, '中'),
    (20, '差'),
    (21, '中'),
    (22, '差'),
    (27, '优'),
    (28, '中'),
    (29, '优'),
    (30, '中'),
    (31, '差'),
    (32, '差'),
    (33, '差'),
    (34, '中'),
    (35, '差'),
    (36, '良'),
    (37, '良'),
    (38, '差'),
    (39, '中'),
    (40, '差'),
    (41, '差'),
    (42, '差'),
    (43, '差'),
    (44, '差'),
    (45, '差'),
    (46, '差'),
    (47, '差'),
    (48, '差'),
    (49, '差'),
    (50, '良'),
    (51, '优'),
    (52, '差'),
    (53, '差'),
    (54, '差'),
    (55, '差'),
    (56, '差'),
    (57, '差'),
    (58, '差'),
    (59, '差'),
    (60, '差'),
    (61, '优'),
    (62, '差'),
    (63, '差'),
    (64, '中'),
    (65, '差'),
    (66, '差'),
    (67, '差'),
    (68, '差'),
    (69, '差'),
    (70, '中'),
    (71, '差')]
# base_url = 'http://120.78.147.8/projectvote/tool/search.php?opt=3&a=%s&b=%s&c=%s&d=%s&telNo=henan1&project=%s&jtype=1'
base_url = 'http://120.78.147.8/projectvote/tool/search.php?opt=3&j=%s&k=%s&l=%s&m=%s&telNo=henan2&project=%s&jtype=2'
for pair in source:
    score, scores = sf.generator(pair[1])
    print(pair[0], score, scores)
    target_url = base_url % (scores[0], scores[1], scores[2], scores[3], pair[0])
    print(target_url)
    r = requests.get(target_url)
    print(r.content)
