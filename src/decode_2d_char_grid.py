
import requests

url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print(url)

urlDataHtml = requests.get(url).text

from bs4 import BeautifulSoup

soup = BeautifulSoup(urlDataHtml, "html.parser")

class RowData:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

rowDataList = []
maxX = 0
maxY = 0
for table in soup.find_all("table"):
    rows = []
    row = 0
    for tr in table.find_all("tr"):

        if row > 0:
            x = -1
            y = -1
            char = ' '
            col = 0
            for td in tr.find_all(["td", "th"]):
                cellString = td.get_text(strip=True)
                if col == 0:
                    x = int(cellString)
                    maxX = max(maxX, x)
                elif col == 1:
                    char = cellString[0] if cellString else ' '
                elif col == 2:
                    y = int(cellString)
                    maxY = max(maxY, y)
                col += 1
            if x != -1 and y != -1 and char != ' ':
                rowDataList.append(RowData(x, y, char))
        row += 1

# create char matrix with dimensions maxX+1 by maxY+1
charMatrix = [[' ' for _ in range(maxY + 1)] for _ in range(maxX + 1)]

# fill the char matrix with row data
for rowData in rowDataList:
    charMatrix[rowData.x][rowData.y] = rowData.char

# print the char matrix
for row in charMatrix:
    print(''.join(row))
