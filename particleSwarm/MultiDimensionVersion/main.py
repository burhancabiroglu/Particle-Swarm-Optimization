
import random

import collections

import time

# Verbose Modu(HATA AYIKLAMA MODU)
verbose_mode=False



# xözülmesi istenen denklem
def equation(x,y,z,t,w):
    result=11*x*x*x*x*x*x-y*y*y*y-4*z*z*z+3*t*t-7*w-7
    return result

print("\n\n")
print("  DENKLEM EN OPTIMAL SEKILDE COZULUYOR. LUTFEN BEKLEYIN  ",end="")
for i in range(0,5):
    time.sleep(0.5)
    print(" . ",end="")

# particle sinifi. x,y,z,t,w adli parametreleri aliyor. 
#ayrica icinde denklemden cikan sonucu kaydedecek resutl adli degisken ve minimum pbest degerini bulacak metodlar var
class particle:
    def __init__(self,x,y,z,t,w,result,vx=0,vy=0,vz=0,vt=0,vw=0,pbestx=0,pbesty=0,pbestz=0,pbestt=0,pbestw=0):
        self.x=x
        self.y=y
        self.z=z
        self.t=t
        self.w=w

        self.result=result
        
        self.vx=vx
        self.vy=vy
        self.vz=vz
        self.vt=vt
        self.vw=vw

        self.pbx=[]
        self.pby=[]
        self.pbz=[]
        self.pbt=[]
        self.pbw=[]


        self.pbx.append(self.x)
        self.pby.append(self.y)
        self.pbz.append(self.z)
        self.pbt.append(self.t)
        self.pbw.append(self.w)

        self.pbestx=self.bestx()
        self.pbesty=self.besty()
        self.pbestz=self.bestz()
        self.pbestt=self.bestt()
        self.pbestw=self.bestw()
       
        
    #x icin pbest yani minimum parcacik degerini bulan metod
    def bestx(self):
        alis=[]
        for i in self.pbx:
            result=abs(0-i)
            alis.append(result) 
        
        return min(alis)  


    #y icin pbest yani minimum parcacik degerini bulan metod
    def besty(self):
        alis=[]
        for i in self.pby:
            result=abs(0-i)
            alis.append(result) 
        
        return min(alis)    


    #z icin pbest yani minimum parcacik degerini bulan metod
    def bestz(self):
        alis=[]
        for i in self.pbz:
            result=abs(0-i)
            alis.append(result) 
        
        return min(alis)


    #t icin pbest yani minimum parcacik degerini bulan metod
    def bestt(self):
        alis=[]
        for i in self.pbt:
            result=abs(0-i)
            alis.append(result) 
        
        return min(alis)


    #w icin pbest yani minimum parcacik degerini bulan metod
    def bestw(self):
        alis=[]
        for i in self.pbw:
            result=abs(0-i)
            alis.append(result) 
        
        return min(alis)



# Particle Swarm Optimization Sinifi
class ParticleSwarmOptimization:

    # Constructor. Gbest tüm parcaciklarin degeri icin istenilen en iyi degeri kaydeden degisken.
    # x,y,z,t,w icin ayru ayri degerler tutulmalidir.
    def __init__(self):

        self.gbestx=0
        self.gbesty=0
        self.gbestz=0
        self.gbestt=0
        self.gbestw=0
    
        self.particules=[]
        self.denklemKokleri=[]

        self.rand1=random.randint(0,10)/10
        self.rand2=random.randint(0,10)/10

     
        
    # Parcaciklar bu metodta yaratilir. "count" ile istenilen sayida parcacik ile cözüme ulasilir
    def create_particules(self,count):
        
        eslesme=True

        # eger ayni parcacik 2 defa yaratilirsa hata verip tekrar üretilir.
        # parcaciklarin degerleri farkli olmak zorundadir.
        while(eslesme):
            self.particules.clear()
            for i in range(0,count):
                v1=random.randint(0,10)
                v2=random.randint(0,10)
                v3=random.randint(0,10)
                v4=random.randint(0,10)
                v5=random.randint(0,10)
                self.particules.append(particle(v1,v2,v3,v4,v5,equation(v1,v2,v3,v4,v5)))

            for item,count in collections.Counter(self.particules).items():
                if (count>1):
                    eslesme=True
                else:
                    eslesme=False
        

   

    # sifira en cok yaklasan( istenilen degere ) parcaciklari buluruz
    def closeToZero(self,values):

        if(verbose_mode): # VerboseMode Controlller
            print("-------------------------------")

        alist=[]

        for i in values:
            result=abs(0-i.result)
            alist.append(result)
            if(verbose_mode): # VerboseMode Controlller
                print("resultlar : "+str(result))
    
        mini=min(alist)


        if(verbose_mode):  # VerboseMode Controlller
            print("minimum degeri: " + str(mini))
        
     
        if(mini==0 and verbose_mode):
            print("bu iste bir dogruluk var ")

        for a in values:

            if(verbose_mode):  # VerboseMode Controlller
                print("a resultlari:"+ str(a.result))

            if mini==abs(0-a.result):

                if(verbose_mode):  # VerboseMode Controlller
                    print("eslesme oldu")
                return a
                
                     
           
                

        
    # tüm algoritmanin dayandigi denklem ve teori budur. 
    def particleSwarmEq(self,x,v,pbest,gbest):
        
        vlast=v+2*self.rand1*(pbest-x)+2*self.rand2*(gbest-x)
        return vlast

    # cözüm Metodudur. cözüme ulasmaz ise kontrol degeri 0 olarak geri döndürülür.
    # cözüm icin 3 kez sansi vardir. aksi takdirde program sonsuza kadar döngüye girerek bozulur.
    def solution(self,particules):
        
        kontrol=0

        for aba in range(0,3):
            
            # istenilen amaca (degere) yaklasan en iyi parcacik bulunur.
            gbestval=self.closeToZero(self.particules)
            
            
            # bu parcacik hedefi buldu ise döndüden cikilir
            if(gbestval.result==0):
                if(verbose_mode): # VerboseMode Controlller
                    print(str(gbestval.x)+" "+str(gbestval.y)+" "+str(gbestval.z)+" "+str(gbestval.t)+" "+str(gbestval.w)+" "+str(gbestval.result))
                kontrol=1
                break
            
                
            self.gbestx=gbestval.x
            self.gbesty=gbestval.y
            self.gbestz=gbestval.z
            self.gbestt=gbestval.t
            self.gbestw=gbestval.w
            

  
        


            # optimizasyon algoritmasinin bir parcasi
            for p in self.particules:
                p.vx=self.particleSwarmEq(x=p.x,v=p.vx,pbest=p.bestx(),gbest=self.gbestx)
                p.vy=self.particleSwarmEq(x=p.y,v=p.vy,pbest=p.besty(),gbest=self.gbesty)
                p.vz=self.particleSwarmEq(x=p.z,v=p.vz,pbest=p.bestz(),gbest=self.gbestz)
                p.vt=self.particleSwarmEq(x=p.t,v=p.vt,pbest=p.bestt(),gbest=self.gbestt)
                p.vw=self.particleSwarmEq(x=p.w,v=p.vw,pbest=p.bestw(),gbest=self.gbestw)
                
            self.rand1=random.randint(0,10)/10
            self.rand2=random.randint(0,10)/10

            # optimizasyon algoritmasinin bir parcasi
            for p in self.particules:
                p.x=p.x+p.vx
                p.y=p.y+p.vy
                p.z=p.z+p.vz
                p.t=p.t+p.vt
                p.w=p.w+p.vw
                p.result=equation(p.x,p.y,p.z,p.t,p.w)

        if(verbose_mode):# VerboseMode Controlller
                    
            print("kontrol degeri: " + str(kontrol))
        
        return kontrol,gbestval.x,gbestval.y,gbestval.z,gbestval.t,gbestval.w         
            
   
    # cözüm metodunu yönetir ve sorunu cözer.
    def solve(self,count):
    
        res=0
        # parcaciklar yaratilir
        try:
           self.create_particules(count)
           
        # cözüm denenir. Eger cözüm olmazsa döngü cözene kadar yeniden calisir
        finally:
            res,kokx,koky,kokz,kokt,kokw=self.solution(self.particules)
            while(res==0):
                #time.sleep(0.1)
                try:
                    self.create_particules(count)
                finally:
                    res,kokx,koky,kokz,kokt,kokw=self.solution(self.particules)    

        self.denklemKokleri.append({"x1":kokx,"x2":koky,"x3":kokz,"x4":kokt,"x5":kokw})

        sayac=0
        # bir denklemin sonsuz sayida cözümü olabir. biz simdilik sayaci 5000 yaparak 5000 iterasyon icerisinde en iyi sonuclari bulan bir program yaziyoruz. 
        # bu sayacin degeri arttirilarak daha fazla cözüm bulabiliriz.
        while(self.denklemKokleri.__contains__({"x1":kokx,"x2":koky,"x3":kokz,"x4":kokt,"x5":kokw}) or res==0 and sayac<5000):
            sayac=sayac+1
            try:
                self.create_particules(count)
            finally:
                res,kokx,koky,kokz,kokt,kokw=self.solution(self.particules)
                if(res==1):
                    #bulunan cözüm varsa bunlar denklem köklerine eklenir.
                    self.denklemKokleri.append({"x1":kokx,"x2":koky,"x3":kokz,"x4":kokt,"x5":kokw})  

        if(res==1):
            self.denklemKokleri.append({"x1":kokx,"x2":koky,"x3":kokz,"x4":kokt,"x5":kokw})    
            
        
# ParticleSwarmOptimization sinifindan nesne olusturulur
pso=ParticleSwarmOptimization()

# Denklem 20 adet parcacik ile cözülür. En optimal sonuc elde edilir.
pso.solve(count=20)

# Rastgele bir sonuc döndürülerek denklem kökleri icerinde yine rastgele bir cözüm print edilir.
raN=random.randint(0,int(pso.denklemKokleri.__len__())-1)

print("\n\n\n\n")
# Görsel Kullanici Arayüzü
print("___________________ Verilen Denklem ___________________")
print("|                                                     |")
print("| 11*(x1)^6 - (x2)^4 - 4*(x3)^3 + 3*(x4)^2 - 7*x5 = 7 |")
print("|_____________________________________________________|")
print("|                                                     |")
print("|         Verilen Denklemin "+str(pso.denklemKokleri.__len__())+" cözümü bulundu         |")
print("|                                                     |")
print("|_____________________________________________________|")
print("|                                                     |") 
print("|_________________ Örnek bir cözüm  __________________|")
print("|                                                     |") 
print("|         x1= "+str(pso.denklemKokleri[raN]["x1"]).format(2)+ "  x2= "+str(pso.denklemKokleri[raN]["x2"]).format(2)+"  x3= "+str(pso.denklemKokleri[raN]["x3"]).format(2)+"  x4= "+str(pso.denklemKokleri[raN]["x4"]).format(2)+"  x5= "+str(pso.denklemKokleri[raN]["x5"]).format(2)+"          |")
print("|                                                     |") 
print("|_____________________________________________________|")
print("|                                                     |") 
print("|_____________ Denklemin Diger cözümleri _____________|")
print("\n")


# Bulunan tüm denklem cözümleri yazdirilir. Unutulmamali ki program her calistirildiginda cözümler ve cözüm sayilari farkli olabilir.
for c,i in enumerate(pso.denklemKokleri):
    print("Denklemin "+"{:^3}".format(str(c+1))+" . cözümü : " +"{:^60}".format(str(i))+"\n")









