# LibSelenium
Automação Selenium para facilitar acessos e processo

### PS: AINDA PASSARÁ POR ATUALIZAÇÕES

# Dependências do Projeto

Este arquivo lista todas as dependências do projeto e suas respectivas versões.

## Instalação

Para instalar as dependências, você pode usar o gerenciador de pacotes Python `pip`. Certifique-se de que você está no ambiente virtual correto ou global, dependendo de suas preferências.

``` Terminal
pip install -r requirements.txt
```
OU, você poderá acessar meu arquivo requirements também

## Observação:
Certifique-se de verificar regularmente se há atualizações para essas dependências e mantenha seu ambiente virtual ou projeto atualizado

# Ativação do Ambiente Virtual

Este arquivo fornece instruções sobre como ativar o ambiente virtual para o seu projeto em diferentes sistemas operacionais.

## Windows (CMD)

### Terminal DOS/CMD
Acesse o diretório do projeto e digite:
``` batch CMD
iniciar_venv.bat
```
### Power Shell
Acesse o diretório do projeto e digite:
```Power Shell
.\iniciar_venv.ps1
```

### PS: Mais adiante um .sh do Linux tb será implementado

## Caso não queira acessar de forma automatizada o meu ambiente Virtual, você pode fazer o seguinte:

### Windows (PowerShell)
Acesse o diretório do projeto e digite:
``` Power Shell
.\Libs\Scripts\Activate.ps1
```

``` Linux / macOS (Bash)
source Libs/bin/activate
```
Certifique-se de que você está no diretório raiz do seu projeto antes de executar esses comandos.

Lembre-se de que, no Windows, você pode usar tanto o CMD quanto o PowerShell, dependendo da sua preferência.

# Uso da Biblioteca Selenium

Este arquivo descreve o uso da biblioteca Selenium em seu projeto Python. A biblioteca Selenium é usada para automação de testes e interações com navegadores da web.

## Configuração do Chrome

Antes de usar o Selenium, você deve configurar o Chrome para o seu projeto. Você pode fazer isso usando o método `ConfigurarChrome` da classe `UsesSelenium`. Aqui estão alguns exemplos de como usá-lo:

``` python
driver = UsesSelenium()
# Configurar o Chrome com janela
driver.ConfigurarChrome(abrir="window", set_dir="SetPadrao")

# Configurar o Chrome sem janela (headless)
driver.ConfigurarChrome(abrir="headless", tamanho=(1920, 1080))

# Configurar o Chrome e instalar uma nova versão do chromedriver
driver.ConfigurarChrome(abrir="new_version")
```
## Abrindo uma Página da Web
Depois de configurar o Chrome, você pode abrir uma página da web usando o método `GetSearch`. Por exemplo:

``` Python
# Abrir a página do Google
driver.GetSearch("https://google.com")
```

## Extrair a URL Atual
Você pode extrair a URL atual da página aberta usando o método `ExtrairUrl`:

``` Python
#Ex do interior de sua funcionalidade
current_url = driver.ExtrairUrl()
print("URL atual:", current_url)
```

## Fechando a Execução
Para fechar o navegador, você pode usar o método `CloseSearchExecution`. Você pode escolher entre diferentes opções para fechar o navegador:

1. remove_exe=True: Fecha o navegador normalmente.
2. force_remove=True: Força o fechamento do navegador usando o comando taskkill (somente no Windows).
3. Sem parâmetros: Fecha o navegador, mas mantém os processos do Chrome abertos.

``` Python
# Fecha o navegador normalmente
driver.CloseSearchExecution(remove_exe=True)

# Força o fechamento do navegador
driver.CloseSearchExecution(force_remove=True)

# Fecha o navegador sem forçar o fechamento dos processos do Chrome
driver.CloseSearchExecution()
```

Lembre-se de que esta é apenas uma introdução ao uso do Selenium em seu projeto. Você pode personalizar ainda mais o código para suas necessidades específicas.

# Extensão da Biblioteca Selenium

Este arquivo estende o uso da biblioteca Selenium e inclui funcionalidades adicionais para automação de tarefas web.

### Você pode utilizar as funcionalidade anteriores por aqui também se preferir

## Simulando um Clique

Você pode usar o método `SimularClick` para simular um clique em uma posição específica na tela:

```python
# Simular um clique nas coordenadas (222, 222)
driver.SimularClick(posix=222, posiy=222)
```

## Inserindo Texto
Para inserir texto em campos de entrada, use o método `SimularUmTexto`:

``` Python
# Inserir o texto "Hello, Selenium!" com um intervalo de 0,5 segundos entre cada caractere
driver.SimularUmTexto("Hello, Selenium!")
```

## Carregando um Elemento
Você pode usar o método `CarregarElemento` para esperar até que um elemento seja carregado na página:

``` Python
# Esperar até que um elemento com a classe "L3eUgb" que é uma classe HTML do Google, seja carregado em até 10 segundos
driver.CarregarElemento(By.CLASS_NAME, "L3eUgb", 10)
```

## Inserindo um Elemento
Para inserir texto em um elemento, use o método `InserirElemento`:
``` Python
# Inserir texto no elemento com ID "APjFqb" após clicar nele
driver.InserirElemento(By.ID, "Selenium", "APjFqb", click=True)
```

## Clicando em um Elemento
Use o método `ClicarEmElemento` para clicar em um elemento na página:

``` Python
# Clicar em um elemento com a classe "gNO89b"
driver.ClicarEmElemento(By.CLASS_NAME, "gNO89b")
```

## Simulando o Teclado
Você pode simular o pressionamento de teclas com o método `simular_teclado`:
``` Python
# Simular pressionamento da tecla "a" três vezes
driver.simular_teclado("a", 3)
```

## Capturando uma Captura de Tela
Use o método `tirar_print` para capturar uma captura de tela de um elemento na página:
``` Python
# Capturar uma captura de tela do elemento com classe "L3eUgb"
driver.tirar_print(By.CLASS_NAME, "L3eUgb", dir_image="caminho/do/diretorio") #dir_image é opcional caso queira salvar suas imagens extraídas em outro local
```

## Mudando o Foco da Janela
O método `mudar_foco` permite mudar o foco da janela ou aba:
``` Python
# Mudar o foco para a aba padrão
driver.mudar_foco(0)
```

## Verificando a Existência de um Elemento
Use o método `VerificarExixtenciaElemento` para verificar se um elemento existe na página:

``` Python
# Verificar a existência de um elemento com classe "L3eUgb"
if driver.VerificarExixtenciaElemento(By.CLASS_NAME, "L3eUgb"):
    # Faça algo se o elemento existir
else:
    # Faça algo se o elemento não existir
```

Lembre-se de que esta é uma extensão do uso da biblioteca Selenium em seu projeto Python, e você pode personalizar ainda mais o código conforme suas necessidades específicas.

