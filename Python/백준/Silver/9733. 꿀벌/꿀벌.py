works = open(0).read().split()
total = len(works)
for c in 'Re','Pt','Cc','Ea','Tb','Cm','Ex':
    m = works.count(c)
    print(c,m,f'{m/total:.2f}')
print('Total',total,'1.00')