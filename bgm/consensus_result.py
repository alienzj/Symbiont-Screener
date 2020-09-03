#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

class ConsensusResult:

    def __init__(self,total, loop_num , min_hit_fac=0.2):
        self.total = int(total)
        self.loop_num = int(loop_num)
        self.min_hit_fac = float(min_hit_fac)
        self.min_threshold = int(min_hit_fac*self.loop_num)
        self.results = []
        self.best_hits = []

    def PushOneResult(self , result, best_hit):
        self.results.append(result);
        self.best_hits.append(best_hit)

    def GenFinalResult(self):
        self.scores= np.zeros(self.total)
        self.hosts= np.zeros(self.total)
        for i,result in enumerate(self.results):
            hit=np.where(result==self.best_hits[i])
            for index in hit :
                self.scores[index] +=1;
        for i,score in enumerate(self.scores) : 
            if score >= self.min_threshold:
                self.hosts[i] = 1
            else :
                self.hosts[i] = 0


