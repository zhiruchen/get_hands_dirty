# encoding: utf-8


def msort(mlist):
    """select sort"""
    for n in range(len(mlist)-1):
		min_pos = n
		for pos in range(n+1, len(mlist)):
		    if mlist[pos] < mlist[min_pos]:
		        min_pos = pos

		if min_pos != n:
		    mlist[n], mlist[min_pos] = mlist[min_pos], mlist[n]

    return mlist


if __name__ == '__main__':
	print msort([1,3,2,4,5])