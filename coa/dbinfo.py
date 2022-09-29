# -*- coding: utf-8 -*-
"""Project : PyCoA - Copyright ©pycoa.fr
Date :    april 2020 - march 2022
Authors : Olivier Dadoun, Julien Browaeys, Tristan Beau
License: See joint LICENSE file
Module : report
About
-----
This is the PyCoA rapport module it gives all available information concerning a database key words
"""
from coa.error import *

def generic_info(namedb, keys):
    '''
    Return information on the available keyswords for the database selected
    '''
    mydico = {}
    if namedb == 'spf':
        urlmaster3='https://www.data.gouv.fr/fr/datasets/donnees-de-laboratoires-pour-le-depistage-a-compter-du-18-05-2022-si-dep/'
        urlmaster5='https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1'
        urlmaster4='https://www.data.gouv.fr/fr/datasets/indicateurs-de-suivi-de-lepidemie-de-covid-19/'
        urlmaster6='https://www.data.gouv.fr/fr/datasets/donnees-de-laboratoires-pour-le-depistage-indicateurs-sur-les-variants/'
        urlmaster7='https://www.data.gouv.fr/fr/datasets/donnees-de-laboratoires-pour-le-depistage-focus-par-niveau-scolaire/'
        urlmaster8='https://www.data.gouv.fr/fr/datasets/donnees-de-laboratoires-pour-le-depistage-indicateurs-sur-les-mutations/'
        urlmaster9='https://www.data.gouv.fr/en/datasets/donnees-des-urgences-hospitalieres-et-de-sos-medecins-relatives-a-lepidemie-de-covid-19/'
        url3='https://www.data.gouv.fr/fr/datasets/r/ca490480-09a3-470f-8556-76d6fd291325'
        url4='https://www.data.gouv.fr/fr/datasets/r/4acad602-d8b1-4516-bc71-7d5574d5f33e'
        url5='https://www.data.gouv.fr/fr/datasets/r/32a16487-3dd3-4326-9d2b-317e5a3b2daf'
        url6='https://www.data.gouv.fr/fr/datasets/r/16f4fd03-797f-4616-bca9-78ff212d06e8'
        url8='https://www.data.gouv.fr/fr/datasets/r/bc318bc7-fb90-4e76-a6cb-5cdc0a4e5432'
        url9='https://www.data.gouv.fr/en/datasets/r/eceb9fb4-3ebc-4da3-828d-f5939712600a'
        spfdic = {
        'tot_dchosp':
        ['tot_dc:FILLIT',url3,urlmaster3],
        'cur_hosp':
        ['cur_hosp:FILLIT',url3,urlmaster3],
        'tot_rad':
        ['tot_rad:FILLIT',url3,urlmaster3],
        'cur_rea':
        ['cur_rea:FILLIT',url3,urlmaster3],
        'cur_idx_tx_incid':
        ['cur_idx_tx_incid: Taux d\'incidence (activité épidémique : Le taux d\'incidence correspond au nombre de personnes testées\
        positives (RT-PCR et test antigénique) pour la première fois depuis plus de 60 jours rapporté à la taille de la population. \
        Il est exprimé pour 100 000 habitants)',url3,urlmaster3],
        'cur_idx_R':
        ['cur_idx_R:FILLIT',url4,urlmaster4],
        'cur_tx_crib':
        ['cur_tx_crib:FILLIT',url4,urlmaster3],
        'cur_idx_tx_occupation_sae':
        ['cur_idx_tx_occupation_sae:FILLIT',url4,urlmaster4],
        'cur_tx_pos':
        ['cur_tx_pos: Taux de positivité des tests virologiques (Le taux de positivité correspond au nombre de personnes testées positives\
         (RT-PCR et test antigénique) pour la première fois depuis plus de 60 jours rapporté au nombre total de personnes testées positives ou \
         négatives sur une période donnée ; et qui n‘ont jamais été testées positive dans les 60 jours précédents.)',url4,urlmaster3],
        'tot_vacc1':
        ['tot_vacc1:(nom initial  n_cum_dose1)',url5,urlmaster5],
        'tot_vacc_complet':
        ['tot_vacc_complet:(nom initial n_cum_complet)',url5,urlmaster5],
        'tot_vacc_rappel':
        ['tot_vacc_rappel: (nom initial  n_cum_rappel)',url5,urlmaster5],
        'tot_vacc2_rappel':
        ['tot_vacc2_rappel:(nom initial  n_cum_2_rappel)',url5,urlmaster5],
        'tot_incid_hosp':
        ['tot_incid_hosp: Nombre total de personnes hospitalisées',url3,urlmaster3],
        'tot_incid_rea':
        ['tot_incid_rea: Nombre total d\'admissions en réanimation',url3,urlmaster3],
        'tot_incid_rad':
        ['tot_incid_rad: Nombre total de  retours à domicile',url3,urlmaster3],
        'tot_incid_dchosp':
        ['tot_incid_dchosp: Nombre total de personnes  décédées',url3,urlmaster3],
        'tot_P':
        ['tot_P: Nombre total de tests positifs',url3,urlmaster3],
        'tot_T':
        ['tot_T: Nombre total de tests réalisés',url3,urlmaster3],
        'cur_idx_Prc_tests_PCR_TA_crible' :
        ['cur_idx_Prc_tests_PCR_TA_crible: % de tests PCR criblés parmi les PCR positives.',url6,urlmaster6],
        'cur_idx_Prc_susp_501Y_V1' :
        ['Prc_susp_501Y_V1: % de tests avec suspicion de variant 20I/501Y.V1 (UK).\n Royaume-Uni (UK): code Nexstrain= 20I/501Y.V1.',url6,urlmaster6],
        'cur_idx_Prc_susp_501Y_V2_3' :
        ['Prc_susp_501Y_V2_3: % de tests avec suspicion de variant 20H/501Y.V2 (ZA) ou 20J/501Y.V3 (BR).Afrique du Sud (ZA) : \
        code Nexstrain= 20H/501Y.V2. Brésil (BR) : code Nexstrain= 20J/501Y.V3',url6,urlmaster6],
        'cur_idx_Prc_susp_IND' :
        ['Prc_susp_IND: % de tests avec une détection de variant mais non identifiable',url6,urlmaster6],
        'cur_idx_Prc_susp_ABS' :
        ['Prc_susp_ABS: % de tests avec une absence de détection de variant',url6,urlmaster6],
        #'cur_idx_ti':
        #['ti : taux d\'incidence hebdomadaire rapporté à la population pour 100 000 habitants , par semaine calendaire (en milieu scolaire)',url7,urlmaster7],
        #'cur_idx_tp':
        #['tp :Le taux de positivité hebdomadaire rapporté 100 tests réalisés, par semaine calendaire (en milieu scolaire)',url7,urlmaster7],
        #'nb_crib' : ['Nombre de tests criblés',url8,urlmaster8],
        #'nb_pos' : ['Nombre de tests positifs',url8,urlmaster8],
        #'tx_crib' : ['Taux tests criblés',url8,urlmaster8],
        #'cur_idx_tx_A1':['FILL IT',url8,urlmaster8],
        #'cur_idx_tx_B1':['FILL IT',url8,urlmaster8],
        #'cur_idx_tx_C1':['FILL IT',url8,urlmaster8],
        'cur_nb_A0' :
        ['cur_nb_A0:Nombre des tests positifs pour lesquels la recherche de mutation A est négatif (A = E484K)',url8,urlmaster8],
        'cur_nb_A1' :
        ['cur_nb_A1:Nombre des tests positifs pour lesquels la recherche de mutation A est positif (A = E484K)',url8,urlmaster8],
        'cur_tx_A1' :
        ['cur_tx_A1:Taux de présence mutation A (A = E484K)',url8,urlmaster8],
        'cur_nb_C0' :
        ['cur_nb_C0:Nombre des tests positifs pour lesquels la recherche de mutation C est négatif (C = L452R)',url8,urlmaster8],
        'cur_nb_C1' :
        ['cur_nb_C1:Nombre des tests positifs pour lesquels la recherche de mutation C est positif (C = L452R)',url8,urlmaster8],
        'cur_tx_C1' :
        ['cur_tx_C1:Taux de présence mutation C (C = L452R)',url8,urlmaster8],
        'cur_nbre_pass_corona' :
        ['Nombre de passages aux urgences pour suspicion de COVID-19 (nbre_pass_corona)',url9,urlmaster9],
        }
        mydico = spfdic
    elif namedb == 'spfnational':
        spfn = {
        'cur_reanimation':['(nom d\'origine incid_rea) Nombre de nouveaux patients admis en réanimation au cours des dernières 24h.'],\
        'cur_hospitalises':['(nom d\'origine incid_hosp) Nombre de nouveaux patients hospitalisés au cours des dernières 24h.'],\
        'cur_cas':['(nom d\'origine,conf_j1) Nombre de nouveaux cas confirmés (J-1 date de résultats)'],
        'tot_dc_hosp':['(nom d\'origine dchosp) :Cumul des décès (cumul des décès constatés à l\'hôpital et en EMS)'],\
        'tot_dc_esms':['(nom d\'origine esms_dc)tot_dc_esms: Décès en ESMS'],
        'tot_dc':['(nom d\'origine dc_tot): tot dc'],
        'cur_tx_pos': ['(nom d\'origine tx_pos): Taux de positivité des tests virologiques'],
        }
        for k,v in spfn.items():
              spfn[k].append('https://www.data.gouv.fr/fr/datasets/r/f335f9ea-86e3-4ffa-9684-93c009d5e617')
              spfn[k].append('https://www.data.gouv.fr/fr/datasets/synthese-des-indicateurs-de-suivi-de-lepidemie-covid-19/')
        mydico = spfn
    elif namedb == 'insee':
        insee = {
        'tot_deaths_since_2018-01-01':['tot deaths number_of_deaths integrated since 2018-01-01 '],\
        }
        for k,v in insee.items():
            insee[k].append('https://www.data.gouv.fr/fr/datasets/fichier-des-personnes-decedees/')
            insee[k].append('https://www.data.gouv.fr/fr/datasets/fichier-des-personnes-decedees/')
        mydico = insee
    elif namedb == 'opencovid19':
        op19 = {
        'tot_deces':['tot_deces: total cumulé du nombre de décès au niveau national'],
        'tot_cas_confirmes':['tot_cas_confirmes: total cumulé du nombre de cas confirmes au niveau national'],
        'cur_reanimation':['cur_reanimation:  nombre de personnes en réanimation'],
        'cur_hospitalises':['cur_hospitalises: nombre de personnes en hospitalisation'],
        'tot_gueris':['tot_gueris: total cumulé du nombre de gueris au niveau national'],
        'tot_nouvelles_hospitalisations':['tot_nouvelles_hospitalisations: total cumulé du nombre d\'hospitalisation au niveau national'],
        'tot_nouvelles_reanimations':['tot_nouvelles_reanimations: tot_nouvelles_reanimations: total cumulé du nombre réanimations au niveau national'],
        'tot_depistes':['tot_depistes: total cumulé du nombre de personnes dépistées (testées par PCR) au niveau national'],
        }
        for k,v in op19.items():
            op19[k].append('https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.csv')
            op19[k].append('https://github.com/opencovid19-fr/data')
        mydico = op19
    elif namedb == 'opencovid19national':
        op19nat = {
         'tot_deces':['tot_deces: total cumulé du nombre de décès'],
         'tot_cas_confirmes':['tot_cas_confirmes: total cumulé du nombre de cas confirmés'],
         'tot_cas_ehpad':['tot_cas_ehpad: total cumulé du nombre de cas en EHPAD'],
         'tot_cas_confirmes_ehpad':['total cumulé du nombre de cas positifs en EHPAD'],
         'tot_cas_possibles_ehpad':['tot_cas_possibles_ehpad:FILLIT'],
         'tot_deces_ehpad':['total cumulé du nombre de décès en EHPAD'],
         'cur_reanimation':['cur_hospitalises: nombre de personnes en reanimation'],
         'cur_hospitalises':['cur_hospitalises: nombre de personnes en hospitalisation'],
         'tot_gueris':['total cumulé du nombre de gueris'],
         'tot_nouvelles_hospitalisations':['tot_nouvelles_hospitalisations: total cumulé du nombre d\'hospitalisation'],
         'tot_nouvelles_reanimations':['tot_nouvelles_reanimations: tot_nouvelles_reanimations: total cumulé du nombre réanimations'],
         'tot_depistes':['tot_depistes: total cumulé du nombre de personnes dépistées (testées par PCR)']
          }
        for k,v in op19nat.items():
              op19nat[k].append('https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.csv')
              op19nat[k].append('https://github.com/opencovid19-fr/data')
        mydico = op19nat
    elif namedb == 'obepine':
        obe = {
         'idx_obepine':['tot_deces: total cumulé du nombre de décès']}
        for k,v in obe.items():
              obe[k].append('https://www.data.gouv.fr/fr/datasets/r/25fb690a-af7f-4e69-bf40-7ca7698e2748')
              obe[k].append('https://www.data.gouv.fr/en/datasets/surveillance-du-sars-cov-2-dans-les-eaux-usees-1')
        mydico = obe
    elif namedb == 'owid':
        owid={
        'total_deaths':['total_deaths: Total deaths attributed to COVID-19'],
        'total_cases':['total_cases: Total confirmed cases of COVID-19'],
        'total_tests':['total_tests: Total tests for COVID-19'],
        'total_tests_per_thousand':['tal_tests_per_thousand: Total tests for COVID-19 per thousand'],
        'cur_new_tests':['cur_new_tests (original name new_tests): New tests for COVID-19 (only calculated for consecutive days)'],
        'total_vaccinations':['total_vaccinations: Total number of COVID-19 vaccination doses administered'],
        'total_population':['total_population: total population of a given country'],
        'total_people_fully_vaccinated_per_hundred':['total_people_fully_vaccinated_per_hundred (original name people_fully_vaccinated_per_hundred): Total number of people who received all doses prescribed by the vaccination protocol per 100 people in the total population'],
        'total_boosters':['total_boosters: Total number of COVID-19 vaccination booster doses administered (doses administered beyond the number prescribed by the vaccination protocol)'],
        'total_people_vaccinated':['total_people_vaccinated (original name people_vaccinated): Total number of people who received at least one vaccine dose'],
        'total_people_fully_vaccinated':['total_people_fully_vaccinated (original name people_fully_vaccinated): Total number of people who received all doses prescribed by the vaccination protocol'],
        'total_people_vaccinated_per_hundred':['total_people_vaccinated_per_hundred (original name people_vaccinated_per_hundred): total_people_vaccinated_per_hundred:Total number of people who received all doses prescribed by the vaccination protocol per 100 people in the total population'],
        'total_cases_per_million':['total_cases_per_million: Total confirmed cases of COVID-19 per 1,000,000 people'],
        'total_deaths_per_million':['total_deaths_per_million: Total deaths attributed to COVID-19 per 1,000,000 people'],
        'total_vaccinations_per_hundred':['total_vaccinations_per_hundred: COVID19 vaccine doses administered per 100 people'],
        'cur_reproduction_rate':['cur_reproduction_rate (original name reproduction_rate): Real-time estimate of the effective reproduction rate (R) of COVID-19. See https://github.com/crondonm/TrackingR/tree/main/Estimates-Database'],
        'cur_icu_patients':['cur_icu_patients (orignal name icu_patients): Number of COVID-19 patients in intensive care units (ICUs) on a given day'],
        'cur_hosp_patients':['cur_hosp_patients (original name hosp_patients): Number of COVID-19 patients in hospital on a given day'],
        'cur_weekly_hosp_admissions':['cur_weekly_hosp_admissions (original name weekly_hosp_admissions): Number of COVID-19 patients in hospital on a given week'],
        'cur_idx_positive_rate':['cur_idx_positive_rate (original name positive_rate): The share of COVID-19 tests that are positive, given as a rolling 7-day average (this is the inverse of tests_per_case)'],
        'total_gdp_per_capita':['Gross domestic product at purchasing power parity (constant 2011 international dollars), most recent year available'],
        'cur_excess_mortality':['cur_excess_mortality: original name excess_mortality. Percentage difference between the reported number of weekly or monthly deaths in 2020–2021 and the projected number of deaths for the same period based on previous years'],
        'cur_excess_mortality_cumulative_per_million':['cur_excess_mortality_cumulative_per_million:original name excess_mortality_cumulative_per_million.Cumulative difference between the reported number of deaths since 1 January 2020 and the projected number of deaths for the same period based on previous years, per million people. '],
        }
        for k,v in owid.items():
            owid[k].append("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
            owid[k].append("https://github.com/owid")
        mydico = owid
    elif namedb == 'jhu':
        jhu = {
        'tot_deaths':['tot_deaths (original name deaths): counts include confirmed and probable (where reported).',\
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'],
        'tot_confirmed':['tot_confirmed (original name confirmed): counts include confirmed and probable (where reported).',\
        'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'],
        'tot_recovered':['tot_recovered (original name recovered): cases are estimates based on local media reports, and state and local reporting when available, and therefore may be substantially lower than the true number. US state-level recovered cases are from COVID Tracking Project (https://covidtracking.com/)',\
        'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv']
         }
        for k,v in jhu.items():
             jhu[k].append("https://github.com/CSSEGISandData/COVID-19")
        mydico = jhu
    elif namedb == 'jhu-usa':
        jhuusa = {
        'tot_deaths':['tot_deaths (original name deaths): counts include confirmed and probable (where reported).',\
        'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'],
        'tot_confirmed':['tot_confirmed (original name confirmed): counts include confirmed and probable (where reported).',\
        'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv']
        }
        for k,v in jhuusa.items():
            jhuusa[k].append("https://github.com/CSSEGISandData/COVID-19")
        mydico = jhuusa
    elif namedb == 'moh':
        moh = {
        'tot_cases':['tot_cases: total cases (from original data cases_new )'],\
        'hosp_covid':['hosp_covid: hosp_covid'],\
        'daily_partial':['daily_partial: daily_partial'],\
        'daily_full':['daily_full: daily_full'],\
        'icu_covid':['icu_covid: icu_covid'],\
        'beds_icu_covid':['beds_icu_covid: beds_icu_covid'],\
        'tot_deaths':['tot_deaths'],\
        }
        for k,v in moh.items():
            moh[k].append("https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_state.csv")
            moh[k].append("https://github.com/MoH-Malaysia/covid19-public")
        mydico = moh
    elif namedb == 'minciencia':
        mi = {
        'cases':['cases: Casos confirmados'],\
        }
        for k,v in mi.items():
            mi[k].append("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19_std.csv")
            mi[k].append("https://github.com/MinCiencia")
        mydico = mi
    elif namedb == 'covid19india':
        india = {
        'tot_Deceased':['tot_Deceased (original name: Deceased): Total number of Deceased'],\
        'tot_Confirmed':['tot_Confirmed (original name: Confirmed): Total number of Confirmed'],\
        'tot_Recovered':['tot_Recovered ( original name:  Recovered): Total number of Recovered'],\
        'tot_Tested':['tot_Tested ( original name:  Tested): Total number of Tested']
        }
        for k,v in india.items():
            india[k].append('https://api.covid19india.org/csv/latest/states.csv')
            india[k].append('https://www.covid19india.org/')
        mydico = india
    elif namedb == 'dpc':
        ita = {
        'tot_cases':['tot_cases:original name totale_casi + FILLIT'],\
        'tot_deaths':['tot_deaths:original name deceduti + FILLIT']
        }
        for k,v in ita.items():
            ita[k].append('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv')
            ita[k].append('https://github.com/pcm-dpc/COVID-19')
        mydico = ita
    elif namedb == 'rki':
        rki = {
        'tot_deaths':['tot_deaths:FILLIT','https://github.com/jgehrcke/covid-19-germany-gae/raw/master/deaths-rki-by-ags.csv'],
        'tot_cases':['tot_cases:FILLIT','https://github.com/jgehrcke/covid-19-germany-gae/raw/master/deaths-rki-by-ags.csv'],
        }
        for k,v in rki.items():
            rki[k].append('https://github.com/jgehrcke/covid-19-germany-gae')
        mydico = rki
    elif namedb == 'escovid19data':
        esco = {
        'tot_deaths':['Cumulative deaths  (original name deceased)'],\
        'tot_cases':['Number of new COVID-19 cases detected with PCR (original name cases_accumulated_PCR)'],\
        'cur_hosp':['Hospitalized (original name hospitalized)'],\
        'tot_hosp':['Cumulative Hospitalized (original name hospitalized_accumulated)'],\
        'cur_hosp_per100k':['Intensive care per 100,000 inhabitants (original name hospitalized_per_100000'],\
        'cur_icu':['UCI, intensive care patient, (original name intensive_care)'],\
        'tot_recovered':['Recovered (original name recovered)'],\
        'tot_cases_per100k':['Cumulative cases per 100,000 inhabitants (original name cases_per_cienmil)'],\
        'cur_icu_per1M' :['Intensive care per 1000,000 inhabitants (original name intensive_care_per_1000000)'],\
        'tot_deaths_per100k':['Cumulative deaths per 100,000 inhabitants (original name deceassed_per_100000)'],\
        'tot_cases_per100k':['Intensive care per 100,000 inhabitants, (original name hospitalized_per_100000)'],\
        'incidence':['Cases in 14 days by 100,000 inhabitants (original name ia14'],\
        'population':['Inhabitants of the province (orignal name poblacion)'],\
        }
        for k,v in esco.items():
            esco[k].append('https://raw.githubusercontent.com/montera34/escovid19data/master/data/output/covid19-provincias-spain_consolidated.csv')
            esco[k].append('https://github.com/montera34/escovid19data')
        mydico = esco
    elif namedb == 'sciensano':
        sci = {
        'cur_hosp':['Total number of lab-confirmed hospitalized COVID-19 patients at the moment of reporting, including ICU (prevalence) (original name TOTAL_IN)'],\
        'cur_icu':['Total number of lab-confirmed hospitalized COVID-19 patients in ICU at the moment of reporting (prevalence) (original name TOTAL_IN_ICU)'],\
        'cur_resp':['Total number of lab-confirmed hospitalized COVID-19 patients under respiratory support at the moment of reporting (prevalence) (original name TOTAL_IN_RESP)'],\
        'cur_ecmo':['Total number of lab-confirmed hospitalized COVID-19 patients on ECMO at the moment of reporting (prevalence) (orginale name TOTAL_IN_ECMO)']
        }
        for k,v in sci.items():
            sci[k].append('https://epistat.sciensano.be/Data/COVID19BE_HOSP.csv')
            sci[k].append('https://epistat.wiv-isp.be/covid/')
        mydico = sci
    elif namedb == 'phe':
        url='https://api.coronavirus.data.gov.uk/v2/data?areaType=ltla&metric='
        phe = {
        'tot_deaths':['Total number of deaths (original name cumDeaths28DaysByDeathDate)',url+'cumDeaths28DaysByDeathDate'+'&format=csv'],\
        'tot_cases':['Total number of cases (originale name cumCasesBySpecimenDate)',url+'cumCasesBySpecimenDate'+'&format=csv'],
        'tot_tests':['Total number of tests (originale name cumTestByPublishDate)',url+'cumLFDTests'+'&format=csv'],
        'tot_vacc1':['Total number of tot_vacc1 (originale name cumCasesBySpecimenDate)',url+'cumPeopleVaccinatedFirstDoseByVaccinationDate'+'&format=csv'],
        'tot_vacc2':['Total number of tot_vacc2 (originale name cumCasesBySpecimenDate)',url+'cumPeopleVaccinatedSecondDoseByVaccinationDate'+'&format=csv'],
        'tot_vacc3':['Total number of tot_vacc3 (originale name cumCasesBySpecimenDate)',url+'cumPeopleVaccinatedThirddDoseByVaccinationDate'+'&format=csv'],
        'cur_B.1.617.2':['Current variant B.1.617.2',url +'https://covid-surveillance-data.cog.sanger.ac.uk/download/lineages_by_ltla_and_week.tsv'],
        }
        for k,v in phe.items():
            phe[k].append('https://coronavirus.data.gov.uk/details/download')
        mydico = phe
    elif namedb == 'dgs':
        dgs = {
            'tot_cases':['original name confirmados_1']}
        for k,v in dgs.items():
              dgs[k].append('https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/data_concelhos_new.csv')
              dgs[k].append('https://github.com/dssg-pt/covid19pt-data')
        mydico = dgs
    elif namedb == 'covidtracking':
        url='https://covidtracking.com/data/download/all-states-history.csv'
        cotra = {
            'tot_death': ['Cumulative deaths tot_death (original name death)'],\
            'tot_hosp': ['Cumulative hospitalized (original name hospitalizedCumulative)'],\
            'cur_hosp': ['Current hospitalized (original name hospitalizedCurrently)'],\
            'tot_icu': ['(original name inIcuCumulative)'],\
            'cur_icu': ['(original inIcuCurrently)'],\
            'tot_neg_test': ['(original negative)'],\
            'tot_pos_test': ['(original positive)'],\
            'tot_onVentilator': ['(original onVentilatorCumulative)'],\
            'cur_onVentilator': ['(original onVentilatorCurrently)'],\
            'tot_test': ['(original totalTestResults)'],\
        }
        for k,v in cotra.items():
            cotra[k].append(url)
            cotra[k].append('https://covidtracking.com/analysis-updates/five-major-metrics-covid-19-data')
        mydico = cotra
    elif namedb == 'risklayer':
        url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-JLawOH35vPyOk39w0tjn64YQLlahiD2AaNfjd82pgQ37Jr1K8KMHOqJbxoi4k2FZVYBGbZ-nsxhi/pub?output=csv'
        risk = {
            'tot_positive': ['tot_positive ... fill it '],\
            'tot_incidence': ['tot_incidence ... fill it'],\
            }
        for k,v in risk.items():
            risk[k].append(url)
            risk[k].append('https://www.risklayer-explorer.com/event/100/detail')
        mydico = risk
    elif namedb == 'europa':
        url='https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-region/jrc-covid-19-all-days-by-regions.csv'
        euro = {
            'tot_deaths':['Orginal name CumulativeDeceased'],
            'tot_positive':['sum the Original name CurrentlyPositive'],
            'cur_hosp':['Orginal name Hospitalized'],
            'cur_icu':['Orginal name IntensiveCare'],
            }
        for k,v in euro.items():
            euro[k].append(url)
            euro[k].append('https://github.com/ec-jrc/COVID-19/tree/master/data-by-region')
        mydico = euro
    elif namedb == 'imed':
        imed = {
        'tot_cases':['tot_cases (original name cases)',\
        'https://github.com/iMEdD-Lab/open-data/blob/master/COVID-19/greece_cases_v2.csv'],
        'tot_deaths':['tot_deaths (original name deaths)',\
        'https://github.com/iMEdD-Lab/open-data/blob/master/COVID-19/greece_deaths_v2.csv']
        }
        for k,v in imed.items():
             imed[k].append("https://github.com/iMEdD-Lab/open-data/tree/master/COVID-19")
        mydico = imed
    elif namedb == 'govcy':
        mi = {
        'tot_deaths':['total deaths attributed to Covid-19 disease (total deaths)'],\
        'tot_cases':['total number of confirmed cases (total cases)'],\
        'cur_hosp':['number of patients with covid-19 hospitalized cases (Hospitalised Cases)'],\
        'cur_severe':['number of patients with covid-19 hospitalized in severe cases (Severe Cases)'],\
        'cur_icu':['number of patients with covid-19 admitted to ICUs (Cases In ICUs)'],\
        'cur_incub':['number of patients with covid-19 admitted to ICUs (Incubated Cases)'],\
        'tot_pcr':['extract from PCR_daily tests performedtotal number of PCR tests performed (PCR_daily tests performed)'],\
        'tot_rat':['total number of rapid antigen (RAT) tests performed (total RA tests)'],\
        'tot_test':['total numbers of PCR and RA tests performed (total tests)'],\
        }
        for k,v in mi.items():
            mi[k].append("https://www.data.gov.cy/sites/default/files/CY%20Covid19%20Open%20Data%20-%20Extended%20-%20new_247.csv")
            mi[k].append("https://www.data.gov.cy/node/4617?language=en")
        mydico = mi
    elif namedb == 'mpoxgh':
        url='https://github.com/globaldothealth/monkeypox/raw/main/archives/2022-05-20.csv'
        mpoxgh = {
            'tot_confirmed': ['total confirmed cases (from Status = confirmed)'],\
            }
        for k,v in mpoxgh.items():
            mpoxgh[k].append(url)
            mpoxgh[k].append('https://github.com/globaldothealth/monkeypox')
        mydico = mpoxgh

    else:
        raise CoaKeyError('Error in the database selected, please check !')
    if keys not in mydico:
        raise CoaKeyError(keys + ': this keyword doesn\'t exist for this database !')
    else:
        return mydico[keys]
