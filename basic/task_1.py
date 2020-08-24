"""

Task 1. Write a function that implements the output
of the multiplication table
dimension AｘB. The first and second factors must be set
as function arguments. String elements
(elements of the multiplication table) must be separated by tabs.

Example:
Multiplication table 10x10:
0	1	2	3	4	5	6	7	8	9	10
1	1	2	3	4	5	6	7	8	9	10
2	2	4	6	8	10	12	14	16	18	20
3	3	6	9	12	15	18	21	24	27	30
4	4	8	12	16	20	24	28	32	36	40
5	5	10	15	20	25	30	35	40	45	50
6	6	12	18	24	30	36	42	48	54	60
7	7	14	21	28	35	42	49	56	63	70
8	8	16	24	32	40	48	56	64	72	80
9	9	18	27	36	45	54	63	72	81	90
10	10	20	30	40	50	60	70	80	90	100

Pay attention to the first row and column!
At the intersection of their elements,
the desired values ​​are found.
THESE ROW AND COLUMN MUST BE!

"""

def multiplication_table(x, y):
    for i in range(x + 1):
        print(i, end='\t')
    print('\r')
    for i in range(1, y + 1):
        print(i, end='\t')
        for j in range(1, x + 1):
            print(i * j, end='\t')
        print('\r')
    print()

multiplication_table(10, 10)

def multiplication_table_1(x, y):
    for i in range(y + 1):
        row = []
        for j in range(x + 1):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(i * j)
        print('\t'.join([str(i) for i in row]))

multiplication_table_1(3, 5)