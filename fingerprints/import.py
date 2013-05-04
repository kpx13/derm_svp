# -*- coding: utf-8 -*-


import os
from os.path import dirname
import sys

ROOT = dirname(dirname(os.path.abspath(__file__)))
PROJECT_ROOT = ROOT
sys.path.append(PROJECT_ROOT)
print PROJECT_ROOT
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "derm_svp.settings")

import sys
from django.conf import settings
from fingerprints.models import FingerPrints, Human

def get_bool(val):
    if val == '1': return True
    elif val == '0': return False
    elif val == '-1': return None

def get_finger(val):
    line = val.strip().split(';')
    if len(line) == 4:
        fp = FingerPrints(pattern=line[0],
                          orient=line[1], 
                          rc_u=line[2],
                          rc_r=line[3])
    else:
        fp = FingerPrints(pattern=line[0])
    fp.save()
    return fp
    

def process(line):
    
    line = line.strip().split(',')
    print line[0]
    
    Human(name=line[0].decode('utf-8'),
          desc=line[9].decode('utf-8'),
          ur=get_bool(line[1]),
          an=get_bool(line[2]),
          ko=get_bool(line[3]),
          my=get_bool(line[4]),
          zr=get_bool(line[5]),
          zv=get_bool(line[6]),
          o =get_bool(line[7]),
          ob=get_bool(line[8]),
          
          r1= get_finger(line[10]),
          r2= get_finger(line[11]),
          r3= get_finger(line[12]),
          r4= get_finger(line[13]),
          r5= get_finger(line[14]),
          l1= get_finger(line[15]),
          l2= get_finger(line[16]),
          l3= get_finger(line[17]),
          l4= get_finger(line[18]),
          l5= get_finger(line[19]),
          ).save()
    
    """
    category = price_line[0].decode('utf-8')
    name = price_line[1].decode('utf-8')
    art = price_line[2].decode('utf-8')
    cars = price_line[3].decode('utf-8').split(' ')
    color = price_line[4].decode('utf-8')
    price = price_line[9].decode('utf-8')"""
    """
    if price == '':
        price = 0
    profit = price_line[11].decode('utf-8')
    category = Category.add_and_get(category)
    color = Color.add_and_get(color)
    for c in cars:
        car = CarModel.add_and_get(c)
        if car:
            Item(category=category,
                 car_model=car,
                 color=color,
                 name=name,
                 art=art,
                 price=price,
                 profit=profit).save()
    """
                 
    
def go(filename):
    file_from = open(filename, 'r')
    first = True
    for l in file_from:
        if not first:
            process(l)
        else:
            first = False

go('subjects.csv')