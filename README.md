# Top 5 Melhores Sinais Olt Fiberhome
Script de automação

## Sobre
Script desenvolvido em `Python` utilizando a biblioteca `Subprocess` e `Os` para executar comandos em shell em uma maquina `Linux` para coletar os dados via `SNMPWALK` de RX Power da OLT e ONUs, enviando as informações coletadas por meio de `zabbix_sender` para o servidor `Zabbix`, que integrado ao `Grafana` apresenta as informações de forma organizada.

### Versões usadas
```
ZABBIX  v6.0.2
GRAFANA v8.4.4
```

### Requisitos
```
apt-get install zabbix-sender / yum install zabbix-sender
apt-get install python3 / yum install python3
apt-get install snmpd snmp
pip3 install subprocess.run
```

### SNMPWALK

| Option | Description |
|-----------------|------------------------------------------------------------|
| -v | Specifies the SNMP version you want to use |
| -c | Sets a community string |
| hostname | The SNMP agent name |
| object_id | Specify an object ID to return all SNMP objects below it |

__Exemplo:__

`snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME OID_SNMP`

`snmpwalk -v2c -c COMMUNITY_STRING IP_OLT_FIBERHOME .1.3.6.1.4.1.5875.800.3.9.3.3.1.6`

`snmpwalk -v 1 -c public localhost sysname`

### Permissão
```
chmod a+x /usr/lib/zabbix/externalscripts/script_melhores_sinais_olt.py
```

### Crontab
- [Crontab Editor](https://crontab.guru/)
```
crontab -e
30 * * * * /usr/bin/python3 /usr/lib/zabbix/externalscripts/script_melhores_sinais_olt.py
```

### MIBs
- [GEPON-OLT-COMMON-MIB](http://www.circitor.fr/Mibs/Html/G/GEPON-OLT-COMMON-MIB.php)

### Itens Zabbix Trapper
![](item_zabbix_trapper.png)

### Tabela no Grafana
![](tabela_grafana.png)

### Créditos
__Desenvolvido por:__
```
Gabriel Aparecido Zucoloto
```
- [Linkedin](https://www.linkedin.com/in/gabriel-zucoloto-51a51b231)
- [Portfolio](https://bielzucoloto.github.io/)
