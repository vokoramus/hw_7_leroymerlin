# import re
#
# href = 'https://spb.leroymerlin.ru/product/shkaf-napolnyy-dub-shato-80x86x60-sm-82550141/'
#
# p = re.compile(r'\/([^\/]+)\/$')
# m = p.search(href)
#
# href_2 = m.group(1)
# print(href_2)  # 'shkaf-napolnyy-dub-shato-80x86x60-sm-82550141'
#
# p = re.compile(r'(\d+)$')
# m = p.search(href_2)
# print(m.group(1))

from os.path import join
p = 'karkas-navesnoy-delinia-id-80x768x35-sm-82000371'
f = 'f1c3f3ff55f8a5651d307d4993e5331e04ed6251.jpg'
print(join(p, f))
