# encoding: utf-8


def merge_list(data_list):
	data_len = len(data_list)
	i, j = 0, 1

	while data_list[i] <= data_list[j] and j < data_len:
		i += 1
		j += 1
			

	incr_list, decre_list = data_list[:j], data_list[j:][::-1]
	print incr_list, decre_list
	m, n, k = 0, 0, 0

	while m < len(incr_list) and n < len(decre_list):
		if incr_list[m] < decre_list[n]:
			data_list[k] = incr_list[m]
			m += 1
		else:
			data_list[k] = decre_list[n]
			n += 1

		k += 1


	while m < len(incr_list):
		data_list[k] = incr_list[m]
		k, m = k + 1, m + 1

	while n < len(decre_list):
		data_list[k] = decre_list[n]
		k, n = k + 1, n + 1

	return data_list
