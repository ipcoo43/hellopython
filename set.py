print('set : 집합을 의미')


s1 = {1,2,3}
s2 = {3,4,5}

print('s1 =',s1)
print('ss =',s2)
print('합집합(|) : s1|s2 =', s1|s2)
print('교집합(&) : s1&s2 =', s1&s2)
print('차집합(^) : s1^s2 =', s1^s2)
print('합집합 : s1.union(s2) =', s1.union(s2))
ss = s1.union(s2)
print('s1 =',s1)
print('s1.update(s2) = ',s1.update(s2))
print('s1 = ',s1)