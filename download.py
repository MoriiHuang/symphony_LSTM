from selenium import webdriver
from lxml import etree
from time import sleep
import json
def main():
    json_file_path = '/Users/lucifer/Desktop/LSTM/data/result.json'
    with open(json_file_path,'r') as f:
        res=json.load(f)
    for i in res:
        bro=webdriver.Chrome(executable_path='./chromedriver')
        bro.get(i[0])
        sleep(1)
main()