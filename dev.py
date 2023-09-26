from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import subprocess
import chromedriver_autoinstaller

class UsesSelenium:
    def __init__(self):
        self.driver = ""
        self.lista = []

    def ConfigurarChrome(self, abrir:str="", tamanho:tuple=None, disable_notifications:bool=False, Noterror_ssl:bool=False, todos:bool=False, set_dir:str=None): #headless(abre sem a janela), #window(abre com janela), #new_version(Abre o chromedriver instalando uma nova extensão chromedriver)
        try:
            self._Exibir("-=", 30)
            if set_dir != None and set_dir != "SetPadrao":
                caminho = set_dir
            elif set_dir == "SetPadrao":
                directory_atual = os.getcwd()
                directory = "Win_1147503_chrome-win\\chrome-win\\chrome.exe"
                caminho = os.path.join(directory_atual, directory)
            else:
                directory_atual = os.getcwd()
                directory = "LibSelenium\\Win_1147503_chrome-win\\chrome-win\\chrome.exe"
                # Constrói o caminho completo
                caminho = os.path.join(directory_atual, directory) #Funde os dois dirs
            # Verifique se o caminho existe
            if os.path.exists(caminho):
                print(f'O caminho para a pasta EXE do chrome padrão gerado: {caminho}')
                self.GerarTempoExecucao(5)
                options = uc.ChromeOptions()
                options.binary_location = caminho
                if tamanho != None:
                    options.add_argument(f'--window-size={str(tamanho[0])},{str(tamanho[1])}')
                elif disable_notifications == True:
                    options.add_argument('--disable-notifications')
                elif Noterror_ssl == True:
                    options.add_argument('--ignore-certificate-errors')
                elif todos == True:
                    options.add_argument('--disable-notifications')
                    options.add_argument('--ignore-certificate-errors')

                if abrir == "" or abrir == "window":
                    print("Abrindo Janela do Chrome")
                elif abrir == "headless":
                    print("Executando o chrome sem Janela")
                    options.add_argument("--headless")
                elif abrir == "new_version":
                    print("Extraindo e gerando um exe chromedriver para execução")
                    servico = Service(ChromeDriverManager().install())
                    # Obtenha o caminho para o chromedriver instalado
                    chromedriver_path = ChromeDriverManager().install()
                    print(f"Arquivo Padrão de instalação/atualização automática do path do driver: {chromedriver_path}")
                self.driver = uc.Chrome(options=options) if abrir in ["", "window", "headless"] else webdriver.Chrome(service=servico, options=options)
                self._Exibir("-=", 30)
            else:
                print(f'O caminho especificado não existe: {caminho}')
                print("Setamento da pasta para binário do chrome ou para o executável não foi encontrado!")
                print("Verifique o diretório que está usando e setando!")
                self._Exibir("==", 30)
        except Exception as e:
            print("Houve um erro no método ConfigurarChrome")
            print(f"Execption: {e}")
            self._Exibir("==", 30)


    def GetSearch(self, url):
        try:
            if not isinstance(self.driver, str):
                print("Sucesso!")
                print(f"Acessando a pesquisa {url}")
                self.driver.get(url)
            else:
                print("Erro de execução")
                print("Driver não encontrado!")
                print("Verifique se configurou o acesso chamando o Método ConfigurarChrome")
        except requests.exceptions.RequestException as re:
            print("Uma exception ocorreu no método GetSearch")
            print("Erro de requisição HTTP")
            print(f"Motivo: {re}")
        except Exception as e:
            print("Uma exception ocorreu no método GetSearch")
            print(f"Motivo: {re}")
        
    def CloseSearchExecution(self, remove_exe:bool=False, force_remove:bool=False):
        try:
            self._Exibir("==", 30)
            if remove_exe == True:
                print("Sucesso!")
                print("Fechando o navegador com executável...")
                self.driver.close()
                self.GerarTempoExecucao(3, amostra=True)
                self.driver.quit()
                print("Fechado!")
            elif force_remove == True:
                print("Sucesso!")
                print("forçando o fechamento do navegador com executável...")
                print("Verrificando Processos...")
                self.GerarTempoExecucao(5, amostra=True)
                try:
                     subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'], check=True)
                     print("processos removidos com êxito")
                except:
                    print("Sem processos abertos")
            else:
                from prettytable import PrettyTable
                dados = [["remove_exe=True", "force_remove=True"]]
                tabela = PrettyTable()
                tabela.field_names = ["Remover Via Selenium", "Remover via terminal"]
                # Adicione os dados à tabela
                for linha in dados:
                    tabela.add_row(linha)
                print("Fechando o navegador")
                print("OBS: Os processos do chrome se mantém abertos após essa execução")
                print(f"Caso queira, para fechar os processos do chrome, chame novamente o método e/ou execute os parâmetro:\n{tabela}")
                self.driver.close()
                self._Exibir("==", 30)
        except Exception as e:
            print("Uma excption ocorreu no método Fechar CloseSearchExecution")
            print(f"Motivo: {e}")
            try:
                subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'], check=True)
            except:
                print("Sem processos abertos")
            self._Exibir("--", 30)


    def GerarTempoExecucao(self, tempo:float=5, amostra:bool=False):
        from time import sleep
        try:
            print("Gerando tempo de execução...")
            if amostra == True:
                n = self.__gerar_lista(tempo)
                for i in n:
                    t = str(i)
                    x = t.rjust(len(str(tempo)), " ")
                    print(f"A execução terminará em: {x}", end="\r")
                    sleep(1)
                print()
            else:
                sleep(tempo)
        except Exception as e:
            print("Ocorreu um erro no método GerarTempoExecucao")
            print(f"Motivo: {e}")


    def ExtrairUrl(self):
        try:
            self._Exibir("-=", 30)
            print("Buscando a URL atual....")
            self.GerarTempoExecucao(5, True)
            current_url = self.driver.current_url
            if current_url:
                print("Sucesso!")
                print("URL atual:", current_url)
                self._Exibir("-=", 30)
                return current_url
            else:
                print("Um erro ocorreu no método ExtrairUrl")
                print(f"Não foi possível extrair os dados de URL para busca {current_url}")
                return None
        except Exception as e:
            print("Uma exception ocorreu na função ExtrairUrl")
            print("Motivo:", e)
            self._Exibir("==", 30) 


    def __gerar_lista(self, numero):
        while numero >= 0:
            self.lista.append(numero)
            numero -= 1
        return self.lista


    def _Exibir(self, string, tamanho):
        print(string * tamanho)


if __name__ == "__main__":
    driver = UsesSelenium()
    driver.ConfigurarChrome("window", set_dir="SetPadrao")
    driver.GetSearch("https://google.com")
    driver.ExtrairUrl()
    driver.CloseSearchExecution(remove_exe=True)
    #driver.simular_teclado("a", 3)
    #driver.GerarTempoExecucao(4, True)
    #driver.simular_teclado("backspace", 3)
