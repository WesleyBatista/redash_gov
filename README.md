# Implementação do Redash para o HACKATHON DA SAÚDE 2017

Vamos usar open source no governo!

## Demo

<img src="https://cloud.githubusercontent.com/assets/71468/17391289/8e83878e-5a1d-11e6-8938-af9054a33b19.gif" width="60%"/>

You can try out the demo instance: http://demo.redash.io/ (login with any Google account).


#### Example of transforming the data to upload to mariadb instance

```
python ./scripts/cli.py /home/wesleybatista/Documentos/Saude/CeInfo/EstabSUS/Listagem Estabelecimentos SMS _Gerenc End Coord Geog Hor+írio_2017-03-24.xlsx stabsus_data.csv ./scripts/stabsus_dict.json
```
