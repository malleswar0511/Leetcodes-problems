def medainoftwosortedarrays(l1,l2):
    mergedlist =l1+l2
    mergedlist.sort()
    median_len = len(mergedlist)
    if median_len % 2==1:
        return mergedlist[median_len//2]
    else:
        return (mergedlist[median_len//2-1]+mergedlist[median_len//2])/2
    
    
nums1 = [1,3]
nums2 = [2]
print(medainoftwosortedarrays(nums1,nums2))

nums1 = [1,2]
nums2 = [3,4]
print(medainoftwosortedarrays(nums1,nums2))