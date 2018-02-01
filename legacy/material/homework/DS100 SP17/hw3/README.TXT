Files
-----
README.TXT: This file.
D11: Transaction data collected in November, 2000
D12: Transaction data collected in December, 2000
D01: Transaction data collected in January, 2001
D02: Transaction data collected in February, 2001

Format of Transaction Data
--------------------------
First line: Column definition in Traditional Chinese
    日期;會員卡號;年齡;區域;商品分類;商品編碼;數量;成本;銷售
Second line and the rest: data columns separated by ";"

Column definition
-----------------
1: Transaction date and time (time invalid and useless)
2: Customer ID
3: Age: 10 possible values,
   A <25,B 25-29,C 30-34,D 35-39,E 40-44,F 45-49,G 50-54,H 55-59,I 60-64,J >65
4: Residence Area: 8 possible values, 
   A-F: zipcode area: 105,106,110,114,115,221,G: others, H: Unknown
   Distance to store, from the closest: 115,221,114,105,106,110
5: Product subclass
6: Product ID
7: Amount
8: Asset
9: Sales price