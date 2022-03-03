from cgitb import text
from tkinter import *
from turtle import width
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def acesso():
    user = user_input.get()
    senha = password_input.get()
    hashtag = hashtag_input.get()

    driver = webdriver.Firefox(executable_path=r'C:\Users\joao.matias\Desktop\teste\interface - InstagramBot\geckodriver.exe')
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    username = driver.find_element_by_name('username')
    username.send_keys(user)
    time.sleep(1)
    password = driver.find_element_by_name('password')
    password.send_keys(senha)
    time.sleep(1)

    entrar = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    entrar.click()
    time.sleep(5)
    
    driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
    time.sleep(5)

    for i in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 

    comeco = driver. find_element_by_class_name('_9AhH0')
    comeco.click()

    while True:
        passar = driver.find_element_by_css_selector(".l8mY4 > button:nth-child(1)")
        passar.click()
        time.sleep(2)
        try:
            seguir = driver.find_element_by_css_selector("button.sqdOP:nth-child(2)")
            seguir.click()
            time.sleep(1)
        except Exception:
            pass
        try:
            cancelar = driver.find_element_by_css_selector("button.aOOlW:nth-child(2)")
            cancelar.click()
            time.sleep(1)
        except Exception:
            pass
        like = driver.find_element_by_css_selector(".fr66n > button:nth-child(1)")
        like.click()
        time.sleep(2)

janela = Tk() #comeco da janela
janela.title("BOT LIKE")
janela.geometry('250x125')

user_text = Label(janela, text='Usuário:', pady=5)
user_text.grid(column=0, row=0)
password_text = Label(janela, text='Senha:', pady=5)
password_text.grid(column=0,row=1)
hashtag_text = Label(janela, text='Hashtag:', pady=5)
hashtag_text.grid(column=0, row=2)
envia = Button(janela, text='ENVIAR', command=acesso, pady=5)
envia.grid(column=1, row=3)

user_input = Entry(janela, width=30)
user_input.grid(column=1, row=0)
password_input = Entry(janela, width=30, show='*')
password_input.grid(column=1, row=1)
hashtag_input = Entry(janela, width=30)
hashtag_input.grid(column=1, row=2)

janela.mainloop() #fim da janela