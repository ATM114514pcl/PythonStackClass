import math
import copy
class Stack():
     def __init__(self):
          self.stack=[];
          self.immd0=0;
          self.immd1=0;
     def Set(self,inputData):
          self.stack=inputData;
     def Get(self):
          return self.stack;
     def Push(self,Type,Data):
          try:
               if Type.upper()=="NULL":
                    self.stack.append([None,"nil"])
               elif Type.upper()=="STRING":
                    self.stack.append([str(Data),"str"]);
               elif Type.upper()=="INT":
                    self.stack.append([int(Data),"int"]);
               elif Type.upper()=="FLOAT":
                    self.stack.append([float(Data),"flt"]);
               elif Type.upper()=="BOOL":
                    self.stack.append([bool(Data),"bol"]);
               else:
                    self.stack.append([Data,"ukn"]);
          except Exception as Err:
               self.stack.append([type(Err).__name__,"err"]);
     def Pop(self):
          try:
               return self.stack.pop();
          except Exception as Err:
               self.stack.append([type(Err).__name__,"err"]);
     def Copy(self):
          try:
               self.stack.append(copy.deepcopy(self.stack[-1]));
          except Exception as Err:
               self.stack.append([type(Err).__name__,"err"]);
     def Swap(self,target0,target1):
          try:
               self.immd0=self.stack[target0];
               self.immd1=self.stack[target1];
               self.stack[target0]=self.immd1;
               self.stack[target1]=self.immd0;
          except Exception as Err:
               self.stack.append([type(Err).__name__,"err"]);
     def Delete(self,target):
          try:
               del self.stack[target];
          except Exception as Err:
               self.stack.append([type(Err).__name__,"err"]);
     def Convert(self,Type):
          try:
               if Type.upper()=="NULL":
                    self.stack.append([None,"nil"])
               elif Type.upper()=="STRING":
                    self.stack.append([str(self.stack[-1][0]),"str"]);
               elif Type.upper()=="INT":
                    self.stack.append([int(self.stack[-1][0]),"int"]);
               elif Type.upper()=="FLOAT":
                    self.stack.append([float(self.stack[-1][0]),"flt"]);
               elif Type.upper()=="BOOL":
                    self.stack.append([bool(self.stack[-1][0]),"bol"]);
               else:
                    self.stack.append([self.stack[-1][0],"ukn"]);
               del self.stack[-2];
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
                         self.immd0=self.stack[-1][0];
                         self.immd1=self.stack[-2][0];
                         self.stack.append([(self.immd0 and self.immd1),"bol"]);
                         del self.stack[-3:-1];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Or(self):
               try:
                    if self.stack[len(self.stack)-1][1]=="bol" and self.stack[len(self.stack)-2][1]=="bol":
                         self.immd0=self.stack[-1][0];
                         self.immd1=self.stack[-2][0];
                         self.stack.append([(self.immd0 or self.immd1),"bol"]);
                         del self.stack[-3:-1];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Not(self):
               try:
                    if self.stack[len(self.stack)-1][1]=="bol":
                         self.immd0=self.stack[-1][0];
                         self.stack.append([(not self.immd0),"bol"]);
                         del self.stack[-2];
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
                    if (self.stack[-1][1] in ["int","flt"]) and (self.stack[-2][1] in ["int","flt"]):
                         self.immd0=self.stack[-1][0]+self.stack[-2][0];
                         if self.stack[-1][1]=="flt" or self.stack[-2][1]=="flt":
                              self.immd1="flt";
                              self.immd0=float(self.immd0);
                         else:
                              self.immd1="int";
                              self.immd0=int(self.immd0);
                         self.stack.append([self.immd0,self.immd1]);
                         del self.stack[-3:-1];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Sub(self):
               try:
                    if (self.stack[-1][1] in ["int","flt"]) and (self.stack[-2][1] in ["int","flt"]):
                         self.immd0=self.stack[-2][0]-self.stack[-1][0];
                         if self.stack[-1][1]=="flt" or self.stack[-2][1]=="flt":
                              self.immd1="flt";
                              self.immd0=float(self.immd0);
                         else:
                              self.immd1="int";
                              self.immd0=int(self.immd0);
                         self.stack.append([self.immd0,self.immd1]);
                         del self.stack[-3:-1];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Mul(self):
               try:
                    if (self.stack[-1][1] in ["int","flt"]) and (self.stack[-2][1] in ["int","flt"]):
                         self.immd0=self.stack[-1][0]*self.stack[-2][0];
                         if self.stack[-1][1]=="flt" or self.stack[-2][1]=="flt":
                              self.immd1="flt";
                              self.immd0=float(self.immd0);
                         else:
                              self.immd1="int";
                              self.immd0=int(self.immd0);
                         self.stack.append([self.immd0,self.immd1]);
                         del self.stack[-3:-1];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Div(self):
               try:
                    if (self.stack[-1][1] in ["int","flt"]) and (self.stack[-2][1] in ["int","flt"]):
                         self.immd0=float((self.stack[-2][0])/(self.stack[-1][0]));
                         self.stack.append([self.immd0,"flt"]);
                         del self.stack[-3:-1];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Pi(self):
               self.stack.append([math.pi,"flt"]);
               return;
          def Sqrt(self):
               try:
                    if self.stack[-1][1] in ["int","flt"]:
                         self.immd0=math.sqrt(self.stack[-1][0]);
                         self.stack.append([self.immd0,"flt"]);
                         del self.stack[-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Sin(self):
               try:
                    if self.stack[-1][1] in ["int","flt"]:
                         self.immd0=math.sin(self.stack[-1][0]);
                         self.stack.append([self.immd0,"flt"]);
                         del self.stack[-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Asin(self):
               try:
                    if self.stack[-1][1] in ["int","flt"]:
                         self.immd0=math.asin(self.stack[-1][0]);
                         self.stack.append([self.immd0,"flt"]);
                         del self.stack[-2];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
     @property
     def Vector(self):
          return self._Vector(self);
     class _Vector():
          def __init__(self,owner):
               self.stack=owner.stack;
               self.immd0=0;
               self.immd1=0;
               self.immd2=0;
          def Combine(self):
               try:
                    self.immd0=(self.stack[-1][1] in ["int","flt"]) and (self.stack[-2][1] in ["int","flt"]);
                    self.immd1=(self.stack[-3][1] in ["int","flt"]) and (self.stack[-4][1] in ["int","flt"]);
                    if self.immd0 and self.immd1:
                         self.immd2=[self.stack[-4][0],];
                         self.immd2.append(self.stack[-3][0]);
                         self.immd2.append(self.stack[-2][0]);
                         self.immd2.append(self.stack[-1][0]);
                         self.stack.append([self.immd2,"vec"]);
                         del self.stack[-5:-1];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
          def Split(self):
               try:
                    if self.stack[-1][1]=="vec" and len(self.stack[-1][]0)==4:
                         self.immd0=self.stack[-1][0];
                         self.stack.append([self.immd0[0],"flt"]);
                         self.stack.append([self.immd0[1],"flt"]);
                         self.stack.append([self.immd0[2],"flt"]);
                         self.stack.append([self.immd0[3],"flt"]);
                         del self.stack[-5];
                         return;
                    else:
                         self.stack.append([None,"nil"]);
                         return;
               except Exception as Err:
                    self.stack.append([type(Err).__name__,"err"]);
