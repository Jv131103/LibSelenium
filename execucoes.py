from dev import UsesSelenium
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import os
from PIL import Image


class UsosSelenium(UsesSelenium):
    def __init__(self):
        super().__init__()
    
    def SimularClick(self, posix:int=222, posiy:int=222):
        try:
            print("Simulando um click")
            pyautogui.moveTo(posix, posiy)
            self.GerarTempoExecucao(2)
            pyautogui.click()
            self.GerarTempoExecucao(5)
        except Exception as e:
            print("Uma exception ocorreu no método SimularClick")
            print(e)
        

    def SimularUmTexto(self, txt):
        try:
            if not isinstance(txt, str):
                print("Um erro ocorreu no método SimularUmTexto")
                print("O parâmetro txt precisa ser uma string")
            else:
                pyautogui.write(txt, interval=0.5)
        except Exception as e:
            print("Uma exception ocorreu no Método SimularUmTexto")
            print("Motivo")

    def CarregarElemento(self, by:By, element_address:str, temp:int):
        try:
            if not isinstance(element_address, str):
                print("Erro Gerado em elemento:")
                print("Precisa ser uma string")
            else:
                wait = WebDriverWait(self.driver, temp)
                print(f"Buscando o elemento de endereço {element_address}")
                try:
                    wait.until(EC.presence_of_element_located((by, element_address)))
                    print("Elemento encontrado")
                except Exception as e:
                    print(f"Erro ao localizar ou carregar o elemento {element_address} usando o locador {by}")
                    print(f"Motivo do erro: {e}")
        except Exception as e:
            print("Uma exceção ocorreu no método CarregarElemento!")
            print(f"Motivo: {e}")


    def InserirElemento(self, by:By, text:str, element_address:str, click=False):
        try:
            if not isinstance(element_address, str):
                print("Erro Gerado no método element_adrees")
                print("Não foi possível definir o endereço padrão do elemento")
                print("Precisa ser uma string")
            if not isinstance(text, str):
                print("Erro Gerado no método text")
                print("Não foi possível definir o texto a ser inserido no elemento")
                print("Precisa ser uma string")
            else:
                print(f"Buscando o elemento de endereço {element_address}")
                try:
                    if click == True:
                        elemento = self.driver.find_element(by, element_address)
                        elemento.click()
                        self.GerarTempoExecucao(2)
                        elemento.send_keys(text)
                    else:
                        print(f"Inserindo o elemento {element_address}")
                        self.driver.find_element(By.ID, element_address).send_keys(text)
                        print("Dado inserido com êxito!")
                except Exception as e:
                    print(f"Erro ao localizar ou carregar o elemento {element_address} usando o locador {by}")
                    print(f"Motivo do erro: {e}")
        except Exception as e:
            print("Uma exceção ocorreu no método CarregarElemento!")
            print(f"Motivo: {e}")


    def ClicarEmElemento(self, by, element_adress):
        try:
            if not isinstance(element_adress, str) or element_adress == "":
                print("Erro na execução do Método ClicarEmElemento!")
                print("Motivo: O valor inserido no parâmetro precisa ser uma string e não pode ser vazio!")
            else:
                if by == By.ID or by == By.XPATH or by == By.CLASS_NAME or by == By.CSS_SELECTOR or by == By.NAME:
                    print("Clicando em elemento....")
                    print(f"Verificando o endereço de elemento {element_adress}")
                    self.driver.find_element(by, element_adress).click()
                    print("Item clicado com sucesso!")
                else:
                    print("Erro na execução do Método ClicarEmElemento!")
                    print("Motivo: O valor inserido no parâmetro by não corresponde a um valor existente!")
        except Exception as e:
            print("Uma excption ocorreu no método ClicarEmElemento!!!")
            print(f"Motivo: {e}")


    def simular_teclado(self, simular_tecla=None, loop=0):
        try:
            if simular_tecla is not None:
                if loop > 0:
                    while loop > 0:
                        keyboard.press_and_release(simular_tecla)
                        loop -= 1
                else:
                    keyboard.press_and_release(simular_tecla)
            else:
                print("Um erro ocorreu no Método simular_teclado:")
                print("Nenhuma tecla fornecida para simulação.")
        except Exception as e:
            print(f"Ocorreu um erro ao simular a tecla: {e}")

    def tirar_print(self, by, element_adress, dir_image=None):
        try:
            self._Exibir("==", 30)
            if dir_image is None:
                print("Setando localmente a pasta image")
                directory_atual = os.getcwd()
                directory = "image"
                # Constrói o caminho completo
                caminho = os.path.join(directory_atual, directory)
            elif dir_image != None:
                caminho = dir_image
            else:
                print("Houve um erro no método tirar_print")
                print("Caminho de dir de imagem não setado!")
            print(f"Caminho completo: {caminho}")
            print("Printando a imagem")
            # Salvar a imagem do elemento específico
            element = self.driver.find_element(by, element_adress)
            location = element.location
            size = element.size
            page_image_path = os.path.join(caminho, "pageImage.png")
            print(f"Salvando imagem da tela em {page_image_path}")
            self.driver.save_screenshot(page_image_path)
            x = location["x"]
            y = location["y"]
            width = location["x"] + size["width"]
            height = location["y"] + size["height"]
            im = Image.open(page_image_path)
            im = im.crop((int(x), int(y), int(width), int(height)))
            element_image_path = os.path.join(caminho, "element_image.png")
            print(f"Salvando imagem extraída em {element_image_path}")
            im.save(element_image_path)
        except FileNotFoundError as fnfe:
            print("Arquivo não encontrado no método tirar_print:", fnfe)
        except Exception as e:
            print("Uma exception ocorreu no método tirar_print:")
            print("Motivo:", e)
        self._Exibir("--", 30)
    

    def mudar_foco(self, indice_da_aba=-1):
        # Caso queira voltar a aba padrão, no parâmetro indice_da_aba digite apenas 0
        try:
            # Mudar o foco para a nova janela (ou aba) que foi aberta após o clique
            self.driver.switch_to.window(self.driver.window_handles[indice_da_aba])
        except IndexError as ie:
            print("Índice de janela/aba inválido na função mudar_foco:", ie)
        except Exception as e:
            print("Erro de janelas na função mudar_foco")
            print(e)

    
    def VerificarExixtenciaElemento(self, by, element_adress):
        try:
            self._Exibir("--", 30)
            if not isinstance(element_adress, str):
                print("Erro Gerado em elemento:")
                print("Precisa ser uma string")
            else:
                print(f"Buscando o elemento {element_adress}")
                elemento = self.driver.find_element(by, element_adress)
                self.GerarTempoExecucao(amostra=True)
                if elemento:
                    print("O elemento inserido foi encontrado na página.")
                    print("Sucess = True")
                    return True
                else:
                    print("O elemento inserido não foi encontrado na página.")
                    print("Sucess = False")
                    return False
        except NoSuchElementException as nsee:
            print("Houve uma exception no Método VerificarExixtenciaElemento!") 
            print(f"O elemento {element_adress} não foi encontrado na página.")
            print(f"Detalhes mais específicos do erro: {nsee}")
            return False
        except Exception as e:
            print("Houve uma exception no Método VerificarExixtenciaElemento!")
            print("Não foi possível verificar dado!")
            print(f"Motivo: {e}")
            return False
        self._Exibir("--", 30)

if __name__ == "__main__":
    driver = UsosSelenium()
    driver.ConfigurarChrome("window", set_dir="SetPadrao")
    driver.GetSearch("https://google.com")
    driver.ExtrairUrl()
    driver.CarregarElemento(By.CLASS_NAME, "L3eUgb", 10)
    if driver.VerificarExixtenciaElemento(By.CLASS_NAME, "L3eUgb"):
        driver.InserirElemento(By.ID, "Selenium", "APjFqb", True)
        driver.ClicarEmElemento(By.CLASS_NAME, "gNO89b")
        driver.CloseSearchExecution(True)
    else:
        print("Não foi possível terminar a execução")
    #driver.simular_teclado("a", 3)
    #driver.GerarTempoExecucao(4, True)
    #driver.simular_teclado("backspace", 3)

