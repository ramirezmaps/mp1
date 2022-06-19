
curso = {'972-1':('Aurora',[67,56,48]),
'580-2':('Sebastian',[28,60,38]),
'632-7':('Rafaela',[53,72,22]),
'900-4':('Dario',[61,1,42])}

prom = 0

print(curso)

for v in curso.values():
    prom = prom + v[1][2]

prom = prom / len(curso)

print(f"el promedio del tercer elemento corresponde a: {prom}")