class mycomplexnumber:
    def _init_(self,real=0,img=0):
        self.real_part=real
        self.img_part=img
    def displaycomplex(self):
                print("{}+{}j".format(self.real_part,self.img_part))
com1=mycomplexnumber(61,60)
com1.displaycomplex()
