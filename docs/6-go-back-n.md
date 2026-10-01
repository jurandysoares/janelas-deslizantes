# Go-Back-N

## Ideia geral

No **Go-Back-N (GBN)**, o transmissor pode enviar várias unidades antes de receber confirmações. Quando ocorre uma perda, a recuperação volta ao ponto da falha e reenvia a unidade perdida e as unidades posteriores que precisam ser recuperadas.

Considere:

```text
0: OK
1: OK
2: PERDA
3: PENDENTE
4: PENDENTE
```

Se o quadro 2 for perdido, o receptor não dispõe do quadro esperado para continuar a sequência normalmente.

## Exemplo de perda

```mermaid
sequenceDiagram
    autonumber
    participant E as Transmissor
    participant R as Receptor
    E->>R: Quadro 0
    R-->>E: ACK 0
    E->>R: Quadro 1
    R-->>E: ACK 1
    E-x R: Quadro 2
    Note over E,R: Quadro 2 perdido
    E->>R: Quadro 3
    Note over R: Esperava o quadro 2
    R-->>E: ACK cumulativo / próximo esperado: 2
    Note over E: Timeout / detecção da perda
    E->>R: Retransmissão do quadro 2
    E->>R: Retransmissão do quadro 3
```

O ponto essencial é que o GBN pode retransmitir dados que chegaram ao receptor depois da perda, mas que precisam ser reenviados para recuperar a sequência.

## ACK cumulativo

Um **ACK cumulativo** pode confirmar, de uma só vez, que todas as unidades anteriores a determinado ponto foram recebidas corretamente.

Por exemplo, se o próximo quadro esperado é 5:

```text
0 ✓   1 ✓   2 ✓   3 ✓   4 ✓   5 <= próximo esperado
```

Uma confirmação indicando 5 pode representar o recebimento correto de 0 a 4, conforme a convenção de numeração adotada pelo protocolo.
