#!/usr/bin/python3
import requests
import subprocess
import os

sinais_onu = os.popen('snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.3.1.6 | cut -d "." -f15 | cut -d " " -f1,4 | sort -k 2 | head -n 5').read()

lista_onu = []

lista_onu.append(sinais_onu)
x = lista_onu[0].split("\n")

sinal_1_onu = (x[0]).split(" ")
sinal_2_onu = (x[1]).split(" ")
sinal_3_onu = (x[2]).split(" ")
sinal_4_onu = (x[3]).split(" ")
sinal_5_onu = (x[4]).split(" ")

pon_do_sinal_1 = os.popen('snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.3.1.2.{} | cut -d ":" -f2 | cut -d " " -f2,3'.format(sinal_1_onu[0])).read()
pon_do_sinal_2 = os.popen('snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.3.1.2.{} | cut -d ":" -f2 | cut -d " " -f2,3'.format(sinal_2_onu[0])).read()
pon_do_sinal_3 = os.popen('snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.3.1.2.{} | cut -d ":" -f2 | cut -d " " -f2,3'.format(sinal_3_onu[0])).read()
pon_do_sinal_4 = os.popen('snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.3.1.2.{} | cut -d ":" -f2 | cut -d " " -f2,3'.format(sinal_4_onu[0])).read()
pon_do_sinal_5 = os.popen('snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.3.1.2.{} | cut -d ":" -f2 | cut -d " " -f2,3'.format(sinal_5_onu[0])).read()

sinal_top_1_onu = (pon_do_sinal_1.replace("\n","").replace('"',""), sinal_1_onu[1][:3]+'.'+sinal_1_onu[1][3:])
sinal_top_2_onu = (pon_do_sinal_2.replace("\n","").replace('"',""), sinal_2_onu[1][:3]+'.'+sinal_2_onu[1][3:])
sinal_top_3_onu = (pon_do_sinal_3.replace("\n","").replace('"',""), sinal_3_onu[1][:3]+'.'+sinal_3_onu[1][3:])
sinal_top_4_onu = (pon_do_sinal_4.replace("\n","").replace('"',""), sinal_4_onu[1][:3]+'.'+sinal_4_onu[1][3:])
sinal_top_5_onu = (pon_do_sinal_5.replace("\n","").replace('"',""), sinal_5_onu[1][:3]+'.'+sinal_5_onu[1][3:])

subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.onu.1 -o '{}'".format(sinal_top_1_onu[0] + " " + sinal_top_1_onu[1]), shell=True)
subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.onu.2 -o '{}'".format(sinal_top_2_onu[0] + " " + sinal_top_2_onu[1]), shell=True)
subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.onu.3 -o '{}'".format(sinal_top_3_onu[0] + " " + sinal_top_3_onu[1]), shell=True)
subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.onu.4 -o '{}'".format(sinal_top_4_onu[0] + " " + sinal_top_4_onu[1]), shell=True)
subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.onu.5 -o '{}'".format(sinal_top_5_onu[0] + " " + sinal_top_5_onu[1]), shell=True)

sinais_olt = os.popen('snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.7.1.2 | cut -d "." -f15,16 | cut -d " " -f1,4 | sort -k 2 | head -n 5').read()

lista_olt = []

lista_olt.append(sinais_olt)
y = lista_olt[0].split("\n")

sinal_1_olt = (y[0]).split(" ")
sinal_2_olt = (y[1]).split(" ")
sinal_3_olt = (y[2]).split(" ")
sinal_4_olt = (y[3]).split(" ")
sinal_5_olt = (y[4]).split(" ")

valor_olt_1 = sinal_1_olt[0].split(".")
valor_olt_2 = sinal_2_olt[0].split(".")
valor_olt_3 = sinal_3_olt[0].split(".")
valor_olt_4 = sinal_4_olt[0].split(".")
valor_olt_5 = sinal_5_olt[0].split(".")

sinal_top_1_olt = sinal_1_olt[1][:3]+'.'+sinal_1_olt[1][3:]
sinal_top_2_olt = sinal_2_olt[1][:3]+'.'+sinal_2_olt[1][3:]
sinal_top_3_olt = sinal_3_olt[1][:3]+'.'+sinal_3_olt[1][3:]
sinal_top_4_olt = sinal_4_olt[1][:3]+'.'+sinal_4_olt[1][3:]
sinal_top_5_olt = sinal_5_olt[1][:3]+'.'+sinal_5_olt[1][3:]

index_lista = [["369623040","PON 11/1/"],["370147328","PON 11/2/"],["370671616","PON 11/3/"],["371195904","PON 11/4/"],["371720192","PON 11/5/"],["372244480","PON 11/6/"],["372768768","PON 11/7/"],["373293056","PON 11/8/"],["403177472","PON 12/1/"],["403701760","PON 12/2/"],["404226048","PON 12/3/"],["404750336","PON 12/4/"],["405274624","PON 12/5/"],["405798912","PON 12/6/"],["406323200","PON 12/7/"],["406847488","PON 12/8/"],["436731904","PON 13/1/"],["437256192","PON 13/2/"],["437780480","PON 13/3/"],["438304768","PON 13/4/"],["438829056","PON 13/5/"],["439353344","PON 13/6/"],["439877632","PON 13/7/"],["440401920","PON 13/8/"],["470286336","PON 14/1/"],["470810624","PON 14/2/"],["471334912","PON 14/3/"],["471859200","PON 14/4/"],["472383488","PON 14/5/"],["472907776","PON 14/6/"],["473432064","PON 14/7/"],["473956352","PON 14/8/"],["503840768","PON 15/1/"],["504365056","PON 15/2/"],["504889344","PON 15/3/"],["505413632","PON 15/4/"],["505937920","PON 15/5/"],["506462208","PON 15/6/"],["506986496","PON 15/7/"],["507510784","PON 15/8/"]]

for item in index_lista:
    if (item[0]) == (valor_olt_1[0]):
        subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.olt.1 -o '{}'".format(item[1] + valor_olt_1[1] + " " + sinal_top_1_olt), shell=True)
    if (item[0]) == (valor_olt_2[0]):
        subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.olt.2 -o '{}'".format(item[1] + valor_olt_2[1] + " " + sinal_top_2_olt), shell=True)
    if (item[0]) == (valor_olt_3[0]):
        subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.olt.3 -o '{}'".format(item[1] + valor_olt_3[1] + " " + sinal_top_3_olt), shell=True)
    if (item[0]) == (valor_olt_4[0]):
        subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.olt.4 -o '{}'".format(item[1] + valor_olt_4[1] + " " + sinal_top_4_olt), shell=True)
    if (item[0]) == (valor_olt_5[0]):
        subprocess.run("zabbix_sender -z IP_ZABBIX -s NOME_HOST -k melhor.sinal.olt.5 -o '{}'".format(item[1] + valor_olt_5[1] + " " + sinal_top_5_olt), shell=True)


