# desafio-tecnico

## Requisitos:
- Python 3x
- PIP
- Selenium
- SQLAlchemy

## Instalação das dependencias
- pip install -r requirements.txt

## Drivers

Faça o download do driver para a versão do Google Chrome instalado na maquina.

Chrome: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Extraia o arquivo para a pasta raiz do script: ```%PATH%/desafio-tecnico```

## Modo de execução do script:

#### Execute o script:
```python
$ python parsing.py
```

#### Digite ```"S"``` ou ```"N"``` para as opções com no exemplo abaixo e o termo para buscar no site Acorda Cidade

> 1º Mostrando o resultado no navegador

```python
Deseja abrir o navegador? [S/N]: s
Deseja maximizar a janela? [S/N]: n
Deseja exibir aviso/erros no terminal? [S/N]: n
Deseja encerrar o navegador? [S/N]: n
Digite o que produra: termo para busca
```

> 2º Mostrando o resultado no terminal

```python
Deseja abrir o navegador? [S/N]: n
Deseja exibir aviso/erros no terminal? [S/N]: n
Deseja encerrar o navegador? [S/N]: n
Digite o que produra: termo para busca
```

> \* No campo "Digite o que produra:" se nao for passado nenhum termo para busca ele procura por "falta de agua" dando o resultado a baixo no terminal ou abrindo a pagina no navegador.

```
Embasa explica falta de água em diversos locais de Feira de Santana

Acorda Cidade Em reposta às reclamações divulgadas no programa Acorda Cidade, enviadas via WhatsApp, sobre falta de água em alguns locais de Feira de Santana, a Empresa Baiana de Saneamentos e Águas (Embasa) enviou uma nota com explicações sobre a interrupção do fornecimento.

Segundo a empresa, em função de uma falha elétrica no equipamento que bombeia água, houve uma interrupção no fornecimento de água em algumas localidades do distrito de Maria Quitéria, como Candeia Grossa. O equipamento já foi substituído e o abastecimento está sendo regularizado gradativamente.

Em relação ao distrito da Matinha, estão sendo registradas baixas pressões na rede de distribuição de algumas localidades, em decorrência da elevação da temperaturas e o consequente aumento do consumo de água. Mas a Embasa já está fazendo ajustes operacionais para normalizar o abastecimento.

Nos distritos de Jaguara e Bonfim de Feira, que são abastecidos pelo Sistema Integrado de Santo Estevão, ocorreram quedas de energia e um vazamento na adutora, que afetaram o fornecimento de água para a população local. O vazamento já foi corrigido, as tensões da rede elétrica de Estação de Tratamento de Água foi regularizada pela Coelba, e os técnicos estão trabalhando para normalizar o abastecimento nas próximas 48 horas.

Em Ipuaçu, um equipamento de bombeamento quebrou, mas a Embasa já fez os reparos necessários e o abastecimento está sendo restabelecido.
```
#### O site não tem um padrão para a primeira TAG ```<p>``` para mostrar a localidade da matéria ou nome do autor mas em algumas matérias ela aparece como parte do paragrafo da matéria e em outro ela não aparece e foi mantida por falta de um padrão na resposta.
