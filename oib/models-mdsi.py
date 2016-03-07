# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AdmIpsstation(models.Model):
    iid = models.BigIntegerField(db_column='IID', primary_key=True)  # Field name made lowercase.
    ipscode = models.CharField(db_column='IPSCode', unique=True, max_length=25)  # Field name made lowercase.
    ipsname = models.CharField(db_column='IPSName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipsplz = models.CharField(db_column='IPSPLZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ipsort = models.CharField(db_column='IPSOrt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ipsinfo = models.CharField(db_column='IPSInfo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipssort = models.CharField(db_column='IPSSort', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aktiv = models.CharField(db_column='Aktiv', max_length=2)  # Field name made lowercase.
    spital = models.CharField(db_column='Spital', max_length=100, blank=True, null=True)  # Field name made lowercase.
    strasse = models.CharField(db_column='Strasse', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_ipsstation'


class AdmPersonal(models.Model):
    uid = models.BigIntegerField(db_column='UID', primary_key=True)  # Field name made lowercase.
    ipscode = models.CharField(db_column='IPSCode', max_length=25)  # Field name made lowercase.
    titel = models.CharField(db_column='Titel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vorname = models.CharField(db_column='Vorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    arztnummer = models.CharField(db_column='ArztNummer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arztsort = models.CharField(db_column='ArztSort', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spitaltelefond = models.CharField(db_column='SpitalTelefonD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spitaltelefon = models.CharField(db_column='SpitalTelefon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eintrittdatum = models.CharField(db_column='EintrittDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', unique=True, max_length=15)  # Field name made lowercase.
    loginname = models.CharField(db_column='LoginName', unique=True, max_length=45)  # Field name made lowercase.
    passwort = models.CharField(db_column='Passwort', max_length=45)  # Field name made lowercase.
    passwortstamp = models.CharField(db_column='PasswortStamp', max_length=14, blank=True, null=True)  # Field name made lowercase.
    passwortchange = models.CharField(db_column='PasswortChange', max_length=2)  # Field name made lowercase.
    zuprofil = models.CharField(db_column='ZuProfil', max_length=45)  # Field name made lowercase.
    sprache = models.CharField(db_column='Sprache', max_length=2)  # Field name made lowercase.
    aktiv = models.CharField(db_column='Aktiv', max_length=2)  # Field name made lowercase.
    anrede = models.CharField(db_column='Anrede', max_length=45, blank=True, null=True)  # Field name made lowercase.
    stellung = models.CharField(db_column='Stellung', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spitalfax = models.CharField(db_column='SpitalFax', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_personal'


class AdmProfil2Site(models.Model):
    rid = models.BigIntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    zuprofil = models.CharField(db_column='ZuProfil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zusite = models.CharField(db_column='zuSite', max_length=45, blank=True, null=True)  # Field name made lowercase.
    menulink = models.CharField(db_column='MenuLink', max_length=45)  # Field name made lowercase.
    ipzuprofil = models.CharField(db_column='IPzuProfil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    logread = models.CharField(db_column='LogRead', max_length=2, blank=True, null=True)  # Field name made lowercase.
    logwrite = models.CharField(db_column='LogWrite', max_length=2, blank=True, null=True)  # Field name made lowercase.
    logadmin = models.CharField(db_column='LogAdmin', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_profil2site'


class DatDrg(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ipscode = models.CharField(db_column='IPSCode', max_length=25)  # Field name made lowercase.
    pd_patid = models.CharField(db_column='PD_PatID', max_length=45)  # Field name made lowercase.
    pd_fid = models.CharField(db_column='PD_FID', max_length=45)  # Field name made lowercase.
    p_beatm = models.CharField(db_column='P_Beatm', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_schwere = models.CharField(db_column='P_Schwere', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_scoreart = models.CharField(db_column='P_ScoreArt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_nemsalle = models.CharField(db_column='P_NemsAlle', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_ecmo = models.CharField(db_column='P_ECMO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_no = models.CharField(db_column='P_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_los = models.CharField(db_column='P_LOS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    del_field = models.CharField(db_column='Del', max_length=2)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    fid = models.BigIntegerField(db_column='FID')  # Field name made lowercase.
    mutdatum = models.CharField(db_column='MutDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pd_gebdat = models.CharField(db_column='PD_GebDat', max_length=8, blank=True, null=True)  # Field name made lowercase.
    pd_sex = models.CharField(db_column='PD_Sex', max_length=1)  # Field name made lowercase.
    expstatus = models.CharField(db_column='ExpStatus', max_length=2)  # Field name made lowercase.
    expdatum = models.CharField(db_column='ExpDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mutts = models.CharField(db_column='MUTTS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insts = models.CharField(db_column='INSTS', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dat_drg'


class DatMdsi(models.Model):
    mid = models.BigIntegerField(db_column='MID', primary_key=True)  # Field name made lowercase.
    ipscode = models.CharField(db_column='IPSCode', max_length=25)  # Field name made lowercase.
    m_mdsid = models.CharField(db_column='M_MDSID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    m_alter = models.IntegerField(db_column='M_Alter', blank=True, null=True)  # Field name made lowercase.
    m_einheit = models.CharField(db_column='M_Einheit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sex = models.CharField(db_column='M_Sex', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_gebgew = models.CharField(db_column='M_GebGew', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_gestalter = models.CharField(db_column='M_GestAlter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_wiederein = models.CharField(db_column='M_WiederEin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_woher = models.CharField(db_column='M_Woher', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_wo = models.CharField(db_column='M_Wo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_eintritt = models.CharField(db_column='M_Eintritt', max_length=14, blank=True, null=True)  # Field name made lowercase.
    m_los = models.CharField(db_column='M_LOS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_wohin = models.CharField(db_column='M_Wohin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_patgrp = models.CharField(db_column='M_PatGrp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_diag1 = models.CharField(db_column='M_Diag1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_diagv = models.CharField(db_column='M_DiagV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_isskopf = models.CharField(db_column='M_ISSKopf', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_issface = models.CharField(db_column='M_ISSFace', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_issthorax = models.CharField(db_column='M_ISSThorax', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_issabdomen = models.CharField(db_column='M_ISSAbdomen', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_issextremity = models.CharField(db_column='M_ISSExtremity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_issextern = models.CharField(db_column='M_ISSExtern', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_interv = models.CharField(db_column='M_Interv', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_schwere = models.CharField(db_column='M_Schwere', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_scoreart = models.CharField(db_column='M_ScoreArt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_nemsalle = models.CharField(db_column='M_NemsAlle', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_nems1 = models.CharField(db_column='M_Nems1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_nemsletz = models.CharField(db_column='M_NemsLetz', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sasanz4 = models.CharField(db_column='M_SASAnz4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sasanz5 = models.CharField(db_column='M_SASAnz5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sasanz6 = models.CharField(db_column='M_SASAnz6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sgi1a = models.CharField(db_column='M_SGI1A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sgi1b = models.CharField(db_column='M_SGI1B', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sgi2 = models.CharField(db_column='M_SGI2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_sgi3 = models.CharField(db_column='M_SGI3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_monit = models.CharField(db_column='M_Monit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_mediint = models.CharField(db_column='M_Mediint', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_beatm = models.CharField(db_column='M_Beatm', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_atemh = models.CharField(db_column='M_Atemh', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_evasoa = models.CharField(db_column='M_EVasoa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_mvasoa = models.CharField(db_column='M_MVasoa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_nieren = models.CharField(db_column='M_Nieren', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_ipsinterv = models.CharField(db_column='M_IPSInterv', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_trans = models.CharField(db_column='M_Trans', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_austritt = models.CharField(db_column='M_Austritt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_out28d = models.CharField(db_column='M_OUT28D', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_out1y = models.CharField(db_column='M_OUT1Y', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rechjahr = models.CharField(db_column='RechJahr', max_length=4)  # Field name made lowercase.
    rechquart = models.CharField(db_column='RechQuart', max_length=4)  # Field name made lowercase.
    rechmonat = models.CharField(db_column='RechMonat', max_length=4)  # Field name made lowercase.
    rechwoche = models.CharField(db_column='RechWoche', max_length=4)  # Field name made lowercase.
    m_del = models.CharField(db_column='M_Del', max_length=2)  # Field name made lowercase.
    mutdatum = models.CharField(db_column='MutDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    expstatus = models.CharField(db_column='ExpStatus', max_length=2)  # Field name made lowercase.
    expdatum = models.CharField(db_column='ExpDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    fid = models.CharField(db_column='FID', max_length=25)  # Field name made lowercase.
    m_tot_tiss = models.CharField(db_column='M_Tot_Tiss', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_tot_sapsd = models.CharField(db_column='M_Tot_SAPSD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dat_mdsi'


class DatPatfall(models.Model):
    fid = models.BigIntegerField(db_column='FID', primary_key=True)  # Field name made lowercase.
    pd_fid = models.CharField(db_column='PD_FID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pd_gebdat = models.CharField(db_column='PD_GebDat', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pd_sex = models.CharField(db_column='PD_Sex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pd_gestalter = models.CharField(db_column='PD_GestAlter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_gebgew = models.CharField(db_column='PD_GebGew', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_eindat = models.CharField(db_column='PD_EinDat', max_length=14)  # Field name made lowercase.
    pd_woher = models.CharField(db_column='PD_Woher', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_vonwo = models.CharField(db_column='PD_VonWo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_ausdat = models.CharField(db_column='PD_AusDat', max_length=14)  # Field name made lowercase.
    pd_wohin = models.CharField(db_column='PD_Wohin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_patid = models.CharField(db_column='PD_PatID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pd_name = models.CharField(db_column='PD_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pd_vorname = models.CharField(db_column='PD_Vorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pd_bett = models.CharField(db_column='PD_Bett', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_klasse = models.CharField(db_column='PD_Klasse', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_gruppe = models.CharField(db_column='PD_Gruppe', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pd_opdat = models.CharField(db_column='PD_OPDat', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pd_optext = models.CharField(db_column='PD_OPText', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pd_wohnort = models.CharField(db_column='PD_Wohnort', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pd_kanton = models.CharField(db_column='PD_Kanton', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pd_telefon = models.CharField(db_column='PD_Telefon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pd_einbericht = models.TextField(db_column='PD_EinBericht', blank=True, null=True)  # Field name made lowercase.
    pd_ausbericht = models.TextField(db_column='PD_AusBericht', blank=True, null=True)  # Field name made lowercase.
    di_plan = models.CharField(db_column='DI_Plan', max_length=10, blank=True, null=True)  # Field name made lowercase.
    di_diag1 = models.CharField(db_column='DI_Diag1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    di_diag1text = models.CharField(db_column='DI_Diag1Text', max_length=200, blank=True, null=True)  # Field name made lowercase.
    di_interv = models.CharField(db_column='DI_Interv', max_length=10, blank=True, null=True)  # Field name made lowercase.
    di_diagverl = models.CharField(db_column='DI_DiagVerl', max_length=10, blank=True, null=True)  # Field name made lowercase.
    di_wiederein = models.CharField(db_column='DI_WiederEin', max_length=2)  # Field name made lowercase.
    diiss_kopf = models.CharField(db_column='DIISS_Kopf', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diiss_face = models.CharField(db_column='DIISS_Face', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diiss_thorax = models.CharField(db_column='DIISS_Thorax', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diiss_abdomen = models.CharField(db_column='DIISS_Abdomen', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diiss_extremity = models.CharField(db_column='DIISS_Extremity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diiss_extern = models.CharField(db_column='DIISS_Extern', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diiss_score = models.IntegerField(db_column='DIISS_Score', blank=True, null=True)  # Field name made lowercase.
    dip_einplan = models.CharField(db_column='DIP_EinPlan', max_length=10)  # Field name made lowercase.
    dip_postop = models.CharField(db_column='DIP_PostOp', max_length=10)  # Field name made lowercase.
    dip_hlm = models.CharField(db_column='DIP_HLM', max_length=10)  # Field name made lowercase.
    dip_riskho = models.CharField(db_column='DIP_RiskHo', max_length=10)  # Field name made lowercase.
    dip_riskti = models.CharField(db_column='DIP_RiskTi', max_length=10)  # Field name made lowercase.
    dip_pupill = models.CharField(db_column='DIP_Pupill', max_length=10)  # Field name made lowercase.
    dip_atmung = models.CharField(db_column='DIP_Atmung', max_length=10)  # Field name made lowercase.
    dip_bd = models.IntegerField(db_column='DIP_BD', blank=True, null=True)  # Field name made lowercase.
    dip_base = models.IntegerField(db_column='DIP_Base', blank=True, null=True)  # Field name made lowercase.
    dip_fio2 = models.IntegerField(db_column='DIP_FiO2', blank=True, null=True)  # Field name made lowercase.
    dip_mort = models.CharField(db_column='DIP_Mort', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dic_cribii = models.IntegerField(db_column='DIC_CribII', blank=True, null=True)  # Field name made lowercase.
    dic_wo = models.CharField(db_column='DIC_Wo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dic_gew = models.IntegerField(db_column='DIC_Gew', blank=True, null=True)  # Field name made lowercase.
    dis2_alter = models.CharField(db_column='DIS2_Alter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_herzf = models.CharField(db_column='DIS2_Herzf', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_bd = models.CharField(db_column='DIS2_BD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_temp = models.CharField(db_column='DIS2_Temp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_fio2 = models.CharField(db_column='DIS2_FiO2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_po2 = models.CharField(db_column='DIS2_PO2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_urin = models.CharField(db_column='DIS2_Urin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_harn = models.CharField(db_column='DIS2_Harn', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_leuk = models.CharField(db_column='DIS2_Leuk', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_kali = models.CharField(db_column='DIS2_Kali', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_natri = models.CharField(db_column='DIS2_Natri', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_bikar = models.CharField(db_column='DIS2_Bikar', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_bilir = models.CharField(db_column='DIS2_Bilir', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_gcs = models.CharField(db_column='DIS2_GCS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_chron = models.CharField(db_column='DIS2_Chron', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_aufn = models.CharField(db_column='DIS2_Aufn', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dis2_score = models.IntegerField(db_column='DIS2_Score', blank=True, null=True)  # Field name made lowercase.
    dis2_mort = models.CharField(db_column='DIS2_Mort', max_length=10, blank=True, null=True)  # Field name made lowercase.
    out_spital = models.CharField(db_column='OUT_Spital', max_length=10, blank=True, null=True)  # Field name made lowercase.
    out_28d = models.CharField(db_column='OUT_28D', max_length=10, blank=True, null=True)  # Field name made lowercase.
    out_1y = models.CharField(db_column='OUT_1Y', max_length=10, blank=True, null=True)  # Field name made lowercase.
    out_1yquali = models.CharField(db_column='OUT_1YQuali', max_length=10, blank=True, null=True)  # Field name made lowercase.
    del_field = models.CharField(db_column='Del', max_length=2)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mutstatus = models.CharField(db_column='MutStatus', max_length=2)  # Field name made lowercase.
    mutdatum = models.CharField(db_column='MutDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    loct_01 = models.CharField(db_column='LOCT_01', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_02 = models.CharField(db_column='LOCT_02', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_03 = models.CharField(db_column='LOCT_03', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_04 = models.CharField(db_column='LOCT_04', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_05 = models.CharField(db_column='LOCT_05', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_06 = models.CharField(db_column='LOCT_06', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_07 = models.CharField(db_column='LOCT_07', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_08 = models.CharField(db_column='LOCT_08', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_09 = models.CharField(db_column='LOCT_09', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_10 = models.CharField(db_column='LOCT_10', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_11 = models.CharField(db_column='LOCT_11', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_12 = models.CharField(db_column='LOCT_12', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_13 = models.CharField(db_column='LOCT_13', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_14 = models.CharField(db_column='LOCT_14', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_15 = models.CharField(db_column='LOCT_15', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_16 = models.CharField(db_column='LOCT_16', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_17 = models.CharField(db_column='LOCT_17', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_18 = models.CharField(db_column='LOCT_18', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_19 = models.CharField(db_column='LOCT_19', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_20 = models.CharField(db_column='LOCT_20', max_length=250, blank=True, null=True)  # Field name made lowercase.
    di_intervtext = models.CharField(db_column='DI_IntervText', max_length=200, blank=True, null=True)  # Field name made lowercase.
    diiss_wirbel = models.CharField(db_column='DIISS_Wirbel', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mutmeld = models.CharField(db_column='MutMeld', max_length=600, blank=True, null=True)  # Field name made lowercase.
    to_mdsi = models.CharField(db_column='TO_MDSI', max_length=2)  # Field name made lowercase.
    m_hospeindat = models.CharField(db_column='M_HospEinDat', max_length=250, blank=True, null=True)  # Field name made lowercase.
    m_hospausdat = models.CharField(db_column='M_HospAusDat', max_length=250, blank=True, null=True)  # Field name made lowercase.
    m_bfsaustritt = models.IntegerField(db_column='M_BFSAustritt', blank=True, null=True)  # Field name made lowercase.
    m_gewicht = models.SmallIntegerField(db_column='M_Gewicht', blank=True, null=True)  # Field name made lowercase.
    m_groesse = models.SmallIntegerField(db_column='M_Groesse', blank=True, null=True)  # Field name made lowercase.
    m_therapielimit = models.IntegerField(db_column='M_TherapieLimit', blank=True, null=True)  # Field name made lowercase.
    m_gradlimit = models.IntegerField(db_column='M_GradLimit', blank=True, null=True)  # Field name made lowercase.
    m_grundlimit = models.IntegerField(db_column='M_GrundLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dat_patfall'


class DatSchicht(models.Model):
    sid = models.BigIntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    fid = models.BigIntegerField(db_column='FID')  # Field name made lowercase.
    schichtnr = models.CharField(db_column='SchichtNr', max_length=2)  # Field name made lowercase.
    datum = models.CharField(db_column='Datum', max_length=14)  # Field name made lowercase.
    ne_monit = models.CharField(db_column='NE_Monit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_ivmedi = models.CharField(db_column='NE_IVMedi', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_beatm = models.CharField(db_column='NE_Beatm', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_vasoakt = models.CharField(db_column='NE_Vasoakt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_dialyse = models.CharField(db_column='NE_Dialyse', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_inticu = models.CharField(db_column='NE_IntICU', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_intauss = models.CharField(db_column='NE_IntAuss', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_sas = models.CharField(db_column='NE_SAS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_score = models.IntegerField(db_column='NE_Score', blank=True, null=True)  # Field name made lowercase.
    ne_kat = models.CharField(db_column='NE_Kat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_katman = models.CharField(db_column='NE_KatMan', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_beatmman = models.CharField(db_column='NE_BeatmMan', max_length=10, blank=True, null=True)  # Field name made lowercase.
    verlauf = models.CharField(db_column='Verlauf', max_length=250, blank=True, null=True)  # Field name made lowercase.
    betrperson = models.CharField(db_column='BetrPerson', max_length=45, blank=True, null=True)  # Field name made lowercase.
    del_field = models.CharField(db_column='Del', max_length=2)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mutdatum = models.CharField(db_column='MutDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    loct_01 = models.CharField(db_column='LOCT_01', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_02 = models.CharField(db_column='LOCT_02', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_03 = models.CharField(db_column='LOCT_03', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_04 = models.CharField(db_column='LOCT_04', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_05 = models.CharField(db_column='LOCT_05', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_06 = models.CharField(db_column='LOCT_06', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_07 = models.CharField(db_column='LOCT_07', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_08 = models.CharField(db_column='LOCT_08', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_09 = models.CharField(db_column='LOCT_09', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_10 = models.CharField(db_column='LOCT_10', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_11 = models.CharField(db_column='LOCT_11', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_12 = models.CharField(db_column='LOCT_12', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_13 = models.CharField(db_column='LOCT_13', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_14 = models.CharField(db_column='LOCT_14', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_15 = models.CharField(db_column='LOCT_15', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_16 = models.CharField(db_column='LOCT_16', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_17 = models.CharField(db_column='LOCT_17', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_18 = models.CharField(db_column='LOCT_18', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_19 = models.CharField(db_column='LOCT_19', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loct_20 = models.CharField(db_column='LOCT_20', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ne_rass = models.CharField(db_column='NE_RASS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_ecmo = models.CharField(db_column='P_ECMO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p_no = models.CharField(db_column='P_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tiss_artkath = models.CharField(db_column='TISS_ArtKath', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tiss_icp = models.CharField(db_column='TISS_ICP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tiss_acid_alkal = models.CharField(db_column='TISS_Acid_Alkal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tiss_pa_kath = models.CharField(db_column='TISS_PA_Kath', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tiss_volumen = models.CharField(db_column='TISS_Volumen', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sapsd_alter = models.CharField(db_column='SAPSD_Alter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_herzf = models.CharField(db_column='SAPSD_Herzf', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_bd = models.CharField(db_column='SAPSD_BD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_temp = models.CharField(db_column='SAPSD_Temp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_fio2 = models.CharField(db_column='SAPSD_FiO2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_po2 = models.CharField(db_column='SAPSD_PO2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_urin = models.CharField(db_column='SAPSD_Urin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_harn = models.CharField(db_column='SAPSD_Harn', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_leuk = models.CharField(db_column='SAPSD_Leuk', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_kali = models.CharField(db_column='SAPSD_Kali', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_natri = models.CharField(db_column='SAPSD_Natri', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_bikar = models.CharField(db_column='SAPSD_Bikar', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_bilir = models.CharField(db_column='SAPSD_Bilir', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_chron = models.CharField(db_column='SAPSD_Chron', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_aufn = models.CharField(db_column='SAPSD_Aufn', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sapsd_score = models.IntegerField(db_column='SAPSD_Score', blank=True, null=True)  # Field name made lowercase.
    m_sofa0 = models.IntegerField(db_column='M_SOFA0', blank=True, null=True)  # Field name made lowercase.
    m_sofa1 = models.IntegerField(db_column='M_SOFA1', blank=True, null=True)  # Field name made lowercase.
    m_sofa2 = models.IntegerField(db_column='M_SOFA2', blank=True, null=True)  # Field name made lowercase.
    m_sofa3 = models.IntegerField(db_column='M_SOFA3', blank=True, null=True)  # Field name made lowercase.
    m_sofa4 = models.IntegerField(db_column='M_SOFA4', blank=True, null=True)  # Field name made lowercase.
    m_sofa5 = models.IntegerField(db_column='M_SOFA5', blank=True, null=True)  # Field name made lowercase.
    m_sofa6 = models.IntegerField(db_column='M_SOFA6', blank=True, null=True)  # Field name made lowercase.
    m_sofa7 = models.IntegerField(db_column='M_SOFA7', blank=True, null=True)  # Field name made lowercase.
    ne_isol = models.CharField(db_column='NE_Isol', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dat_schicht'


class DatSchichtpersonal(models.Model):
    pid = models.BigIntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=10)  # Field name made lowercase.
    jmt = models.CharField(db_column='JMT', max_length=8)  # Field name made lowercase.
    wtk = models.CharField(db_column='WTk', max_length=2)  # Field name made lowercase.
    wt = models.CharField(db_column='WT', max_length=20)  # Field name made lowercase.
    a11 = models.CharField(db_column='A11', max_length=50)  # Field name made lowercase.
    a12 = models.CharField(db_column='A12', max_length=50)  # Field name made lowercase.
    a13 = models.CharField(db_column='A13', max_length=50)  # Field name made lowercase.
    b11 = models.CharField(db_column='B11', max_length=50)  # Field name made lowercase.
    b12 = models.CharField(db_column='B12', max_length=50)  # Field name made lowercase.
    b13 = models.CharField(db_column='B13', max_length=50)  # Field name made lowercase.
    b21 = models.CharField(db_column='B21', max_length=50)  # Field name made lowercase.
    b22 = models.CharField(db_column='B22', max_length=50)  # Field name made lowercase.
    b23 = models.CharField(db_column='B23', max_length=50)  # Field name made lowercase.
    b31 = models.CharField(db_column='B31', max_length=50)  # Field name made lowercase.
    b32 = models.CharField(db_column='B32', max_length=50)  # Field name made lowercase.
    b33 = models.CharField(db_column='B33', max_length=50)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=50)  # Field name made lowercase.
    c12 = models.CharField(db_column='C12', max_length=50)  # Field name made lowercase.
    c13 = models.CharField(db_column='C13', max_length=50)  # Field name made lowercase.
    c21 = models.CharField(db_column='C21', max_length=50)  # Field name made lowercase.
    c22 = models.CharField(db_column='C22', max_length=50)  # Field name made lowercase.
    c23 = models.CharField(db_column='C23', max_length=50)  # Field name made lowercase.
    c31 = models.CharField(db_column='C31', max_length=50)  # Field name made lowercase.
    c32 = models.CharField(db_column='C32', max_length=50)  # Field name made lowercase.
    c33 = models.CharField(db_column='C33', max_length=50)  # Field name made lowercase.
    d11 = models.CharField(db_column='D11', max_length=50)  # Field name made lowercase.
    d12 = models.CharField(db_column='D12', max_length=50)  # Field name made lowercase.
    d13 = models.CharField(db_column='D13', max_length=50)  # Field name made lowercase.
    d21 = models.CharField(db_column='D21', max_length=50)  # Field name made lowercase.
    d22 = models.CharField(db_column='D22', max_length=50)  # Field name made lowercase.
    d23 = models.CharField(db_column='D23', max_length=50)  # Field name made lowercase.
    d31 = models.CharField(db_column='D31', max_length=50)  # Field name made lowercase.
    d32 = models.CharField(db_column='D32', max_length=50)  # Field name made lowercase.
    d33 = models.CharField(db_column='D33', max_length=50)  # Field name made lowercase.
    e11 = models.CharField(db_column='E11', max_length=50)  # Field name made lowercase.
    e12 = models.CharField(db_column='E12', max_length=50)  # Field name made lowercase.
    e13 = models.CharField(db_column='E13', max_length=50)  # Field name made lowercase.
    e21 = models.CharField(db_column='E21', max_length=50)  # Field name made lowercase.
    e22 = models.CharField(db_column='E22', max_length=50)  # Field name made lowercase.
    e23 = models.CharField(db_column='E23', max_length=50)  # Field name made lowercase.
    e31 = models.CharField(db_column='E31', max_length=50)  # Field name made lowercase.
    e32 = models.CharField(db_column='E32', max_length=50)  # Field name made lowercase.
    e33 = models.CharField(db_column='E33', max_length=50)  # Field name made lowercase.
    f11 = models.CharField(db_column='F11', max_length=50)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=50)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=50)  # Field name made lowercase.
    g11 = models.CharField(db_column='G11', max_length=50)  # Field name made lowercase.
    g12 = models.CharField(db_column='G12', max_length=50)  # Field name made lowercase.
    g13 = models.CharField(db_column='G13', max_length=50)  # Field name made lowercase.
    g21 = models.CharField(db_column='G21', max_length=50)  # Field name made lowercase.
    g22 = models.CharField(db_column='G22', max_length=50)  # Field name made lowercase.
    g23 = models.CharField(db_column='G23', max_length=50)  # Field name made lowercase.
    g31 = models.CharField(db_column='G31', max_length=50)  # Field name made lowercase.
    g32 = models.CharField(db_column='G32', max_length=50)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=50)  # Field name made lowercase.
    h11 = models.CharField(db_column='H11', max_length=50)  # Field name made lowercase.
    h12 = models.CharField(db_column='H12', max_length=50)  # Field name made lowercase.
    h13 = models.CharField(db_column='H13', max_length=50)  # Field name made lowercase.
    w11 = models.CharField(db_column='W11', max_length=50)  # Field name made lowercase.
    w12 = models.CharField(db_column='W12', max_length=50)  # Field name made lowercase.
    w13 = models.CharField(db_column='W13', max_length=50)  # Field name made lowercase.
    w21 = models.CharField(db_column='W21', max_length=50)  # Field name made lowercase.
    w22 = models.CharField(db_column='W22', max_length=50)  # Field name made lowercase.
    w23 = models.CharField(db_column='W23', max_length=50)  # Field name made lowercase.
    w31 = models.CharField(db_column='W31', max_length=50)  # Field name made lowercase.
    w32 = models.CharField(db_column='W32', max_length=50)  # Field name made lowercase.
    w33 = models.CharField(db_column='W33', max_length=50)  # Field name made lowercase.
    w41 = models.CharField(db_column='W41', max_length=50)  # Field name made lowercase.
    w42 = models.CharField(db_column='W42', max_length=50)  # Field name made lowercase.
    w43 = models.CharField(db_column='W43', max_length=50)  # Field name made lowercase.
    as11 = models.CharField(db_column='AS11', max_length=50)  # Field name made lowercase.
    as12 = models.CharField(db_column='AS12', max_length=50)  # Field name made lowercase.
    as13 = models.CharField(db_column='AS13', max_length=50)  # Field name made lowercase.
    as21 = models.CharField(db_column='AS21', max_length=50)  # Field name made lowercase.
    as22 = models.CharField(db_column='AS22', max_length=50)  # Field name made lowercase.
    as23 = models.CharField(db_column='AS23', max_length=50)  # Field name made lowercase.
    as31 = models.CharField(db_column='AS31', max_length=50)  # Field name made lowercase.
    as32 = models.CharField(db_column='AS32', max_length=50)  # Field name made lowercase.
    as33 = models.CharField(db_column='AS33', max_length=50)  # Field name made lowercase.
    as41 = models.CharField(db_column='AS41', max_length=50)  # Field name made lowercase.
    as42 = models.CharField(db_column='AS42', max_length=50)  # Field name made lowercase.
    as43 = models.CharField(db_column='AS43', max_length=50)  # Field name made lowercase.
    as51 = models.CharField(db_column='AS51', max_length=50)  # Field name made lowercase.
    as52 = models.CharField(db_column='AS52', max_length=50)  # Field name made lowercase.
    as53 = models.CharField(db_column='AS53', max_length=50)  # Field name made lowercase.
    asb11 = models.CharField(db_column='ASB11', max_length=50)  # Field name made lowercase.
    asb12 = models.CharField(db_column='ASB12', max_length=50)  # Field name made lowercase.
    asb13 = models.CharField(db_column='ASB13', max_length=50)  # Field name made lowercase.
    asb21 = models.CharField(db_column='ASB21', max_length=50)  # Field name made lowercase.
    asb22 = models.CharField(db_column='ASB22', max_length=50)  # Field name made lowercase.
    asb23 = models.CharField(db_column='ASB23', max_length=50)  # Field name made lowercase.
    asb31 = models.CharField(db_column='ASB31', max_length=50)  # Field name made lowercase.
    asb32 = models.CharField(db_column='ASB32', max_length=50)  # Field name made lowercase.
    asb33 = models.CharField(db_column='ASB33', max_length=50)  # Field name made lowercase.
    asb41 = models.CharField(db_column='ASB41', max_length=50)  # Field name made lowercase.
    asb42 = models.CharField(db_column='ASB42', max_length=50)  # Field name made lowercase.
    asb43 = models.CharField(db_column='ASB43', max_length=50)  # Field name made lowercase.
    asb51 = models.CharField(db_column='ASB51', max_length=50)  # Field name made lowercase.
    asb52 = models.CharField(db_column='ASB52', max_length=50)  # Field name made lowercase.
    asb53 = models.CharField(db_column='ASB53', max_length=50)  # Field name made lowercase.
    aw1 = models.CharField(db_column='AW1', max_length=50)  # Field name made lowercase.
    aw2 = models.CharField(db_column='AW2', max_length=50)  # Field name made lowercase.
    aw3 = models.CharField(db_column='AW3', max_length=50)  # Field name made lowercase.
    aw4 = models.CharField(db_column='AW4', max_length=50)  # Field name made lowercase.
    aw5 = models.CharField(db_column='AW5', max_length=50)  # Field name made lowercase.
    beko1 = models.CharField(db_column='BEKO1', max_length=50)  # Field name made lowercase.
    beko2 = models.CharField(db_column='BEKO2', max_length=50)  # Field name made lowercase.
    beko3 = models.CharField(db_column='BEKO3', max_length=50)  # Field name made lowercase.
    oa1 = models.CharField(db_column='OA1', max_length=50)  # Field name made lowercase.
    oa2 = models.CharField(db_column='OA2', max_length=50)  # Field name made lowercase.
    oa3 = models.CharField(db_column='OA3', max_length=50)  # Field name made lowercase.
    da1 = models.CharField(db_column='DA1', max_length=50)  # Field name made lowercase.
    da11 = models.CharField(db_column='DA11', max_length=50)  # Field name made lowercase.
    da12 = models.CharField(db_column='DA12', max_length=50)  # Field name made lowercase.
    da13 = models.CharField(db_column='DA13', max_length=50)  # Field name made lowercase.
    da2 = models.CharField(db_column='DA2', max_length=50)  # Field name made lowercase.
    da21 = models.CharField(db_column='DA21', max_length=50)  # Field name made lowercase.
    da22 = models.CharField(db_column='DA22', max_length=50)  # Field name made lowercase.
    da23 = models.CharField(db_column='DA23', max_length=50)  # Field name made lowercase.
    info = models.TextField(db_column='INFO')  # Field name made lowercase.
    drg = models.CharField(db_column='DRG', max_length=50)  # Field name made lowercase.
    beatm = models.CharField(db_column='BEATM', max_length=50)  # Field name made lowercase.
    number_1b1 = models.CharField(db_column='1B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1b2 = models.CharField(db_column='1B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1b3 = models.CharField(db_column='1B3', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1b4 = models.CharField(db_column='1B4', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2b1 = models.CharField(db_column='2B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2b2 = models.CharField(db_column='2B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b1 = models.CharField(db_column='3B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b2 = models.CharField(db_column='3B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b3 = models.CharField(db_column='3B3', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b4 = models.CharField(db_column='3B4', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4b1 = models.CharField(db_column='4B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5b1 = models.CharField(db_column='5B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6b1 = models.CharField(db_column='6B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6b2 = models.CharField(db_column='6B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7b1 = models.CharField(db_column='7B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7b2 = models.CharField(db_column='7B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_8b1 = models.CharField(db_column='8B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_8b2 = models.CharField(db_column='8B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_9b1 = models.CharField(db_column='9B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_9b2 = models.CharField(db_column='9B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_10b1 = models.CharField(db_column='10B1', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_10b2 = models.CharField(db_column='10B2', max_length=45)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    oa21 = models.CharField(db_column='OA21', max_length=45)  # Field name made lowercase.
    oa22 = models.CharField(db_column='OA22', max_length=45)  # Field name made lowercase.
    oa23 = models.CharField(db_column='OA23', max_length=45)  # Field name made lowercase.
    da31 = models.CharField(db_column='DA31', max_length=45)  # Field name made lowercase.
    da32 = models.CharField(db_column='DA32', max_length=45)  # Field name made lowercase.
    da33 = models.CharField(db_column='DA33', max_length=45)  # Field name made lowercase.
    ss1 = models.CharField(db_column='SS1', max_length=45)  # Field name made lowercase.
    ss2 = models.CharField(db_column='SS2', max_length=45)  # Field name made lowercase.
    ss3 = models.CharField(db_column='SS3', max_length=45)  # Field name made lowercase.
    ss0 = models.CharField(db_column='SS0', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dat_schichtpersonal'


class DatStruktur(models.Model):
    sid = models.BigIntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    ipscode = models.CharField(db_column='IPSCode', max_length=25)  # Field name made lowercase.
    rechjahr = models.CharField(db_column='RechJahr', max_length=4)  # Field name made lowercase.
    vondatum = models.CharField(db_column='VonDatum', max_length=14)  # Field name made lowercase.
    bisdatum = models.CharField(db_column='BisDatum', max_length=14)  # Field name made lowercase.
    alanzplanbett = models.FloatField(db_column='ALAnzPlanBett', blank=True, null=True)  # Field name made lowercase.
    alanzbetriebbett = models.FloatField(db_column='ALAnzBetriebBett', blank=True, null=True)  # Field name made lowercase.
    alartderips = models.CharField(db_column='ALArtderIPS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alpflausweis = models.FloatField(db_column='ALPflAusweis', blank=True, null=True)  # Field name made lowercase.
    alpflsfa = models.FloatField(db_column='ALPflSFA', blank=True, null=True)  # Field name made lowercase.
    alpflkader = models.FloatField(db_column='ALPflKader', blank=True, null=True)  # Field name made lowercase.
    alpfllehr = models.FloatField(db_column='ALPflLehr', blank=True, null=True)  # Field name made lowercase.
    alpflinwb = models.FloatField(db_column='ALPflInWB', blank=True, null=True)  # Field name made lowercase.
    alpflsonst = models.FloatField(db_column='ALPflSonst', blank=True, null=True)  # Field name made lowercase.
    alpflhilfspers = models.FloatField(db_column='ALPflHilfspers', blank=True, null=True)  # Field name made lowercase.
    alarztfmhi = models.FloatField(db_column='ALArztFMHi', blank=True, null=True)  # Field name made lowercase.
    alarztkader = models.FloatField(db_column='ALArztKader', blank=True, null=True)  # Field name made lowercase.
    alarztinwb = models.FloatField(db_column='ALArztInWB', blank=True, null=True)  # Field name made lowercase.
    alarztsonst = models.FloatField(db_column='ALArztSonst', blank=True, null=True)  # Field name made lowercase.
    alperadmin = models.FloatField(db_column='ALPerAdmin', blank=True, null=True)  # Field name made lowercase.
    alpersonst = models.FloatField(db_column='ALPerSonst', blank=True, null=True)  # Field name made lowercase.
    alzertjahrkai = models.CharField(db_column='ALZertJahrKAI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    alzertwbarimy = models.IntegerField(db_column='ALZertWBArImY', blank=True, null=True)  # Field name made lowercase.
    alzertkat = models.CharField(db_column='ALZertKat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alzertwbpfimy = models.IntegerField(db_column='ALZertWBPfImY', blank=True, null=True)  # Field name made lowercase.
    dvpflanrede = models.CharField(db_column='DVPflAnrede', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflname = models.CharField(db_column='DVPflName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflvorname = models.CharField(db_column='DVPflVorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflips = models.CharField(db_column='DVPflIPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflspital = models.CharField(db_column='DVPflSpital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpfladresse = models.CharField(db_column='DVPflAdresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflort = models.CharField(db_column='DVPflOrt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflplz = models.CharField(db_column='DVPflPLZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflemail = models.CharField(db_column='DVPflEMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpfltelefon = models.CharField(db_column='DVPflTelefon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvpflfax = models.CharField(db_column='DVPflFax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztanrede = models.CharField(db_column='DVArztAnrede', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztname = models.CharField(db_column='DVArztName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztvorname = models.CharField(db_column='DVArztVorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztips = models.CharField(db_column='DVArztIPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztspital = models.CharField(db_column='DVArztSpital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztadresse = models.CharField(db_column='DVArztAdresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztort = models.CharField(db_column='DVArztOrt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztplz = models.CharField(db_column='DVArztPLZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztemail = models.CharField(db_column='DVArztEMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarzttelefon = models.CharField(db_column='DVArztTelefon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dvarztfax = models.CharField(db_column='DVArztFax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflanrede = models.CharField(db_column='WVPflAnrede', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflname = models.CharField(db_column='WVPflName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflvorname = models.CharField(db_column='WVPflVorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflips = models.CharField(db_column='WVPflIPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflspital = models.CharField(db_column='WVPflSpital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpfladresse = models.CharField(db_column='WVPflAdresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflort = models.CharField(db_column='WVPflOrt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflplz = models.CharField(db_column='WVPflPLZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflemail = models.CharField(db_column='WVPflEMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpfltelefon = models.CharField(db_column='WVPflTelefon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvpflfax = models.CharField(db_column='WVPflFax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztanrede = models.CharField(db_column='WVArztAnrede', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztname = models.CharField(db_column='WVArztName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztvorname = models.CharField(db_column='WVArztVorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztips = models.CharField(db_column='WVArztIPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztspital = models.CharField(db_column='WVArztSpital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztadresse = models.CharField(db_column='WVArztAdresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztort = models.CharField(db_column='WVArztOrt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztplz = models.CharField(db_column='WVArztPLZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztemail = models.CharField(db_column='WVArztEMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarzttelefon = models.CharField(db_column='WVArztTelefon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    wvarztfax = models.CharField(db_column='WVArztFax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    del_field = models.CharField(db_column='Del', max_length=2)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mutdatum = models.CharField(db_column='MutDatum', max_length=14, blank=True, null=True)  # Field name made lowercase.
    alzertjahrkwfb = models.CharField(db_column='ALZertJahrKWFB', max_length=14, blank=True, null=True)  # Field name made lowercase.
    alzertjahrsbk = models.CharField(db_column='ALZertJahrSBK', max_length=14, blank=True, null=True)  # Field name made lowercase.
    lpflanrede = models.CharField(db_column='LPflAnrede', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflname = models.CharField(db_column='LPflName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflvorname = models.CharField(db_column='LPflVorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflips = models.CharField(db_column='LPflIPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflspital = models.CharField(db_column='LPflSpital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpfladresse = models.CharField(db_column='LPflAdresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflort = models.CharField(db_column='LPflOrt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflplz = models.CharField(db_column='LPflPLZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflemail = models.CharField(db_column='LPflEMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpfltelefon = models.CharField(db_column='LPflTelefon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lpflfax = models.CharField(db_column='LPflFax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztanrede = models.CharField(db_column='LArztAnrede', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztname = models.CharField(db_column='LArztName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztvorname = models.CharField(db_column='LArztVorname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztips = models.CharField(db_column='LArztIPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztspital = models.CharField(db_column='LArztSpital', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztadresse = models.CharField(db_column='LArztAdresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztort = models.CharField(db_column='LArztOrt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztplz = models.CharField(db_column='LArztPLZ', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztemail = models.CharField(db_column='LArztEMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larzttelefon = models.CharField(db_column='LArztTelefon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    larztfax = models.CharField(db_column='LArztFax', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dat_struktur'


class IniCodeparam(models.Model):
    recid = models.BigIntegerField(db_column='RECID', primary_key=True)  # Field name made lowercase.
    site = models.CharField(db_column='SITE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mussfeld = models.IntegerField(db_column='MUSSFELD', blank=True, null=True)  # Field name made lowercase.
    inputtyp = models.CharField(db_column='INPUTTYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    iscode = models.CharField(db_column='ISCODE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    idname = models.CharField(db_column='IDNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headtxt1 = models.CharField(db_column='HEADTXT1', max_length=130, blank=True, null=True)  # Field name made lowercase.
    headtxt2 = models.CharField(db_column='HEADTXT2', max_length=130, blank=True, null=True)  # Field name made lowercase.
    headtxt3 = models.CharField(db_column='HEADTXT3', max_length=130, blank=True, null=True)  # Field name made lowercase.
    headtxt4 = models.CharField(db_column='HEADTXT4', max_length=130, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='TEXT2', max_length=150, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='TEXT3', max_length=150, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='TEXT4', max_length=150, blank=True, null=True)  # Field name made lowercase.
    info1 = models.CharField(db_column='INFO1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    info2 = models.CharField(db_column='INFO2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    info3 = models.CharField(db_column='INFO3', max_length=250, blank=True, null=True)  # Field name made lowercase.
    info4 = models.CharField(db_column='INFO4', max_length=250, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    valon = models.CharField(db_column='VALON', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maxsize = models.IntegerField(db_column='MAXSIZE', blank=True, null=True)  # Field name made lowercase.
    size_r = models.IntegerField(db_column='SIZE_R', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SORTORDER', blank=True, null=True)  # Field name made lowercase.
    forcenewrow = models.IntegerField(db_column='FORCENEWROW', blank=True, null=True)  # Field name made lowercase.
    twocell = models.IntegerField(db_column='TWOCELL', blank=True, null=True)  # Field name made lowercase.
    samecell = models.IntegerField(db_column='SAMECELL', blank=True, null=True)  # Field name made lowercase.
    spezform = models.CharField(db_column='SPEZFORM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    regrecid = models.CharField(db_column='REGRECID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codeinfo = models.CharField(db_column='CodeInfo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    aktiv = models.CharField(db_column='Aktiv', max_length=2)  # Field name made lowercase.
    vorbelegt = models.CharField(db_column='VORBELEGT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tabsort = models.CharField(db_column='TABSORT', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ini_codeparam'


class IniLangbox(models.Model):
    recid = models.BigIntegerField(db_column='RECID', primary_key=True)  # Field name made lowercase.
    site = models.CharField(db_column='SITE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idname = models.CharField(db_column='IDNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    txt1 = models.TextField(db_column='TXT1', blank=True, null=True)  # Field name made lowercase.
    txt2 = models.TextField(db_column='TXT2', blank=True, null=True)  # Field name made lowercase.
    txt3 = models.TextField(db_column='TXT3', blank=True, null=True)  # Field name made lowercase.
    txt4 = models.TextField(db_column='TXT4', blank=True, null=True)  # Field name made lowercase.
    typ = models.CharField(db_column='TYP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sortorder = models.CharField(db_column='SORTORDER', max_length=6, blank=True, null=True)  # Field name made lowercase.
    optionvalue = models.CharField(db_column='OPTIONVALUE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ini_langbox'


class IsopPatfall(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nachname = models.CharField(db_column='NACHNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vorname = models.CharField(db_column='VORNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    geschlecht = models.CharField(db_column='GESCHLECHT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    geburtsdatum = models.CharField(db_column='GEBURTSDATUM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    patnr = models.CharField(db_column='PATNR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eintrittsdatum = models.CharField(db_column='EINTRITTSDATUM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    zimmer = models.CharField(db_column='ZIMMER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    klasse = models.CharField(db_column='KLASSE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kategorie = models.CharField(db_column='KATEGORIE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='TELEFON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fallnr = models.CharField(db_column='FALLNR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    strasse = models.CharField(db_column='STRASSE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plz = models.CharField(db_column='PLZ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ort = models.CharField(db_column='ORT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    austrittsdatum = models.CharField(db_column='AUSTRITTSDATUM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    land = models.CharField(db_column='LAND', max_length=50, blank=True, null=True)  # Field name made lowercase.
    geburtname = models.CharField(db_column='GEBURTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    austrittszeit = models.CharField(db_column='AUSTRITTSZEIT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disziplin = models.CharField(db_column='DISZIPLIN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    eintrittszeit = models.CharField(db_column='EINTRITTSZEIT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    garant1 = models.CharField(db_column='GARANT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    konfession = models.CharField(db_column='KONFESSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    versichnr = models.CharField(db_column='VERSICHNR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zimmertel = models.CharField(db_column='ZIMMERTEL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sprache = models.CharField(db_column='SPRACHE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    zivilstand = models.CharField(db_column='ZIVILSTAND', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kontaktadr = models.CharField(db_column='KONTAKTADR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ahvnr = models.CharField(db_column='AHVNR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mutts = models.CharField(db_column='MUTTS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insts = models.CharField(db_column='INSTS', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'isop_patfall'


class LogError(models.Model):
    rid = models.BigIntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=21, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TIMESTAMP', max_length=14, blank=True, null=True)  # Field name made lowercase.
    errnum = models.CharField(db_column='ERRNUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errstring = models.TextField(db_column='ERRSTRING', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=160, blank=True, null=True)  # Field name made lowercase.
    zeile = models.CharField(db_column='ZEILE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='INFO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_error'


class LogHistory(models.Model):
    rid = models.BigIntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=21, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TIMESTAMP', max_length=14, blank=True, null=True)  # Field name made lowercase.
    tabname = models.CharField(db_column='TABNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oprecid = models.CharField(db_column='OPRECID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recstring = models.TextField(db_column='RECSTRING', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logintxt = models.CharField(db_column='LOGINTXT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LOGINID', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_history'


class LogInfo(models.Model):
    rid = models.BigIntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=21, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TIMESTAMP', max_length=14, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    param = models.TextField(db_column='PARAM', blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='INFO', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_info'


class LogIsgate(models.Model):
    rid = models.BigIntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    gruppe = models.CharField(db_column='GRUPPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TIMESTAMP', max_length=14, blank=True, null=True)  # Field name made lowercase.
    typ = models.CharField(db_column='TYP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    quelle = models.CharField(db_column='QUELLE', max_length=160, blank=True, null=True)  # Field name made lowercase.
    ref1 = models.CharField(db_column='REF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ref2 = models.CharField(db_column='REF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='INFO', blank=True, null=True)  # Field name made lowercase.
    ref3 = models.CharField(db_column='REF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_isgate'
