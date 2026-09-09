# 🛡️ studies — Cybersecurity Knowledge Base

Repositório pessoal para documentar minha evolução em **cibersegurança**, com foco em fundamentos, prática de laboratório, ferramentas, investigação e documentação técnica.

> **Regra de segurança:** conteúdos ofensivos aqui são destinados somente a CTFs, máquinas de laboratório, ambientes próprios ou sistemas para os quais exista autorização explícita.

## 🧭 Mapa de estudos

| Área | Conteúdo |
|---|---|
| 🌐 [Networking](./networking/) | TCP/IP, OSI, DNS, DHCP, ARP e roteamento |
| 🐧 [Linux](./linux/) | shell, filesystem, processos e permissões |
| 🔎 [Nmap Recon](./nmap-recon/) | descoberta, portas, serviços e enumeração |
| 🌐 [Web Security](./web-security/) | HTTP, autenticação, injeção e OWASP |
| 🧪 [Burp Suite](./burp-suite/) | Proxy, Repeater, Intruder e análise |
| 🦈 [Wireshark](./wireshark/) | PCAP, filtros e análise de tráfego |
| 🔑 [Cryptography](./cryptography/) | hashes, criptografia simétrica e assimétrica |
| 💥 [Exploitation](./exploitation/) | exploração em laboratórios e pós-exploração |
| 🪟 [Windows Security](./windows-security/) | Windows, PowerShell, eventos e AD |
| 📡 [Network Attacks](./network-attacks/) | ataques e defesa de camada de rede |
| 🔵 [Blue Team](./blue-team/) | monitoramento, detecção e resposta |
| 📊 [Splunk](./splunk/) | SIEM, ingestão, pesquisa e investigação |
| 🔍 [OSINT & Privacy](./osint-privacy/) | fontes abertas e privacidade |
| 🌿 [Git Security](./git-security/) | histórico, segredos e segurança de repositórios |
| 🎯 [TryHackMe](./tryhackme/) | catálogo e documentação das rooms |
| 🧪 [Projects](./projects/) | projetos próprios para transformar estudo em evidência prática |

## 🧪 Projetos práticos

### [Mini SOC Lab](./projects/mini-soc-lab/)

Laboratório defensivo em **Python** para analisar eventos de autenticação e gerar alertas de:

- brute force;
- login bem-sucedido após falhas;
- direcionamento a contas administrativas.

**Stack:** Python · Linux · Blue Team · Log Analysis

## 📚 TryHackMe

As rooms ficam em um único lugar: [`tryhackme/`](./tryhackme/).

- [`COMPLETED-ROOMS.md`](./tryhackme/COMPLETED-ROOMS.md) — lista das 76 rooms identificadas nas capturas do perfil.
- [`rooms/`](./tryhackme/rooms/) — documentação individual e padronizada.
- [`research/`](./tryhackme/research/) — pesquisas que não representam conclusão pessoal.

O perfil mostrado nas capturas informa **78 completed rooms**; 76 puderam ser identificadas nominalmente.

## 🎯 Status da documentação

- **✅ Concluído:** há evidência de conclusão da room no perfil.
- **🟡 Estudado / evidenciado:** há registro de estudo/prática no processo de aprendizagem.
- **🟠 Em andamento:** assunto iniciado, mas ainda em desenvolvimento.
- **🔎 Conteúdo pesquisado:** material usado como referência sem alegação de conclusão.

## 🧪 Metodologia

1. Entender o conceito.
2. Reproduzir em laboratório autorizado.
3. Registrar comandos e observações.
4. Explicar o porquê, não apenas o procedimento.
5. Relacionar ataque, impacto, detecção e mitigação quando aplicável.
6. Transformar os aprendizados mais importantes em projetos próprios.

## 📚 Referências-base

- [TryHackMe](https://tryhackme.com/)
- [OWASP](https://owasp.org/)
- [NIST](https://www.nist.gov/cybersecurity)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Wireshark](https://www.wireshark.org/docs/)
- [Nmap](https://nmap.org/docs.html)

---

**Status:** 🚧 Em construção contínua
