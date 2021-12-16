from rest_framework import serializers
from InfirmiereApp.models import Infirmieres, Soins, Rapport, Prescription, \
    Passages, Tournees, NumeroTournee, Mutuelles, Medecin, Kine, Fiche, Patient, Equipe, Anamnese, Adresse


class InfirmieresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infirmieres
        fields = ('numero_inami', 'nom', 'prenom', 'adresse_mail', 'mot_de_passe', 'numero_telephone', 'id_adresse')


class SoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soins
        fields = ('id_soins', 'libelle', 'nomenclature', 'id_prescription')


class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = ('id_rapport', 'observation', 'id_anamnese', 'nn_patient')


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('numero_prescription', 'justificatif', 'date_prescription', 'date_fin', 'nn_inami')


class PassagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passages
        fields = ('id_passages', 'heure_theorique', 'heure_reelle', 'id_tournees')


class TourneesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournees
        fields = ('id_tournees', 'date')


class NumeroTourneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumeroTournee
        fields = ('numero_inami', 'id_tournees')


class MutuellesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mutuelles
        fields = ('numero_mutuelles', 'nom', 'nn_patient', 'id_adresse')


class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = ('nn_inami', 'nom', 'prenom', 'numero_telephone', 'id_adresse')


class KineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kine
        fields = ('nn_inami', 'nom', 'prenom', 'numero_telephone', 'nn_patient', 'id_adresse')


class FicheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiche
        fields = ('id_tournees', 'id_soins', 'nn_patient')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('nn_patient', 'nom', 'prenom', 'numero_telephone', 'nn_perso_contact', 'id_adresse')


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ('numero_inami_groupe', 'nom', 'numero_inami')


class AnamneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnese
        fields = ('id_anamnese', 'pulsation', 'oxygene', 'tension')


class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id_adresse', 'rue', 'ville', 'code_postal')
