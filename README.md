# Consulta BCB Registrato
Consulta automatizada ao serviço [Registrato](https://www.bcb.gov.br/cidadaniafinanceira/registrato) do Banco Central do Brasil

## Instalação no Windows

Pré-requisitos:

- Python 3
- Google Chrome 88.0.4324
- Cadastro no Registrato do Banco Central

Baixe o [código](https://github.com/ricardomaia/consulta-bcb-registrato/archive/main.zip) do repositório no GitHub e descompacte.

Renomeie o arquivo `config.sample.yml` para `config.yml` e insira suas credenciais.

Abra o diretório descompactado no console do Windows e execute os seguintes comandos:

```console
C:\Users\user\monitor-dados> pip install virtualenv
```

```console
C:\Users\user\monitor-dados> virtualenv env
```

Ative o ambiente virtual e instale as dependências

```console
C:\Users\user\monitor-dados> env\Scripts\activate.bat
(env) C:\Users\user\monitor-dados> pip install -r requirements.txt
```

### Execute o monitor

```console
(env) C:\Users\user\monitor-dados> python monitor-dados.py
```

O relatório será enviado para o e-mail cadastrado.
