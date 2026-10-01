# Da espera à janela deslizante

A janela generaliza o Stop-and-Wait: em vez de permitir somente uma unidade não confirmada, o transmissor pode manter várias.

```text
Antes:

    +---------------+
    | 0 | 1 | 2 | 3 |
    +---------------+

Depois de confirmar 0 e 1:

      0   1   +---+---+---+---+   6   7
              | 2 | 3 | 4 | 5 |
              +---+---+---+---+
              <---- janela --->
```

A janela contém, conceitualmente, os números de sequência que estão dentro do espaço de transmissão permitido naquele momento.
