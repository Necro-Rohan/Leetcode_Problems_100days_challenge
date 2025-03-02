class Solution:
    def sortEvenOdd(self, arr: List[int]) -> List[int]:
        even_indices_arr = [i for i in range(len(arr)) if i%2 == 0]
        odd_indices_arr = [i for i in range(len(arr)) if i%2 == 1]

        for i in range(len(even_indices_arr)):
            max_idx = i 
            for j in range(i,len(even_indices_arr)):
                if arr[even_indices_arr[j]] < arr[even_indices_arr[max_idx]]:
                    max_idx = j 
            arr[even_indices_arr[i]], arr[even_indices_arr[max_idx]] = arr[even_indices_arr[max_idx]], arr[even_indices_arr[i]]

        for i in range(len(odd_indices_arr)):
            min_idx = i
            for j in range(i,len(odd_indices_arr)):
                if arr[odd_indices_arr[j]] > arr[odd_indices_arr[min_idx]]:
                    min_idx = j 
            arr[odd_indices_arr[i]], arr[odd_indices_arr[min_idx]] = arr[odd_indices_arr[min_idx]], arr[odd_indices_arr[i]]
        return arr 

        