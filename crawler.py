
import aiohttp
import asyncio
from lxml import etree
import os
import json
json_file_path = '/Users/lucifer/Desktop/LSTM/data/result.json'
json_file=open(json_file_path,mode='w')
async def get_url():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://midi.midicn.com/%E5%8F%A4%E5%85%B8%E9%9F%B3%E4%B9%90MIDI') as resp:
            print(resp.status)
            data=await resp.text()
            return data
def get_html(resp):
    result=[]
    root=etree.HTML(str(resp))
    source=root.xpath('//*[@id="content"]/article/div[2]/ul/li')
    for value in source:
        result.append(value.xpath('a/@href'))
    return result

resp=asyncio.run(get_url())
res=get_html(resp)
json.dump(res,json_file)



