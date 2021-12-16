from django.db import models


# Create your models here.


class Infirmieres(models.Model):
    numero_inami = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse_mail = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=50)
    numero_telephone = models.IntegerField()
    id_adresse = models.ForeignKey(
        'Adresse',
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.numero_inami


class Adresse(models.Model):
    id_adresse = models.IntegerField(primary_key=True)
    rue = models.CharField(max_length=100)
    ville = models.CharField(max_length=50)
    code_postal = models.IntegerField()


class Anamnese(models.Model):
    id_anamnese = models.IntegerField(primary_key=True)
    pulsation = models.IntegerField()
    oxygene = models.CharField(max_length=4)
    tension = models.CharField(max_length=4)


class Equipe(models.Model):
    numero_inami_groupe = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    numero_inami = models.ForeignKey(
        'Infirmieres',
        on_delete=models.CASCADE,
    )


class Patient(models.Model):
    nn_patient = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numero_telephone = models.IntegerField()
    nn_perso_contact = models.IntegerField()
    id_adresse = models.ForeignKey(
        'Adresse',
        on_delete=models.CASCADE,
    )


class Fiche(models.Model):
    id_tournees = models.ForeignKey(
        'Tournees',
        on_delete=models.CASCADE,
    )
    id_soins = models.ForeignKey(
        'Soins',
        on_delete=models.CASCADE,
    )
    nn_patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
    )


class Kine(models.Model):
    nn_inami = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numero_telephone = models.IntegerField()
    nn_patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
    )
    id_adresse = models.ForeignKey(
        'Adresse',
        on_delete=models.CASCADE,
    )


class Medecin(models.Model):
    nn_inami = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numero_telephone = models.IntegerField()
    id_adresse = models.ForeignKey(
        'Adresse',
        on_delete=models.CASCADE,
    )


class Mutuelles(models.Model):
    numero_mutuelle = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    nn_patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
    )
    id_adresse = models.ForeignKey(
        'Adresse',
        on_delete=models.CASCADE,
    )


class NumeroTournee(models.Model):
    numero_inami = models.ForeignKey(
        'Infirmieres',
        on_delete=models.CASCADE,
    )
    id_tournees = models.ForeignKey(
        'Tournees',
        on_delete=models.CASCADE,
    )


class Tournees(models.Model):
    id_tournees = models.IntegerField(primary_key=True)
    date = models.DateField()


class Passages(models.Model):
    id_passages = models.IntegerField(primary_key=True)
    heure_theorique = models.TimeField()
    heure_reelle = models.TimeField()
    id_tournees = models.ForeignKey(
        'Tournees',
        on_delete=models.CASCADE,
    )


class Prescription(models.Model):
    numero_prescription = models.IntegerField(primary_key=True)
    justificatif = models.CharField(max_length=150)
    date_prescription = models.DateField()
    date_fin = models.DateField()
    nn_inami = models.ForeignKey(
        'Medecin',
        on_delete=models.CASCADE,
    )


class Rapport(models.Model):
    id_rapport = models.IntegerField(primary_key=True)
    observation = models.CharField(max_length=200)
    id_anamnese = models.ForeignKey(
        'Anamnese',
        on_delete=models.CASCADE,
    )


class Soins(models.Model):
    id_soins = models.IntegerField(primary_key=True)
    libelle = models.CharField(max_length=100)
    nomenclature = models.CharField(max_length=100)
    id_prescription = models.ForeignKey(
        'Prescription',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.id_soins
