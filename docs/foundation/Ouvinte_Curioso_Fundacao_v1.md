# Ouvinte Curioso — Documento de Fundação v1

## 1. Visão

Ouvinte Curioso é um app mobile-first para transformar a escuta casual em descoberta musical contextual.

Ele acompanha o que o usuário está ouvindo no Spotify e entrega contexto, curiosidades, referências e respostas com IA, sem tentar substituir o Spotify e sem reproduzir conteúdo protegido indevidamente.

## 2. Objetivo inicial

Enquanto uma música toca no Spotify, o usuário abre o Ouvinte Curioso e em até 5 segundos entende melhor o que está ouvindo.

## 3. Posicionamento

Ouvinte Curioso não é um player musical.

É um companion de escuta para pessoas curiosas que querem entender melhor músicas, artistas, álbuns, cenas, referências e contextos culturais.

## 4. Princípios de produto

* complementar o Spotify, não competir com ele;
* mobile-first;
* foco em descoberta contextual rápida;
* evitar reprodução indevida de conteúdo protegido;
* não depender de letras completas no MVP;
* entregar valor mesmo com pouca interface;
* começar simples e validar uso real.

## 5. Stack validada pela POC

Frontend futuro:

* Angular v21;
* Vitest;
* mobile-first/PWA.

Backend validado:

* Python 3.13;
* FastAPI;
* uv;
* Pydantic;
* pydantic-settings;
* httpx;
* pytest;
* ruff;
* PostgreSQL via Docker Compose.

Integração validada:

* Spotify OAuth;
* Spotify Web API;
* endpoint currently-playing;
* sessão server-side via cookie assinado;
* DTO limpo para consumo futuro do Angular.

## 6. Resultado da POC backend

A POC validou que o backend consegue:

* autenticar usuário via Spotify;
* trocar authorization code por token no backend;
* manter tokens fora do frontend;
* consultar a música atualmente tocando;
* retornar um DTO limpo;
* rodar localmente no Windows com Docker;
* passar testes básicos e lint.

## 7. Decisão técnica

A stack backend Python + FastAPI está aprovada para servir como base do MVP.

A POC pode ser aproveitada como fundação inicial, desde que evolua com persistência adequada de sessão/tokens, organização mínima de domínio e critérios de segurança.

## 8. Fora do MVP inicial

* player próprio;
* Web Playback SDK;
* letras completas;
* análise profunda de letra;
* Genius;
* MusicBrainz;
* deploy complexo;
* monetização;
* login Google;
* recomendações avançadas;
* histórico extenso;
* arquitetura excessivamente complexa.

## 9. MVP proposto

O MVP deve permitir que o usuário:

1. acesse o app;
2. conecte sua conta Spotify;
3. veja a música atual;
4. receba um resumo contextual rápido;
5. faça perguntas simples sobre a música/artista;
6. tenha uma experiência mobile-first limpa.

## 10. Critério central de sucesso

O usuário deve conseguir abrir o app durante uma música tocando no Spotify e receber contexto útil em até 5 segundos.
