import linkedlist

my_list = linkedlist.LinkedList()

assert my_list.is_empty() == True, "Esta correcto"

my_list.push_front(0)
my_list.push_back(1)
my_list.push_back(2)
my_list.push_back(3)

assert my_list.is_empty() == False, "is_empty es correcto"
assert my_list.size() == 4, "size esta correcto"
my_list.display()

my_list.pop_back()
my_list.pop_front()

my_list.display()

print(my_list.front())
print(my_list.back())