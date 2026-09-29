# Repetição Seletiva

## Motivação

No cenário:

```text
0: OK
1: OK
2: PERDA
3: OK
4: OK
```

o receptor já possui 3 e 4. Retransmiti-los seria desnecessário se o protocolo conseguir armazená-los enquanto aguarda o quadro 2.

A **Repetição Seletiva** procura retransmitir somente as unidades que precisam de recuperação.

## Exemplo

```mermaid
sequenceDiagram
    participant E as Emissor
    participant R as Receptor
    E->>R: Quadro 0
    R-->>E: ACK 0
    E->>R: Quadro 1
    R-->>E: ACK 1
    E->>R: Quadro 2
    Note over E,R: Quadro 2 perdido
    E->>R: Quadro 3
    Note over R: Quadro 3 recebido e armazenado
    R-->>E: ACK 3
    E->>R: Quadro 4
    Note over R: Quadro 4 recebido e armazenado
    R-->>E: ACK 4
    Note over E: Detecta necessidade de recuperar 2
    E->>R: Retransmissão do quadro 2
    R-->>E: ACK 2
```

Depois de recuperar o quadro 2, o receptor pode integrar os dados que já havia armazenado.
