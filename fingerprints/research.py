# -*- coding: utf-8 -*-


import os
from os.path import dirname
import sys

ROOT = dirname(dirname(os.path.abspath(__file__)))
PROJECT_ROOT = ROOT
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "derm_svp.settings")

import sys
from django.conf import settings
from fingerprints.models import FingerPrints, Human


def select_AKMZr():
    return Human.objects.filter(ur=False,
                                  an=True,
                                  ko=True,
                                  my=True,
                                  zr=True,
                                  zv=False,
                                  o =False,
                                  ob=False)

def select_without_Zv():
    return Human.objects.filter(zv=False)

def select_with_Zv():
    return Human.objects.filter(zv=True)
 
    
def go_u_l_rc(filename, func):
    file_to = open(filename, 'w')
    
    for h in func():
        line = ','.join([h.name.encode('utf-8'), 
                                str(h.r1.rc_u), str(h.r1.rc_r),
                                str(h.r2.rc_u), str(h.r2.rc_r),
                                str(h.r3.rc_u), str(h.r3.rc_r),
                                str(h.r4.rc_u), str(h.r4.rc_r),
                                str(h.r5.rc_u), str(h.r5.rc_r),
                                
                                str(h.l1.rc_u), str(h.l1.rc_r),
                                str(h.l2.rc_u), str(h.l2.rc_r),
                                str(h.l3.rc_u), str(h.l3.rc_r),
                                str(h.l4.rc_u), str(h.l4.rc_r),
                                str(h.l5.rc_u), str(h.l5.rc_r),
                                '\n'])
        file_to.write(line)
    file_to.close()
    
def go_sum_rc(filename, func):
    file_to = open(filename, 'w')
    
    for h in func():
        line = ','.join([h.name.encode('utf-8'), 
                                str(h.r1.rc_u + h.r1.rc_r),
                                str(h.r2.rc_u + h.r2.rc_r),
                                str(h.r3.rc_u + h.r3.rc_r),
                                str(h.r4.rc_u + h.r4.rc_r),
                                str(h.r5.rc_u + h.r5.rc_r),
                                
                                str(h.l1.rc_u + h.l1.rc_r),
                                str(h.l2.rc_u + h.l2.rc_r),
                                str(h.l3.rc_u + h.l3.rc_r),
                                str(h.l4.rc_u + h.l4.rc_r),
                                str(h.l5.rc_u + h.l5.rc_r),
                                
                                str(h.complicated_count),
                                '\n'])
        file_to.write(line)
    file_to.close()

def go_div_rc(filename, func):
    file_to = open(filename, 'w')
    
    for h in func():
        line = ','.join([h.name.encode('utf-8'), 
                                str(float(h.r1.rc_u + h.r1.rc_r + 1) / (h.l1.rc_u + h.l1.rc_r + 1)),
                                str(float(h.r2.rc_u + h.r2.rc_r + 1) / (h.l2.rc_u + h.l2.rc_r + 1)),
                                str(float(h.r3.rc_u + h.r3.rc_r + 1) / (h.l3.rc_u + h.l3.rc_r + 1)),
                                str(float(h.r4.rc_u + h.r4.rc_r + 1) / (h.l4.rc_u + h.l4.rc_r + 1)),
                                str(float(h.r5.rc_u + h.r5.rc_r + 1) / (h.l5.rc_u + h.l5.rc_r + 1)),
                                '\n'])
        file_to.write(line)
    file_to.close()

go_div_rc('without_zv.csv', select_without_Zv)
go_div_rc('with_zv.csv', select_with_Zv)

