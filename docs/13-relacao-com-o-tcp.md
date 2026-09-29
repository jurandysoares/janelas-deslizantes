# Relação com o TCP

O estudo de Stop-and-Wait, Go-Back-N e Repetição Seletiva fornece uma base conceitual para compreender números de sequência, ACKs, retransmissões, temporizadores e janelas.

Entretanto, **não é correto simplesmente classificar o TCP como Go-Back-N ou como Repetição Seletiva**. O TCP possui mecanismos próprios e combina controle de fluxo, retransmissão e controle de congestionamento.

A RFC 9293 especifica o TCP como um serviço confiável e ordenado de **fluxo de bytes**. Portanto, o modelo didático dos protocolos de janela deve ser usado para compreender princípios, e não como uma identificação literal do TCP com um desses protocolos.
