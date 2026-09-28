# 15. Analogia

Imagine um professor entregando exercícios numerados.

### Stop-and-Wait

```text
Professor → Exercício 1 → Aluno
Professor ← "Recebi" ← Aluno
Professor → Exercício 2 → Aluno
```

### Go-Back-N

O professor pode entregar vários:

```text
1 → 2 → 3 → 4 → 5
```

Se o exercício 3 não chegar, ele volta ao ponto da falha:

```text
3 → 4 → 5
```

### Repetição Seletiva

Se 4 e 5 já chegaram, mas 3 não:

```text
3
```

é suficiente para recuperar a lacuna, desde que o aluno possa guardar 4 e 5 temporariamente.
