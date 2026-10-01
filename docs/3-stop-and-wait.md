# Stop-and-Wait

## Funcionamento

No **Stop-and-Wait**, o emissor transmite uma unidade de dados e aguarda sua confirmação antes de transmitir a próxima.

```mermaid
sequenceDiagram
    autonumber
    participant E as Emissor
    participant R as Receptor
    E->>R: Quadro 0
    R-->>E: ACK 0
    E->>R: Quadro 1
    R-->>E: ACK 1
    E->>R: Quadro 2
    R-->>E: ACK 2
```

Existe, portanto, no máximo uma unidade não confirmada.

## Perda de dados

Se um quadro for perdido, o emissor precisa de um mecanismo para detectar que a confirmação não chegou. Normalmente, isso envolve um **temporizador** e uma retransmissão após o timeout.

```mermaid
sequenceDiagram
    autonumber
    participant E as Emissor
    participant R as Receptor
    E -x R: Quadro 0
    Note over E,R: Quadro perdido
    Note over E: Timeout
    E->>R: Retransmissão do quadro 0
    R-->>E: ACK 0
```

## ACK perdido e duplicatas

O quadro pode chegar ao receptor, mas o ACK pode ser perdido. O emissor então retransmite o mesmo quadro. O receptor precisa reconhecer que se trata de uma duplicata.

```mermaid
sequenceDiagram
    autonumber
    participant E as Emissor
    participant R as Receptor
    E->>R: Quadro 0
    R --x E: ACK 0
    Note over E,R: ACK perdido
    Note over E: Timeout
    E->>R: Quadro 0 (retransmissão)
    Note over R: Quadro já recebido
    R-->>E: ACK 0
```

Por isso, **números de sequência** são fundamentais em protocolos que precisam distinguir dados novos de retransmissões.
