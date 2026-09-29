# Relação com eficiência do enlace

Considere um enlace no qual o tempo de ida e volta é grande em relação ao tempo necessário para transmitir um quadro.

Stop-and-Wait:

```mermaid
sequenceDiagram
    participant T as Transmissor
    participant R as Receptor

    T->>R: Dados
    R-->>T: Confirmacao

    T->>R: Dados
    R-->>T: Confirmacao
```

Janela deslizante:

```mermaid
sequenceDiagram
    participant T as Transmissor
    participant R as Receptor

    T->>R: Dados 1
    T->>R: Dados 2
    T->>R: Dados 3
    T->>R: Dados 4

    R-->>T: Confirmacao
```

A segunda estratégia permite sobrepor transmissão e espera por confirmações, mantendo mais dados em trânsito.
