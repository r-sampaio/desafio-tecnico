# desafio-tecnico

## Requisitos:
- Python 3x
- PIP
- Selenium

## Instalação das dependencias
- pip install -r requirements.txt

## Drivers

Faça o download do driver para a versão do Google Chrome instalado na maquina.

Chrome: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Extraia o arquivo para a pasta raiz do script: ```%PATH%/desafio-tecnico```

## Modos de execução do script:

##### Para alternar entre os modos de execução basta comentar ou e descomentar as opções desejadas 


#### 1º : O script executa com um parametro de busca pré definido sendo ```falta de agua```.
```python
$ python parsing.py
```

#### 2º : O script executa a busca usando o parametro que foi passado via argumento.
```python
$ python parsing.py "falta de agua"
```

#### 3º : O script pede o parametro de busca via impute do usuario depois de executado.
```python
$ python parsing.py
$ Digite o que produra: falta de agua
```

#### O resultado dos três exemplos acima seriam esse:

```
Embasa explica falta de água em diversos locais de Feira de Santana

Acorda Cidade
Em reposta às reclamações divulgadas no programa Acorda Cidade, enviadas via WhatsApp, sobre falta de água em alguns locais de Feira de Santana, a Empresa Baiana de Saneamentos e Águas (Embasa) enviou uma nota com explicações sobre a interrupção do fornecimento.

Segundo a empresa, em função de uma falha elétrica no equipamento que bombeia água, houve uma interrupção no fornecimento de água em algumas localidades do distrito de Maria Quitéria, como Candeia Grossa. O equipamento já foi substituído e o abastecimento está sendo regularizado gradativamente.

Em relação ao distrito da Matinha, estão sendo registradas baixas pressões na rede de distribuição de algumas localidades, em decorrência da elevação da temperaturas e o consequente aumento do consumo de água. Mas a Embasa já está fazendo ajustes operacionais para normalizar o abastecimento.

Nos distritos de Jaguara e Bonfim de Feira, que são abastecidos pelo Sistema Integrado de Santo Estevão, ocorreram quedas de energia e um vazamento na adutora, que afetaram o fornecimento de água para a população local. O vazamento já foi corrigido, as tensões da rede elétrica de Estação de Tratamento de Água foi regularizada pela Coelba, e os técnicos estão trabalhando para normalizar o abastecimento nas próximas 48 horas.

Em Ipuaçu, um equipamento de bombeamento quebrou, mas a Embasa já fez os reparos necessários e o abastecimento está sendo restabelecido.
```