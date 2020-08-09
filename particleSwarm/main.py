
import random

import collections

import time




verboseMode=False

def equation(x):
    result=x*x+7*x-18
    return result



class particle:
    def __init__(self,value,result,v=0,pbest=0):
        self.value=value
        self.result=result
        self.v=v
        self.pb=[]
        self.pb.append(self.value)
        self.pbest=self.best()
       
        
    
    def best(self):
        alis=[]
        for i in self.pb:
            result=abs(0-i)
            alis.append(result) 
        
        return min(alis)       


   
class ParticleSwarmOptimization:

    def __init__(self):
        self.pbest=0
        self.gbest=0
        self.particules=[]
        self.denklemKokleri=[]
     
        

    def create_particules(self,count):
        
        eslesme=True


        while(eslesme):
            self.particules.clear()
            for i in range(0,count):
                v=random.randint(0,10)
                self.particules.append(particle(v,equation(v)))

            for item,count in collections.Counter(self.particules).items():
                if (count>1):
                    eslesme=True
                else:
                    eslesme=False
        

   


    def closeToZero(self,values):
        
        alist=[]

        for i in values:
            result=abs(0-i.result)
            alist.append(result)
            
    
        mini=min(alist)
        if(verboseMode):
            print("minimum value: " + str(mini))
        
     
       
        for a in values:
           
            if mini==abs(0-a.result):
                
                return a
                
                     
           
                

        

    def particleSwarmEq(self,x,v,pbest,gbest):
        rand1=random.randint(0,10)/10
        rand2=random.randint(0,10)/10
        vlast=v+2*rand1*(pbest-x)+2*rand2*(gbest-x)
        return vlast


    def solution(self,particules):
        
        kontrol=0

        for aba in range(0,3):

            gbestval=self.closeToZero(self.particules)
            
            
          
            if(gbestval.result==0):
                if(verboseMode):
                    print(str(gbestval.value)+" "+str(gbestval.result)+" "+str(gbestval.v))
                kontrol=1
                break
            
                
            self.gbest=gbestval.value

  
            



            for p in self.particules:
                p.v=self.particleSwarmEq(x=p.value,v=p.v,pbest=p.best(),gbest=self.gbest)
        

            for p in self.particules:
                p.value=p.value+p.v
                p.result=equation(p.value)
                
        
        return kontrol,gbestval.value        
            
   

    def solve(self,count):
    
        res=0
        
        try:
           self.create_particules(count)
          
        finally:
            res,kok=self.solution(self.particules)
            while(res==0):
                
                try:
                    self.create_particules(count)
                finally:
                    res,kok=self.solution(self.particules)    

        self.denklemKokleri.append(kok)
        while(self.denklemKokleri.__contains__(kok) or res==0):
            try:
                self.create_particules(count)
            finally:
                res,kok=self.solution(self.particules)    
            
        self.denklemKokleri.append(kok)

pso=ParticleSwarmOptimization()
pso.solve(count=6)


print("\n")
print("Solutions Of The Equation: ")
print(" x1 :  "+ str( pso.denklemKokleri[0]))
print(" x2 :  "+ str( pso.denklemKokleri[1]))


