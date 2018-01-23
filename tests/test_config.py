# coding:utf-8

import sys, os

testdir = os.path.dirname(__file__)
srcdir = '../star_solver/'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

import config as cfg


class ConfigFileTests(unittest.TestCase):

    
    def test_generate_config(self):

        #Arrange

        #Act

        #Assert
        cfg.generate_default_config()
        
        config = cfg.read_config('solver.ini')
        self.assertEqual('eos.csv', config['EOS']['filename'])

