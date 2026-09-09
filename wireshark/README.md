# 🦈 Wireshark

Análise de tráfego e PCAP para troubleshooting, investigação e detecção.

## Tópicos
Ethernet, IP, TCP/UDP, DNS, HTTP/HTTP2, streams, filtros, reassembly e indicadores.

## Filtros-base
`ip.addr == X.X.X.X`, `tcp.port == 80`, `dns`, `http.request`, `tcp.stream eq 0`.

## Método
Visão geral → conversa → filtro → stream → timestamps → correlação.

## Referências
[Wireshark Docs](https://www.wireshark.org/docs/) · [Display Filters](https://wiki.wireshark.org/DisplayFilters)

**Status:** 🟡 estudado / prática registrada