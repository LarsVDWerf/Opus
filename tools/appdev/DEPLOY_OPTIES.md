# Deploy-opties

Drie routes, van minst naar meest complex. Kies per app op basis van eisen.

**Nichts wordt gedeployed zonder STOP-punt uit DRAAIBOEK.md Fase 5.**

---

## Route A — Coolify (voorkeur voor eigen stack)

### Wat is het
Coolify is een self-hosted PaaS (Platform as a Service). Beheert containers, domeinen en SSL automatisch. Meest geschikt als Coolify al draait op jouw infrastructuur.

### Wat Opus van jou nodig heeft
- **Coolify URL**: het adres van jouw Coolify-instantie (bijv. `https://coolify.jouwdomein.nl`)
- **Coolify API Token**: te maken via Coolify → Account Settings → API Tokens
- **Doelserver**: welke server in Coolify gebruik je? (server-ID of naam)
- **Domein voor de app**: bijv. `appnaam.jouwdomein.nl` (DNS moet naar de server wijzen)

### Stappen (door Opus, na credentials van Lars)
1. Maak een Dockerfile aan in `apps/<naam>/Dockerfile`
2. Maak een nieuwe Resource aan in Coolify: type Dockerfile of Docker Compose
3. Koppel de git-repo of upload de image
4. Stel omgevingsvariabelen in via Coolify UI (geen secrets in git)
5. Trigger de eerste deploy
6. Verifieer: health-endpoint, logs, domein

### Risico's
- **DNS-propagatie**: kan tot 48 uur duren bij nieuw domein
- **SSL-certificaat**: Coolify regelt Let's Encrypt, maar vereist correcte DNS
- **Rollback**: via Coolify redeploy naar vorige deployment; snel maar vereist handmatige actie

---

## Route B — Losse Docker-container (op server via SSH)

### Wat is het
Direct een container draaien op een server, zonder PaaS. Meer controle, meer handwerk.

### Wat Opus van jou nodig heeft
- **SSH-toegang**: host, gebruiker, SSH-sleutel (of wachtwoord)
- **Server**: IP-adres of hostname van de doelserver
- **Poort**: welke poort mag de app gebruiken?
- **Reverse proxy**: staat er al een Nginx/Caddy/Traefik op de server? Zo ja, configuratie-pad

### Stappen (door Opus, na credentials van Lars)
1. Bouw de Docker-image lokaal: `docker build -t appnaam .`
2. Stuur de image naar de server: `docker save | ssh server docker load`
3. Stop de eventueel draaiende vorige versie
4. Start de nieuwe container: `docker run -d --name appnaam -p poort:poort appnaam`
5. Verifieer logs en health
6. Werk reverse proxy-config bij indien nodig

### Risico's
- **Geen automatische SSL**: moet handmatig geregeld worden via Certbot of reverse proxy
- **Geen zero-downtime**: er is een korte onderbreking bij update (tenzij blue/green opgezet)
- **Geen automatisch herstarten bij crash**: gebruik `--restart unless-stopped` in docker run
- **Rollback**: handmatig; bewaar vorige image-tag

---

## Route C — Alternatief (voor specifieke gevallen)

Opties die besproken moeten worden met Lars voordat ze ingezet worden:

| Optie | Wanneer | Wat nodig |
|---|---|---|
| VPS (bare metal, geen Docker) | Eenvoudige Python-scripts als service | SSH, systemd, minder isolatie |
| Serverless (bijv. Cloudflare Workers) | Stateless functies, weinig state | CF account, domein, wrangler CLI |
| Lokaal (alleen op jouw machine) | Persoonlijke tools, geen extern verkeer | Geen deploy, gewoon draaien |

**STOP:** kies een route samen met Lars. Zet de keuze in `apps/<naam>/SPEC.md` voordat er gebouwd wordt.

---

## Credentials-beleid

- Nooit credentials in git (`.env` staat in `.gitignore`)
- Gebruik `.env.example` met variabelenamen maar geen waarden
- Productie-secrets worden door Lars ingevoerd via Coolify UI of via SSH, nooit door Opus aangemaakt
