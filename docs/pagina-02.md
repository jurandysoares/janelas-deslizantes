# 2. Por que precisamos de uma janela?

No mecanismo mais simples, o emissor faz:

```text
enviar → esperar ACK → enviar → esperar ACK → ...
```

Se o atraso de propagação for significativo, o transmissor pode passar grande parte do tempo esperando.

Com uma janela, ele pode fazer:

```text
enviar → enviar → enviar → enviar → ...
                 ↑
              ACKs chegam
```

Enquanto as primeiras unidades estão viajando, outras podem ser transmitidas.

Uma janela de tamanho 4 pode ser representada assim:

```text
        ┌─────────────────┐
        │ 0 │ 1 │ 2 │ 3   │
        └─────────────────┘
```

Depois que 0 e 1 são confirmados, a janela avança:

```text
            ┌─────────────────┐
            │ 2 │ 3 │ 4 │ 5   │
            └─────────────────┘
```

É esse deslocamento que dá origem ao termo **janela deslizante**.
