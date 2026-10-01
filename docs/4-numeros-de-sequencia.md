# Números de sequência

As unidades podem receber números de sequência como:

```text
0  1  2  3  4  5  6  ...
```

O número de sequência permite identificar a unidade e ajuda o receptor a reconhecer duplicatas e ordenar dados.

```mermaid
sequenceDiagram
    autonumber
    participant E as Transmissor
    participant R as Receptor
    E->>R: Quadro 0
    R --x E: ACK 0
    Note over E,R: ACK perdido
    E->>R: Quadro 0 (retransmissão)
    Note over R: "Já recebi o quadro 0"
    R-->>E: ACK 0
```
