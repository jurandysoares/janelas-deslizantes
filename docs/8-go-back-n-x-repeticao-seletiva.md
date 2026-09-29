# 8. Go-Back-N × Repetição Seletiva

Considere:

```text
0 ✓
1 ✓
2 ✗
3 ✓
4 ✓
```

No **Go-Back-N**, a perda pode levar à retransmissão de:

```text
2 → 3 → 4
```

Na **Repetição Seletiva**, a recuperação pode ser:

```text
2
```

```mermaid
flowchart TB
    A["Quadro 2 perdido"]
    A --> B["Go-Back-N"]
    A --> C["Repetição Seletiva"]
    B --> D["Retransmite 2 e unidades posteriores necessárias"]
    C --> E["Retransmite somente 2"]
```

A vantagem da repetição seletiva é evitar retransmissões desnecessárias. Em contrapartida, ela exige mecanismos mais sofisticados para armazenar e administrar dados recebidos fora de ordem.
