'''
Author: your name
Date: 2021-05-23 14:27:11
LastEditTime: 2021-05-23 14:41:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \study_for_pytest\code\ch1\test_one.py
'''
import pytest
import os
import sys

path_ch1=os.path.dirname(os.path.abspath(__file__))



def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


if __name__=='__mian__':
    pytest.main(['-v','-s',r'{}\test_one.py'.format(path_ch1)])