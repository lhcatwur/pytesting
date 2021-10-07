#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : example.py
# Date              : 07.10.2021
# Last Modified Date: 07.10.2021
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def test_addFloat(tol=1e5):
    assert abs(add(0.1, 0.2) -  0.3) <= tol     
