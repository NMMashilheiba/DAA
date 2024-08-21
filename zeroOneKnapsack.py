# 0/1 knapsack using dp

n = 3
profits = [60, 100, 120, 232, 12, 33]
weights = [5, 2, 3, 4, 6, 7]
c = 5

def knapsack(c, ps, ws):
	n = len(ps)
	table = [[0 for _ in range(0, c + 1)] for _ in range(0, n)]
	# print(table)

	for i in range(0, n):
		for w in range(1, c + 1):
			if ws[i]<= w:
				# print(ws[i], w)
				table[i][w] = max(table[i - 1][w], table[i - 1][w - ws[i]] + ps[i])
				# print(table)
			else:
				table[i][w] = table[i - 1][w]

	# print(table)

	for row in table:
		print(' '.join(f'{x:3}' for x in row))



knapsack(c, profits, weights)