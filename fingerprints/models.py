# -*- coding: utf-8 -*-
from django.db import models

PATTERN_TYPE = (('A', u'Дуга'),
                ('At', u'Тентовая Дуга'),
                ('L', u'Петля'),
                ('Lp', u'Павлиний глаз'),
                ('Ws', u'Завиток спиралькой'),
                ('W', u'Завиток кружками'),
                ('2L', u'Двойная петля'),
                ('C', u'Сложный узор'))

ORIENT_TYPE = (('U', u'Ульнарная'), # Завиток: Прав рука - против, Левая - по; Петля: хвостик от Бол пал
               ('R', u'Радиальная')) # Завиток: Прав рука - по, Левая - против;  Петля: хвостик к Бол пал


class FingerPrints(models.Model):
    pattern = models.CharField(max_length=2, choices=PATTERN_TYPE, verbose_name=u'Тип узора')
    orient = models.CharField(max_length=1, choices=ORIENT_TYPE, null=True, default=None, verbose_name=u'Ориентация узора')
    rc_u = models.IntegerField(default=0, blank=True, verbose_name = u'Ульнарный ГС')
    rc_r = models.IntegerField(default=0, blank=True, verbose_name = u'Радиальный ГС')
           
    
    class Meta:
        verbose_name = u'палец'
        verbose_name_plural = u'пальцы'
        
    def __unicode__(self):
        return "%s %s (%s, %s)" % (self.pattern, self.orient, self.rc_u, self.rc_r)
    
    @property
    def is_complicated(self):
        return self.pattern == 'Ws' or self.pattern == 'W' or self.pattern == '2L' or self.pattern == 'C'
    

class Human(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name=u'имя')
    desc = models.TextField(blank=True, verbose_name=u'описание')
    # далее - вектора и вероятность от 0 до 10 присутствия этого вектора
    ur = models.NullBooleanField(default=None, verbose_name='У')
    an = models.NullBooleanField(default=None, verbose_name='А')
    ko = models.NullBooleanField(default=None, verbose_name='К')
    my = models.NullBooleanField(default=None, verbose_name='М') 
    zr = models.NullBooleanField(default=None, verbose_name='Зр')
    zv = models.NullBooleanField(default=None, verbose_name='Зв')
    o  = models.NullBooleanField(default=None, verbose_name='Ор')
    ob = models.NullBooleanField(default=None, verbose_name='Об')
    
    # далее - руки от 1(Бол) до 5(Миз) пальца
    r1 = models.ForeignKey(FingerPrints, verbose_name=u'П Бол', related_name = 'r1')
    r2 = models.ForeignKey(FingerPrints, verbose_name=u'П Ук', related_name = 'r2')
    r3 = models.ForeignKey(FingerPrints, verbose_name=u'П Ср', related_name = 'r3')
    r4 = models.ForeignKey(FingerPrints, verbose_name=u'П Без', related_name = 'r4')
    r5 = models.ForeignKey(FingerPrints, verbose_name=u'П Миз', related_name = 'r5')
    l1 = models.ForeignKey(FingerPrints, verbose_name=u'Л Бол', related_name = 'l1')
    l2 = models.ForeignKey(FingerPrints, verbose_name=u'Л Ук', related_name = 'l2')
    l3 = models.ForeignKey(FingerPrints, verbose_name=u'Л Ср', related_name = 'l3')
    l4 = models.ForeignKey(FingerPrints, verbose_name=u'Л Без', related_name = 'l4')
    l5 = models.ForeignKey(FingerPrints, verbose_name=u'Л Миз', related_name = 'l5')
    
    class Meta:
        verbose_name = u'человек'
        verbose_name_plural = u'люди'
        
    def __unicode__(self):
        return self.name
    
    @property
    def sum_rc(self):
        s = 0
        s += self.r1.rc_u + self.r1.rc_r
        s += self.r2.rc_u + self.r2.rc_r
        s += self.r3.rc_u + self.r3.rc_r
        s += self.r4.rc_u + self.r4.rc_r
        s += self.r5.rc_u + self.r5.rc_r
        
        s += self.l1.rc_u + self.l1.rc_r
        s += self.l2.rc_u + self.l2.rc_r
        s += self.l3.rc_u + self.l3.rc_r
        s += self.l4.rc_u + self.l4.rc_r
        s += self.l5.rc_u + self.l5.rc_r
        return s
    
    @property
    def complicated_count(self):
        s = 0
        if self.r1.is_complicated: s += 1
        if self.r2.is_complicated: s += 1
        if self.r3.is_complicated: s += 1
        if self.r4.is_complicated: s += 1
        if self.r5.is_complicated: s += 1
        if self.l1.is_complicated: s += 1
        if self.l2.is_complicated: s += 1
        if self.l3.is_complicated: s += 1
        if self.l4.is_complicated: s += 1
        if self.l5.is_complicated: s += 1

        return s
    

