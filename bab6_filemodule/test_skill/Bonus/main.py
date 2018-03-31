import module as m

m1 = m.read('MatrixA')
m2 = m.read('MatrixB')

result = m.multiple(m1, m2)

m.write(result, 'MatrixC')
