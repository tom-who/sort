class QuickSortWithCounters:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def quicksort(self, arr):
        self._quicksort_helper(arr, 0, len(arr) - 1)

    def _quicksort_helper(self, arr, low, high):
        if low < high:
            partition_index = self._partition(arr, low, high)
            self._quicksort_helper(arr, low, partition_index - 1)
            self._quicksort_helper(arr, partition_index + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]  # Pivot element
        i = low - 1  # Index of smaller element
        for j in range(low, high):
            self.comparisons += 1  # Increment comparisons counter
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1  # Increment swaps counter
        # Swap the pivot element with the element at i+1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1  # Increment swaps counter
        return i + 1

    def get_counters(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}


# Example usage
if __name__ == "__main__":
    sorter = QuickSortWithCounters()
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    sorter.quicksort(arr)
    print("Sorted array:", arr)
    counters = sorter.get_counters()
    print("Counters:", counters)
