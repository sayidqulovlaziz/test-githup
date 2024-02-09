def olibtashlash(head, n):
    a = Listtugun(0)
    a.next = head

    sekin = a
    tez = a
    for _ in range(n):
        tez = tez.next
    while tez.next:
        sekin = sekin.next
        tez = tez.next
    sekin.next = sekin.next.next
    tugun = a.next
    result = []
    while tugun:
        result.append(tugun.val)
        tugun = tugun.next

    return result
head = [1,2,3,4,5]
n = 2
natija = olibtashlash(head, n)
print(natija)

head = [1]
n = 1
natija = olibtashlash(head, n)
print(natija)

head = [1, 2]
n = 1
natija = olibtashlash(head, n)
print(natija)