# Networking Secure Protocols

> Categoria: Networking Security
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Entender como TLS, SSH, VPN e variantes seguras protegem comunicação.

## Conceitos aprendidos
- TLS e HTTPS
- SSH no lugar de Telnet
- SFTP/FTPS
- VPN e túneis seguros

## Ferramentas
`ssh`, `openssl s_client`, navegador e análise de certificados.

## Comandos importantes
```bash
ssh user@LAB_IP
openssl s_client -connect example.com:443
```

## Metodologia
Identificar protocolo → verificar proteção → analisar certificado/chave → observar risco residual.

## O que aprendi
Consolidei que “seguro” depende de autenticação, integridade e confidencialidade, não apenas de uma porta diferente.

## Documentação de apoio
https://tryhackme.com/room/networkingsecureprotocols · https://www.openssl.org/docs/

## Evidência
Room concluída no perfil apresentado.