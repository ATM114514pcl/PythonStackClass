import math
class Stack():
     def __init__(self):
          self.stack=[];
          self.immd0=0;
          self.immd1=0;
     def Set(self,inputData):
          self.stack=inputData;
     def Get(self):
          return self.stack;
     def Push(self,_type,_data):
          try:
               if _type.upper()=="NULL":
                    self.stack.append([None,"nil"])
               elif _type.upper()=="STRING":
                    self.stack.append([str(_data),"str"]);
               elif _type.upper()=="INT":
                    self.stack.append([int(_data),"int"]);
               elif _type.upper()=="FLOAT":
                    self.stack.append([float(_data),"flt"]);
               elif _type.upper()=="BOOL":
                    self.stack.append([bool(_data),"bol"]);
               else:
                    self.stack.append([_data,"Ukn"]);
          except Exception as Err:
               self.stack.append([type(Err).__name__,"err"]);
     def Pop(self):
          try:
               return self.stack.pop();
          except Exception as Err:
               self.stack.append([type(Err).__name__,"err"]);
     @property
     def Bool(self):
          return self._Bool(self);
     class _Bool():
          def __init__(self,owner):
               self.stack=owner.stack;
               self.immd0=0;
               self.immd1=0;
          def And(self):
               try:
                    if self.stack[len(self.stack)-1][1]=="bol" and self.stack[len(self.stack)-2][1]=="bol":
                         self.immd0=self.stack[len(self.stack)-1][0];
                         self.immd1=self.stack[len(self.stack)-2][0];
                         self.stack.append([(self.immd0 and self.immd1),"bol"]);
                         del self.stack[len(self.stack)-2];
                         del self.stack[len(self.stack)-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Or(self):
               try:
                    if self.stack[len(self.stack)-1][1]=="bol" and self.stack[len(self.stack)-2][1]=="bol":
                         self.immd0=self.stack[len(self.stack)-1][0];
                         self.immd1=self.stack[len(self.stack)-2][0];
                         self.stack.append([(self.immd0 or self.immd1),"bol"]);
                         del self.stack[len(self.stack)-2];
                         del self.stack[len(self.stack)-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Not(self):
               try:
                    if self.stack[len(self.stack)-1][1]=="bol":
                         self.immd0=self.stack[len(self.stack)-1][0];
                         self.stack.append([(not self.immd0),"bol"]);
                         del self.stack[len(self.stack)-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
     @property
     def Math(self):
          return self._Math(self);
     class _Math():
          def __init__(self,owner):
               self.stack=owner.stack;
               self.immd0=0;
               self.immd1=0;
          def Add(self):
               try:
                    if (self.stack[len(self.stack)-1][1] in ["int","flt"]) and (self.stack[len(self.stack)-2][1] in ["int","flt"]):
                         self.immd0=self.stack[len(self.stack)-1][0]+self.stack[len(self.stack)-2][0];
                         if self.stack[len(self.stack)-1][1]=="flt" or self.stack[len(self.stack)-2][1]=="flt":
                              self.immd1="flt";
                              self.immd0=float(self.immd0);
                         else:
                              self.immd1="int";
                              self.immd0=int(self.immd0);
                         self.stack.append([self.immd0,self.immd1]);
                         del self.stack[len(self.stack)-2];
                         del self.stack[len(self.stack)-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Sub(self):
               try:
                    if (self.stack[len(self.stack)-1][1] in ["int","flt"]) and (self.stack[len(self.stack)-2][1] in ["int","flt"]):
                         self.immd0=self.stack[len(self.stack)-2][0]-self.stack[len(self.stack)-1][0];
                         if self.stack[len(self.stack)-1][1]=="flt" or self.stack[len(self.stack)-2][1]=="flt":
                              self.immd1="flt";
                              self.immd0=float(self.immd0);
                         else:
                              self.immd1="int";
                              self.immd0=int(self.immd0);
                         self.stack.append([self.immd0,self.immd1]);
                         del self.stack[len(self.stack)-2];
                         del self.stack[len(self.stack)-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Mul(self):
               try:
                    if (self.stack[len(self.stack)-1][1] in ["int","flt"]) and (self.stack[len(self.stack)-2][1] in ["int","flt"]):
                         self.immd0=self.stack[len(self.stack)-1][0]*self.stack[len(self.stack)-2][0];
                         if self.stack[len(self.stack)-1][1]=="flt" or self.stack[len(self.stack)-2][1]=="flt":
                              self.immd1="flt";
                              self.immd0=float(self.immd0);
                         else:
                              self.immd1="int";
                              self.immd0=int(self.immd0);
                         self.stack.append([self.immd0,self.immd1]);
                         del self.stack[len(self.stack)-2];
                         del self.stack[len(self.stack)-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Div(self):
               try:
                    if (self.stack[len(self.stack)-1][1] in ["int","flt"]) and (self.stack[len(self.stack)-2][1] in ["int","flt"]):
                         self.stack.append([float((self.stack[len(self.stack)-2][0])/(self.stack[len(self.stack)-1][0])),"flt"]);
                         del self.stack[len(self.stack)-2];
                         del self.stack[len(self.stack)-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Pi(self):
               self.stack.append([math.pi,"flt"]);
               
