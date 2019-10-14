def merge(llist, rlist):
   5         """
   6         Merge two lists into an ordered list.
   7         """
   8         final = []
   9         while llist or rlist:
  10                 # This verification is necessary for not try to compare
  11                 # a NoneType with a valid type.
  12                 if len(llist) and len(rlist):
  13                         if llist[0] < rlist[0]:
  14                                 final.append(llist.pop(0))
  15                         else:
  16                                 final.append(rlist.pop(0))
  17 
  18                 # This two conditionals here, is for the case when the two lists
  19                 # have diferent sizes. This save us of an error trying to acess
  20                 # an index out of range.
  21                 if not len(llist):
  22                                 if len(rlist): final.append(rlist.pop(0))
  23 
  24                 if not len(rlist):
  25                                 if len(llist): final.append(llist.pop(0))
  26 
  27         return final
  28 
  29 def merge_sort(list):
  30         """
  31         Sort the list passed by argument with merge.
  32         """
  33         if len(list) < 2: return list
  34         mid = len(list) / 2
  35         return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))
