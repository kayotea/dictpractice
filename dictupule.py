# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def dictTuple(dic):
    lst = []
    tup = ()
    for key in dic:
        tup += (key,)
        tup += (dic[key],)
        lst.append(tup)
        tup = ()
    return lst


print dictTuple(my_dict)