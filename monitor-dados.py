from selenium import webdriver
import yaml
import time

with open("config.yml") as file:
    cfg = yaml.load(file, Loader=yaml.BaseLoader)


driver = webdriver.Chrome()
driver.set_window_size(1024, 768)

try:
    driver.get('https://www.bcb.gov.br/cidadaniafinanceira/registrato')

    element_acessar = driver.find_element_by_xpath(
        '/html/body/app-root/app-root/main/dynamic-comp/div/div[2]/div[1]/div/div[2]/div/h3/a')
    element_acessar.click()
    time.sleep(5)
    element_email = driver.find_element_by_id('userNameInput')
    element_email.send_keys(cfg['credentials']['cpf'])
    element_senha = driver.find_element_by_id('passwordInput')
    element_senha.send_keys(cfg['credentials']['senha'])
    element_entrar = driver.find_element_by_id('submitButton')
    element_entrar.click()
    time.sleep(5)
    element_relatorio_pix = driver.find_element_by_xpath(
        '//*[@id="home-section-cidadao"]/div[2]/relatorio-dashboard/div/div[2]/div[1]/div/div/rgt-botoes-relatorio/div/button[3]')
    element_relatorio_pix.click()
    time.sleep(2)

finally:
    driver.get_screenshot_as_file('tela.png')
    driver.quit()
