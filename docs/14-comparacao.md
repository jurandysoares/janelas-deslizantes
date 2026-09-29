# Comparação

| Característica | Stop-and-Wait | Go-Back-N | Repetição Seletiva |
| --- | --- | --- | --- |
| Unidades simultaneamente em trânsito | 1 | Várias | Várias |
| Janela | Efetivamente 1 | Sim | Sim |
| Recuperação de perda | Unidade pendente | Perda e posteriores necessários | Somente unidades necessárias |
| Recepção fora de ordem | Não é necessária | Geralmente não aproveitada | Pode ser armazenada |
| Complexidade | Baixa | Intermediária | Maior |
| Armazenamento no receptor | Pequeno | Menor | Maior |

A evolução pode ser resumida assim:

```mermaid
flowchart LR
    A["Stop-and-Wait"] -->|"mais unidades em trânsito"| B["Janela deslizante"]
    B --> C["Go-Back-N"]
    B --> D["Repetição Seletiva"]
    C -->|"recuperação em bloco"| E["mais retransmissões"]
    D -->|"recuperação seletiva"| F["menos retransmissões"]
```
