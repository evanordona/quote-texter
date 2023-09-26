# encoding: utf-8
import asyncio
from pyppeteer import launch
import re

prog = re.compile('[a-zA-Z]')

URL = 'https://mythgyaan.com/motivational-anime-quotes/'
FILE_NAME = 'quotes.txt'

f = open(FILE_NAME, "w", encoding='utf-8')

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(URL)

    elements = await page.querySelectorAll('h3')

    for element in elements:
        text_content = await page.evaluate('(element) => element.textContent', element)
        
        # while the first char in text_content is not a letter, remove it
        while not bool(prog.match(text_content[0])):
            text_content = text_content[1::]

        f.write(text_content + "\n")

    f.close()
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())