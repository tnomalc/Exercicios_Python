#!/usr/bin/env python
#-*-coding:utf-8-*-
import random

operacionais = ["OpenIndiana","FreeBSD","GNU/Linux","OpenBSD","NetBSD","DragonflyBSD"]
print(operacionais)

random.shuffle(operacionais)
selecionado = random.choice(operacionais)
print(selecionado)



