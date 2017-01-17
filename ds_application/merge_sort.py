# encoding: utf-8


def merge_sort(mlist):
    if len(mlist) > 1:
        mid = len(mlist) / 2
        left_half = mlist[:mid]
        right_half = mlist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                mlist[k] = left_half[i]
                i += 1
            else:
                mlist[k] = right_half[j]
                j += 1
            k += 1

        for n in left_half[i:]:
            mlist[k] = n
            k += 1

        for n in right_half[j:]:
            mlist[k] = n
            k += 1
