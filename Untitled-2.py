class F15:
    def light(self):
        print("ok switching on lights")
    def fan(self,speed):
        print("switch on the fan and the speed is",speed)
        self.s=speed
    def ac(self):
        print("switch on ac")
        print(self.s)
sudheer=F15()
sudheer.light()
sudheer.fan(5)
sudheer.ac()
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    