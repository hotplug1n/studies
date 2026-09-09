# Wireshark: The Basics

> Categoria: Wireshark / Networking
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Aprender a navegar em capturas, dissecar pacotes e usar display filters para encontrar evidências em tráfego.

## Conceitos aprendidos
- PCAP/PCAPNG
- camadas TCP/IP
- campos de pacote
- filtros de exibição
- streams e correlação temporal
- análise de HTTP/DNS/TCP

## Ferramentas
Wireshark e terminal com `tshark` quando útil.

## Comandos importantes
```bash
tshark -r captura.pcapng
```

Filtros:
```text
ip.addr == 10.10.10.10
http.request
dns
tcp.port == 80
tcp.stream eq 0
```

## Metodologia
Abrir PCAP → identificar protocolos dominantes → restringir por host/porta → seguir streams → registrar artefatos relevantes.

## O que eu aprendi
Já houve estudo prático de Wireshark/PCAP, inclusive filtragem e análise de pacotes. A documentação não afirma conclusão oficial da room.

## Lições importantes
O contexto temporal e a relação entre pacotes frequentemente importam mais que um único pacote isolado.

## Referências
- https://tryhackme.com/room/wiresharkthebasics
- https://www.wireshark.org/docs/
