# encoding: utf-8


def sort(mlist):
	llen = len(mlist)

	for n in range(llen-1):
		for i in range(llen-n-1):
			if mlist[i] > mlist[i+1]:
				mlist[i+1], mlist[i] = mlist[i], mlist[i+1]

	return mlist
