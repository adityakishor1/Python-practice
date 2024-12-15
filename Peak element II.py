class Solution:   
    def peakElement(self, arr):
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return mid
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
