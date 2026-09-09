# 🦈 Wireshark

## Objetivo
Aprender análise de tráfego e leitura de PCAPs para investigação, troubleshooting e detecção.

## Conceitos
- captura vs análise offline
- Ethernet, IP, TCP/UDP, DNS, HTTP/HTTP2
- filtros de captura e display filters
- streams e reassembly
- flags TCP, portas, hosts e protocolos
- identificação de indicadores suspeitos

## Filtros úteis
```text
ip.addr == 10.10.10.10
tcp.port == 80
http
http.request
dns
tcp.stream eq 0
```

## Metodologia
Começar por visão geral → identificar conversas → filtrar por protocolo/host → seguir streams → correlacionar timestamps e evidências.

## Status
**Estudado / prática registrada.** Já houve estudo de Wireshark/PCAP e análise de pacotes no processo de aprendizagem.

## Referências
- https://www.wireshark.org/docs/
- https://wiki.wireshark.org/DisplayFilters
