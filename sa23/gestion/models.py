from django.db import models

class Etudiant(models.Model):

    nom = models.CharField(max_length = 100)
    prenom =models.CharField(max_length = 100,null = True)
    groupe =models.CharField(max_length = 100,null = True)
    photo =models.CharField(max_length = 100,null = True)
    email=models.EmailField(default=None,max_length = 100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,"prenom": self.prenom,"groupe": self.groupe,"photo": self.photo," email": self. email,}





class Examens(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateField(blank=True, null = True)
    coefficient = models.CharField(max_length=100)
    ressources = models.ForeignKey('Ressources', on_delete=models.CASCADE,null = True,)

    def __str__(self):
        return  self.titre

    def dico(self):
        return {"titre": self.titre,"date": self.date, "coefficient": self.coefficient,"ressources": self.ressources,}


class Notes(models.Model):
    examens = models.ForeignKey('Examens', on_delete=models.CASCADE,null = True,)
    etudiant =models.CharField(max_length=100)
    note =models.IntegerField(blank=False, null=True)
    appreciation =models.CharField(max_length=100)


    def __str__(self):
        return self.etudiant


    def dico(self):
        return {"examens": self.examens, "note": self.note, "etudiant": self.etudiant, "appreciation": self.appreciation, }


######################################

class UE(models.Model):
    code = models.IntegerField(blank=False, null=True)
    nom = models.CharField(max_length=100)
    semestre = models.IntegerField(blank=False, null=True)
    credit = models.CharField(max_length=100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,"code": self.code,"semestre": self.semestre, "credit": self.credit,}

class Ressources(models.Model):
    code_ressource = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)
    coefficient = models.CharField(max_length=100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"code_ressource": self.code_ressource,"nom": self.nom,"descriptif": self.descriptif, "coefficient": self.coefficient}

class Enseignant(models.Model):

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return  self.nom

    def dico(self):
        return {"nom": self.nom,"prenom": self.prenom,}

