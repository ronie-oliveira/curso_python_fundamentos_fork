'''
Lista
As listas são usadas para armazenar vários itens em uma única variável.

As listas são um dos 4 tipos de dados internos em Python usados para armazenar coleções de Os outros 3 são Tuple, Set e Dicionário, todos com qualidades e usos diferentes.

As listas são criadas usando colchetes:
'''

# [].append
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]

# [].clear
lista = [1, "Python", [40, 30, 20]]

lista.clear()
print(lista) # []

# [].copy
lista = [1, "Python", [40, 30, 20]]

lista.copy()
print(lista) # [1, "Python", [40, 30, 20]]


# [].count
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1
print(cores)

# [].extend
linguagens = ["python", "js", "c"]
print(linguagens) # ["python", "js", "c"]
linguagens.extend(["java", "csharp"])
print(linguagens)

# [].index
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java") # 3
linguagens.index("python") # 0

# [].pop
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python

# [].remove
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")
print(linguagens) # ["python", "js", "java", "csharp"]

# [].reverse
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()
print(linguagens) # ["csharp", "java", "c", "js", "python"]

# [].sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]

# len
linguagens = linguagens = ["python", "js", "c", "java", "csharp"]
len(linguagens) # 5

# sorted
linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python"]
sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]






















