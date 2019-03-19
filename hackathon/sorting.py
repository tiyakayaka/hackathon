def bubble_sort(items):
   """ Implementation of bubble sort """
   out = items.copy() # in place protection on items
   for i in range(len(out)):
       for j in range(len(out)-1-i):
           if out[j] > out[j+1]:
               out[j], out[j+1] = out[j+1], out[j]     # Swap!

   return out


def merge(A, B):
  new_list = []
  while len(A) > 0 and len(B) > 0:
      if A[0] < B[0]:
          new_list.append(A[0])
          A.pop(0)
      else:
          new_list.append(B[0])
          B.pop(0)
  if len(A) == 0:
      new_list = new_list + B
  if len(B) == 0:
      new_list = new_list + A
  return new_list


def merge_sort(items):

   len_i = len(items)
   if len_i == 1:
       return items

   mid_point = int(len_i / 2)
   i1 = merge_sort(items[:mid_point])
   i2 = merge_sort(items[mid_point:])

   return merge(i1, i2)


def quick_sort(items, index=-1):
   """
   the quick sort algorithm takes in an unsorted list of numbers.
   returns a list in ascending order.

   Parameters
   ----------
   items : list
       list of unordered numbers
   index: int, optional
       index number at which to choose the split value
       default set to the last item in the input list

   Returns
   -------
   list
       list of elements in items in ascending order
   """
   len_i = len(items)

   if len_i <= 1:
       # Logic Error
       # identified with test run [1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1]
       # len <= 1
       return items

   pivot = items[index]
   small = []
   large = []
   dup = []
   for i in items:
       if i < pivot:
           small.append(i)
       elif i > pivot:
           large.append(i)
       elif i == pivot:
           dup.append(i)

   small = quick_sort(small)
   large = quick_sort(large)

   return small + dup + large
