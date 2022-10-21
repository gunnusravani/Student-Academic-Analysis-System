from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.CharField(max_length=200,primary_key=True)
    Name = models.CharField(max_length=250)
    SGPA_1_1= models.FloatField(null=True)
    SGPA_1_2= models.FloatField(null=True)
    SGPA_2_1= models.FloatField(null=True)
    SGPA_2_2= models.FloatField(null=True)
    SGPA_3_1= models.FloatField(null=True)
    SGPA_3_2= models.FloatField(null=True)
    SGPA_4_1= models.FloatField(null=True)
    SGPA_4_2= models.FloatField(null=True)
    CGPA = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.roll_no)

R19={'O':10.0,'S':9.0,'A':8.0,'B':7.0,'C':6.0,'D':5.0,'F':0.0,'COMPLETED':0.0,'COMPLE':0.0}
R20={'A+':10.0,'A':9.0,'B':8.0,'C':7.0,'D':6.0,'E':5.0,'F':0.0,'COMPLETED':0.0,'COMPLE':0.0}

class Results_1_1(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):
        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_1_1, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)

class Results_1_2(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):
        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_1_2, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)
    

class Results_2_1(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):
       
        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_2_1, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)

class Results_2_2(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):
        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_2_2, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)


    
class Results_3_1(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):
        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_3_1, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)  
    

class Results_3_2(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):

        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_3_2, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)

class Results_4_1(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):
        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_4_1, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)

class Results_4_2(models.Model):
    Htno =models.ForeignKey('Student', on_delete=models.CASCADE,)
    Subcode =models.CharField(max_length=200)
    Subname=models.CharField(max_length=250)
    Grade=models.CharField(max_length=200)
    Credits=models.FloatField()
    Grade_Points=models.FloatField(default=0)
    
    @property
    def get_grade(self):
        Roll=[j for j in str(self.Htno)]
        if(''.join(Roll[0:2])=='19' or (''.join(Roll[4:6])=='20' and ''.join(Roll[4:6])=='5A') ):
            a = R19[self.Grade]
            return a
        else:
            b = R20[self.Grade]
            return b
    def save(self, *args, **kwargs):
          self.Grade_Points = self.get_grade
          super(Results_4_2, self).save(*args, **kwargs) 
    #exam_type=models.CharField(max_length=10,null=True)

    def __str__ (self):
        return str(self.Htno)

    class Meta:
        unique_together = (("Htno", "Subcode"),)

#mid tabels

class Subjects(models.Model):
    Subcode=models.CharField(max_length=50,primary_key=True)
    Subname=models.CharField(max_length=50,)

    def _str_(self):
        return str(self.Subcode)



class Mid_1_1(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)


class Mid_1_2(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)


class Mid_2_1(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)    


class Mid_2_2(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)


class Mid_3_1(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)


class Mid_3_2(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)

class Mid_4_1(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)

class Mid_4_2(models.Model):
    HTNO =models.ForeignKey('Student', on_delete=models.CASCADE,)
    SUBJECT=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    Subname=models.CharField(max_length=100)
    MID_1=models.IntegerField()
    quiz_1=models.IntegerField()
    assign_1 = models.IntegerField()
    MID_2 = models.IntegerField()
    quiz_2=models.IntegerField()
    assign_2 = models.IntegerField()
    DLS = models.IntegerField()
    Total= models.IntegerField()
    SUB_TYPE = models.CharField(max_length=10)

    def _str_(self):
        return str(self.HTNO)

