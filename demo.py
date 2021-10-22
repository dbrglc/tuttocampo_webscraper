from selenium import webdriver
import lxml.html as lh
from decouple import config

browser = webdriver.Safari()
browser.get(config('LINK'))
innerHTML = browser.execute_script("return document.body.innerHTML")
browser.quit()
tree = lh.fromstring(innerHTML)
righe = tree.xpath('//*[@id="ranking"]/table/tbody/tr')

classifica = [['Team', 'Points', 'Match Played', 'Wins', 'Draws', 'Loses', 'Goal Made', 'Goal Taken', 'Goal difference']]

for riga in righe:
    secondo = [item.text_content().replace("\n", "") for item in riga.xpath('td')]
    classifica.append([i for i in secondo if i])

s = [[str(e) for e in row] for row in classifica]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print ('\n'.join(table))